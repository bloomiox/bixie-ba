#!/usr/bin/env python3
"""Add 'Besplatna AI procjena' (/ai-audit) link to AI dropdowns + mobile menus (bs pages)."""
import os

ROOT = "/root/bixie-site"
EXCLUDE_DIRS = {"en", "de", ".git", "ai-audit"}

REPLACEMENTS = [
    # Tailwind desktop AI dropdown (pair: AI Agenti & + AI Servisi)
    ('<a href="/services/ai-agents" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Agenti & Automatizacija</a><a href="/services/ai-servisi" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Servisi — kompletna implementacija</a>',
     '<a href="/services/ai-agents" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Agenti & Automatizacija</a><a href="/services/ai-servisi" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Servisi — kompletna implementacija</a><a href="/ai-audit" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">Besplatna AI procjena</a>'),
    # Tailwind mobile AI menu (pair)
    ('<a href="/services/ai-agents" class="block py-2 text-sm text-gray-400 hover:text-white">AI Agenti i Automatizacija</a><a href="/services/ai-servisi" class="block py-2 text-sm text-gray-400 hover:text-white">AI Servisi — kompletna implementacija</a>',
     '<a href="/services/ai-agents" class="block py-2 text-sm text-gray-400 hover:text-white">AI Agenti i Automatizacija</a><a href="/services/ai-servisi" class="block py-2 text-sm text-gray-400 hover:text-white">AI Servisi — kompletna implementacija</a><a href="/ai-audit" class="block py-2 text-sm text-gray-400 hover:text-white">Besplatna AI procjena</a>'),
    # Legacy desktop AI dropdown + legacy mobile (pair)
    ('<a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-servisi">AI Servisi</a>',
     '<a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-servisi">AI Servisi</a><a href="/ai-audit">Besplatna AI procjena</a>'),
]

def iter_html():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)

changed, total = [], 0
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
    total += new.count('href="/ai-audit"')

print(f"Files changed: {len(changed)}")
print(f"Total /ai-audit links: {total}")
