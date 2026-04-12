#!/usr/bin/env python3
"""Add JSON-LD structured data to ja/ and zh/ article pages missing it"""
import os, re

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SITE_BASE = "https://criel2019.github.io/studyhub"

LANG_LABELS = {
    "ja": {"pub": "StudyHub", "free": True, "level": "中学校, 高校"},
    "zh": {"pub": "StudyHub", "free": True, "level": "初中, 高中"}
}

def extract_meta(content, name):
    m = re.search(rf'<meta name="{name}" content="([^"]+)"', content)
    return m.group(1).replace('"', '\\"') if m else ""

def extract_title(content):
    m = re.search(r'<title>([^<]+)</title>', content)
    return m.group(1).replace('"', '\\"') if m else ""

def extract_canonical(content):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    return m.group(1) if m else ""

def extract_og_type(content):
    m = re.search(r'property="og:type" content="([^"]+)"', content)
    return m.group(1) if m else "article"

def get_section(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if len(parts) >= 2:
        return parts[1]  # math, japanese, science, etc.
    return ""

def get_teaches(section, title):
    """Extract main topic from title or section"""
    if section == "math": return "Mathematics"
    if section in ("japanese", "korean", "chinese"): return "Language Arts"
    if section == "science": return "Science"
    if section == "english": return "English"
    return title[:40] if title else "Study"

count = 0
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in {'.git', '.codex-audit', 'tools', 'images'} and not d.startswith('.')]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        rel_path = os.path.relpath(fpath, BASE)

        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Only process files missing JSON-LD
        if 'application/ld+json' in content:
            continue

        # Skip noindex and utility files
        if 'content="noindex"' in content or 'google-site-verification' in fpath or '404.html' in fpath:
            continue

        parts = rel_path.replace("\\", "/").split("/")
        lang = parts[0] if parts else "en"
        if lang not in ("ja", "zh"):
            continue

        title = extract_title(content)
        description = extract_meta(content, 'description')
        canonical = extract_canonical(content)
        og_type = extract_og_type(content)
        section = get_section(rel_path)
        teaches = get_teaches(section, title)

        lang_map = {"ja": "ja", "zh": "zh-Hans"}
        lang_code = lang_map.get(lang, lang)

        if og_type == "article":
            jsonld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{description}",
    "url": "{canonical}",
    "inLanguage": "{lang_code}",
    "publisher": {{"@type": "Organization", "name": "StudyHub", "url": "{SITE_BASE}/"}},
    "educationalLevel": "{LANG_LABELS[lang]["level"]}",
    "teaches": "{teaches}",
    "learningResourceType": "Study Guide",
    "isAccessibleForFree": true
  }}
  </script>'''
        else:
            jsonld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "headline": "{title}",
    "description": "{description}",
    "url": "{canonical}",
    "inLanguage": "{lang_code}",
    "publisher": {{"@type": "Organization", "name": "StudyHub", "url": "{SITE_BASE}/"}},
    "isAccessibleForFree": true
  }}
  </script>'''

        # Insert before theme-color meta
        theme_color = '  <meta name="theme-color"'
        if theme_color in content:
            content = content.replace(theme_color, jsonld + '\n  <meta name="theme-color"', 1)
        else:
            # Insert before style link
            style_link = '<link rel="stylesheet"'
            content = content.replace(style_link, jsonld + '\n  ' + style_link, 1)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"JSON-LD added to {count} files.")
