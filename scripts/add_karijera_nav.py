#!/usr/bin/env python3
"""Add Karijera nav/footer links after every 'O nama' link across bixie.ba (bs) pages."""
import os, re, sys

ROOT = "/root/bixie-site"
EXCLUDE_DIRS = {"en", "de", "karijera", ".git"}

# (exact O nama link, replacement that appends matching Karijera link)
REPLACEMENTS = [
    # legacy plain (desktop+mobile nav, legacy pages)
    ('<a href="/about">O nama</a>',
     '<a href="/about">O nama</a><a href="/karijera">Karijera</a>'),
    # Tailwind desktop nav
    ('<a href="/about" class="text-gray-400 hover:text-white text-sm font-medium transition-colors">O nama</a>',
     '<a href="/about" class="text-gray-400 hover:text-white text-sm font-medium transition-colors">O nama</a><a href="/karijera" class="text-gray-400 hover:text-white text-sm font-medium transition-colors">Karijera</a>'),
    # footer inline-style (about-page footer)
    ('<a href="/about" style="display:block;font-size:14px;color:#6b7280;margin-bottom:8px;text-decoration:none">O nama</a>',
     '<a href="/about" style="display:block;font-size:14px;color:#6b7280;margin-bottom:8px;text-decoration:none">O nama</a><a href="/karijera" style="display:block;font-size:14px;color:#6b7280;margin-bottom:8px;text-decoration:none">Karijera</a>'),
    # Tailwind mobile nav
    ('<a href="/about" class="block py-2 text-sm text-gray-400 hover:text-white">O nama</a>',
     '<a href="/about" class="block py-2 text-sm text-gray-400 hover:text-white">O nama</a><a href="/karijera" class="block py-2 text-sm text-gray-400 hover:text-white">Karijera</a>'),
    # Tailwind desktop nav ACTIVE (about page) -> new link gray
    ('<a href="/about" class="text-white text-sm font-medium transition-colors">O nama</a>',
     '<a href="/about" class="text-white text-sm font-medium transition-colors">O nama</a><a href="/karijera" class="text-gray-400 hover:text-white text-sm font-medium transition-colors">Karijera</a>'),
    # ai-za-firme variant
    ('<a href="/about" class="text-gray-400 text-sm">O nama</a>',
     '<a href="/about" class="text-gray-400 text-sm">O nama</a><a href="/karijera" class="text-gray-400 text-sm">Karijera</a>'),
    # index.html mobile nav
    ('<a href="/about" class="block text-gray-400 text-sm pl-3">→ O nama</a>',
     '<a href="/about" class="block text-gray-400 text-sm pl-3">→ O nama</a><a href="/karijera" class="block text-gray-400 text-sm pl-3">→ Karijera</a>'),
    # Tailwind mobile nav ACTIVE (about page)
    ('<a href="/about" class="block py-2 text-sm text-white font-medium">O nama</a>',
     '<a href="/about" class="block py-2 text-sm text-white font-medium">O nama</a><a href="/karijera" class="block py-2 text-sm text-gray-400 hover:text-white">Karijera</a>'),
    # index.html footer
    ('<a href="/about" class="block hover:text-white transition-colors">O nama</a>',
     '<a href="/about" class="block hover:text-white transition-colors">O nama</a><a href="/karijera" class="block hover:text-white transition-colors">Karijera</a>'),
]

def iter_html():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)

changed, total_links = [], 0
for path in iter_html():
    with open(path, encoding="utf-8") as f:
        content = f.read()
    new = content
    for old, repl in REPLACEMENTS:
        new = new.replace(old, repl)
    if new != content:
        changed.append(path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
    total_links += new.count('href="/karijera"')

print(f"Files changed: {len(changed)}")
for p in changed:
    print("  ", p)
print(f"Total Karijera links added: {total_links}")
