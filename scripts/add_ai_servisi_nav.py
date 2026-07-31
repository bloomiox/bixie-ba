#!/usr/bin/env python3
"""Add 'AI Servisi' links to AI dropdown/mobile menus + Usluge dropdowns + footers (bs pages)."""
import os

ROOT = "/root/bixie-site"
EXCLUDE_DIRS = {"en", "de", ".git"}

# Ordered: longer/more specific first where overlap exists
REPLACEMENTS = [
    # 1) Tailwind desktop AI dropdown (uses '&' label)
    ('<a href="/services/ai-agents" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Agenti & Automatizacija</a>',
     '<a href="/services/ai-agents" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Agenti & Automatizacija</a><a href="/services/ai-servisi" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-[#00736a]/10 transition-colors">AI Servisi — kompletna implementacija</a>'),
    # 2) Tailwind mobile AI menu
    ('<a href="/services/ai-agents" class="block py-2 text-sm text-gray-400 hover:text-white">AI Agenti i Automatizacija</a>',
     '<a href="/services/ai-agents" class="block py-2 text-sm text-gray-400 hover:text-white">AI Agenti i Automatizacija</a><a href="/services/ai-servisi" class="block py-2 text-sm text-gray-400 hover:text-white">AI Servisi — kompletna implementacija</a>'),
    # 3) Legacy desktop AI dropdown + legacy mobile AI menu (plain label)
    ('<a href="/services/ai-agents">AI Agenti i Automatizacija</a>',
     '<a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-servisi">AI Servisi</a>'),
    # 4) Footer Usluge column (short label followed by <br>)
    ('<a href="/services/ai-agents">AI Agenti</a><br>',
     '<a href="/services/ai-agents">AI Agenti</a><br><a href="/services/ai-servisi">AI Servisi</a><br>'),
    # 5) Usluge dropdown (short label, no <br>)
    ('<a href="/services/ai-agents">AI Agenti</a>',
     '<a href="/services/ai-agents">AI Agenti</a><a href="/services/ai-servisi">AI Servisi</a>'),
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
    total += new.count('href="/services/ai-servisi"')

print(f"Files changed: {len(changed)}")
for p in changed:
    print("  ", p)
print(f"Total AI Servisi links: {total}")
