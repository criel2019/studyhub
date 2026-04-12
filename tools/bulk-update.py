#!/usr/bin/env python3
"""Bulk HTML updater: adds og:image, favicon, fixes footer color"""
import os, re

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SKIP_DIRS = {'.git', '.codex-audit', 'tools', 'images'}

OG_BASE = "https://criel2019.github.io/studyhub/images/og"
SITE_BASE = "https://criel2019.github.io/studyhub"

stats = {"og_added": 0, "favicon_added": 0, "color_fixed": 0, "skipped": 0}

def get_lang_code(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if parts[0] == "ko":
        return "ko"
    elif parts[0] == "en":
        return "en"
    elif parts[0] == "ja":
        return "ja"
    elif parts[0] == "zh":
        return "zh"
    else:
        return "global"

def get_depth(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    return len(parts) - 1

def process_file(fpath, rel_path):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Skip noindex pages
    if 'content="noindex"' in content or "content='noindex'" in content:
        stats["skipped"] += 1
        return

    # Skip Google verification file
    if 'google-site-verification' in fpath or 'google8c26ce59e7acdd58' in fpath:
        stats["skipped"] += 1
        return

    lang_code = get_lang_code(rel_path)
    depth = get_depth(rel_path)
    prefix = "../" * depth

    # 1. Add og:image after og:site_name (if not already present)
    if 'property="og:image"' not in content:
        og_site_name = '  <meta property="og:site_name" content="StudyHub">'
        if og_site_name in content:
            og_image_url = f"{OG_BASE}/{lang_code}.svg"
            og_insert = (
                f'  <meta property="og:image" content="{og_image_url}">\n'
                f'  <meta property="og:image:width" content="1200">\n'
                f'  <meta property="og:image:height" content="630">'
            )
            content = content.replace(
                og_site_name,
                og_site_name + "\n" + og_insert
            )
            stats["og_added"] += 1

    # 2. Add favicon link after charset meta (if not already present)
    if 'rel="icon"' not in content:
        charset_line = '  <meta charset="UTF-8">'
        if charset_line in content:
            favicon_href = f"{prefix}favicon.svg"
            favicon_link = f'  <link rel="icon" href="{favicon_href}" type="image/svg+xml">'
            content = content.replace(
                charset_line,
                charset_line + "\n" + favicon_link
            )
            stats["favicon_added"] += 1

    # 3. Fix footer disclaimer color (#64748b on dark footer bg)
    # Only fix the footer paragraph pattern (not the hero subtitle)
    footer_color_pattern = 'style="margin-top:0.5rem;font-size:0.8rem;color:#64748b;"'
    footer_color_fixed = 'style="margin-top:0.5rem;font-size:0.8rem;color:rgba(200,215,240,0.62);"'
    if footer_color_pattern in content:
        content = content.replace(footer_color_pattern, footer_color_fixed)
        stats["color_fixed"] += 1

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

# Walk all HTML files
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        rel_path = os.path.relpath(fpath, BASE)
        process_file(fpath, rel_path)

print(f"og:image added:   {stats['og_added']}")
print(f"favicon added:    {stats['favicon_added']}")
print(f"color fixed:      {stats['color_fixed']}")
print(f"skipped:          {stats['skipped']}")
print("Done.")
