#!/usr/bin/env python3
"""Add missing og: tags to ja/ and zh/ article pages"""
import os, re

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OG_BASE = "https://criel2019.github.io/studyhub/images/og"

def extract_meta(content, name):
    m = re.search(rf'<meta name="{name}" content="([^"]+)"', content)
    return m.group(1) if m else ""

def extract_title(content):
    m = re.search(r'<title>([^<]+)</title>', content)
    return m.group(1) if m else ""

def extract_canonical(content):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    return m.group(1) if m else ""

def get_lang_code(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    return parts[0] if parts[0] in ('ko','en','ja','zh') else 'global'

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

        # Only process files missing og:title
        if 'property="og:title"' in content:
            continue
        # Skip noindex and verification
        if 'content="noindex"' in content or 'google-site-verification' in fpath:
            continue
        if '404.html' in fpath:
            continue

        title = extract_title(content)
        description = extract_meta(content, 'description')
        canonical = extract_canonical(content)
        lang_code = get_lang_code(rel_path)
        og_img = f"{OG_BASE}/{lang_code}.svg"

        og_block = (
            f'  <meta property="og:title" content="{title}">\n'
            f'  <meta property="og:description" content="{description}">\n'
            f'  <meta property="og:type" content="article">\n'
            f'  <meta property="og:url" content="{canonical}">\n'
            f'  <meta property="og:site_name" content="StudyHub">\n'
            f'  <meta property="og:image" content="{og_img}">\n'
            f'  <meta property="og:image:width" content="1200">\n'
            f'  <meta property="og:image:height" content="630">'
        )

        # Insert before canonical link (or before theme-color meta)
        if '<link rel="canonical"' in content:
            content = content.replace(
                '<link rel="canonical"',
                og_block + '\n  <link rel="canonical"',
                1
            )
        else:
            # Fallback: insert before theme-color
            content = content.replace(
                '  <meta name="theme-color"',
                og_block + '\n  <meta name="theme-color"',
                1
            )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"og: tags added to {count} files.")
