from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LANGS = {"en", "ko", "ja", "zh"}
HTML_FILES = sorted(ROOT.rglob("*.html"))

PAGE_DATA_START = "  <script id=\"studyhub-page-data\">\n"
PAGE_DATA_END = "  </script>\n"
APP_MARKER = "studyhub-app"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value).strip()


def find_first(pattern: str, text: str, default: str = "") -> str:
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else default


def compute_page_type(rel_path: Path) -> str | None:
    parts = rel_path.parts
    name = rel_path.name
    if name.startswith("google"):
        return None
    if rel_path == Path("404.html"):
        return "404"
    if rel_path == Path("index.html"):
        return "global-home"
    if len(parts) == 2 and parts[0] in LANGS and name == "index.html":
        return "language-home"
    if len(parts) == 3 and parts[0] in LANGS and name == "index.html":
        return "section-index"
    if len(parts) == 3 and parts[0] in LANGS and name.endswith(".html"):
        return "article"
    return "generic"


def build_section_catalog() -> dict[tuple[str, str], dict]:
    catalog: dict[tuple[str, str], dict] = {}
    for rel_path in [p.relative_to(ROOT) for p in HTML_FILES]:
        if compute_page_type(rel_path) != "section-index":
            continue
        text = read_text(ROOT / rel_path)
        lang, section, _ = rel_path.parts
        section_title = strip_tags(find_first(r"<h1[^>]*>(.*?)</h1>", text, section.title()))
        links = []
        for href, title in re.findall(
            r'<a href="([^"]+\.html)" class="topic-card">.*?<h3>(.*?)</h3>',
            text,
            re.IGNORECASE | re.DOTALL,
        ):
            links.append({"href": href, "title": strip_tags(title)})
        catalog[(lang, section)] = {"title": section_title, "links": links}
    return catalog


def page_payload(rel_path: Path, page_type: str, section_catalog: dict[tuple[str, str], dict]) -> dict:
    parts = rel_path.parts
    lang = parts[0] if parts and parts[0] in LANGS else "en"
    payload: dict = {"path": rel_path.as_posix(), "type": page_type, "lang": lang}

    if page_type == "global-home":
        payload["languageCount"] = 4
        payload["subjectCount"] = 3
    elif page_type == "language-home":
        payload["sectionCount"] = 3
    elif page_type == "section-index":
        _, section, _ = parts
        catalog = section_catalog.get((lang, section), {})
        payload["section"] = section
        payload["sectionTitle"] = catalog.get("title", section.title())
        payload["links"] = catalog.get("links", [])
        payload["topicCount"] = len(payload["links"])
        if payload["links"]:
            payload["firstTopic"] = payload["links"][0]
    elif page_type == "article":
        _, section, name = parts
        catalog = section_catalog.get((lang, section), {})
        links = catalog.get("links", [])
        current_index = next((i for i, item in enumerate(links) if item["href"] == name), -1)
        related = [item for item in links if item["href"] != name][:4]
        payload.update(
            {
                "section": section,
                "sectionTitle": catalog.get("title", section.title()),
                "sectionHref": "./",
                "links": links,
                "prev": links[current_index - 1] if current_index > 0 else None,
                "next": links[current_index + 1] if 0 <= current_index < len(links) - 1 else None,
                "related": related,
            }
        )
    return payload


def upsert_body_class(text: str, page_type: str) -> str:
    page_class = f"page-{page_type}"

    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        class_match = re.search(r'class="([^"]*)"', attrs)
        if class_match:
            classes = [c for c in class_match.group(1).split() if c]
            if page_class not in classes:
                classes.append(page_class)
            attrs = attrs.replace(class_match.group(0), f'class="{" ".join(classes)}"')
        else:
            attrs = f'{attrs} class="{page_class}"'
        return f"<body{attrs}>"

    return re.sub(r"<body([^>]*)>", repl, text, count=1, flags=re.IGNORECASE)


def add_skip_link(text: str) -> str:
    skip = '  <a class="skip-link" href="#main-content">Skip to content</a>\n'
    if 'class="skip-link"' in text:
        return text
    return re.sub(r'(<body[^>]*>\n)', r'\1' + skip, text, count=1, flags=re.IGNORECASE)


def update_main(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        if 'id="main-content"' not in attrs:
            attrs = f'{attrs} id="main-content" tabindex="-1"'
        return f"<main{attrs}>"

    return re.sub(r"<main([^>]*)>", repl, text, count=1, flags=re.IGNORECASE)


def upsert_head_bits(text: str, rel_path: Path, payload: dict) -> str:
    theme_tag = '  <meta name="theme-color" content="#2255d8">\n'
    if 'name="theme-color"' not in text:
        text = re.sub(r'(<link rel="stylesheet"[^>]+>\n)', theme_tag + r'\1', text, count=1, flags=re.IGNORECASE)

    script_src = '../' * (len(rel_path.parts) - 1) + 'js/app.js'
    app_tag = f'  <script id="{APP_MARKER}" src="{script_src}" defer></script>\n'
    data_blob = (
        PAGE_DATA_START
        + '  window.__STUDYHUB_PAGE = '
        + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        + ';\n'
        + PAGE_DATA_END
    )

    text = re.sub(r'\s*<script id="studyhub-page-data">.*?</script>\n?', '\n', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(rf'\s*<script id="{APP_MARKER}"[^>]*></script>\n?', '\n', text, flags=re.IGNORECASE | re.DOTALL)
    return re.sub(r'</head>', data_blob + app_tag + '</head>', text, count=1, flags=re.IGNORECASE)


def main() -> None:
    section_catalog = build_section_catalog()
    for abs_path in HTML_FILES:
        rel_path = abs_path.relative_to(ROOT)
        page_type = compute_page_type(rel_path)
        if page_type is None:
            continue
        text = read_text(abs_path)
        payload = page_payload(rel_path, page_type, section_catalog)
        text = upsert_body_class(text, page_type)
        text = add_skip_link(text)
        text = update_main(text)
        text = upsert_head_bits(text, rel_path, payload)
        write_text(abs_path, text)


if __name__ == "__main__":
    main()
