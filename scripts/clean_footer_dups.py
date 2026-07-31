#!/usr/bin/env python3
"""Clean duplicated footer links on legacy pages (pre-existing artifacts + script additions)."""
import os, re

ROOT = "/root/bixie-site"
EXCLUDE_DIRS = {".git"}

def iter_html():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)

# 1) Generic: collapse immediately repeated identical "<a ...>X</a><br>" sequences
REPEAT_RE = re.compile(r'(<a href="[^"]+">[^<]*</a><br>)\1')

# 2) Collapse duplicated "Blog O nama Karijera" blocks (bs/en/de)
BLOCK_REPLACEMENTS = [
    (r'(<a href="/blog">Blog</a><br><a href="/about">O nama</a><a href="/karijera">Karijera</a><br>)\1', r'\1'),
    (r'(<a href="/en/blog">Blog</a><br><a href="/en/about">O nama</a><a href="/en/careers">Careers</a><br>)\1', r'\1'),
    (r'(<a href="/de/blog">Blog</a><br><a href="/de/about">O nama</a><a href="/de/karriere">Karriere</a><br>)\1', r'\1'),
]

# 3) Remove leftover "Karijera -> Blog -> Kontakt" middle Blog (bs/en/de)
TAIL_REPLACEMENTS = [
    ('Karijera</a><br><a href="/blog">Blog</a><br><a href="/contact">Kontakt</a>', 'Karijera</a><br><a href="/contact">Kontakt</a>'),
    ('Careers</a><br><a href="/en/blog">Blog</a><br><a href="/en/contact">Kontakt</a>', 'Careers</a><br><a href="/en/contact">Kontakt</a>'),
    ('Karriere</a><br><a href="/de/blog">Blog</a><br><a href="/de/contact">Kontakt</a>', 'Karriere</a><br><a href="/de/contact">Kontakt</a>'),
]

# 4) Trailing Privacy Policy duplicate (last one lacks <br>)
PRIVACY_REPLACEMENTS = [
    ('<a href="/privacy">Privacy Policy</a><br><a href="/privacy">Privacy Policy</a>', '<a href="/privacy">Privacy Policy</a>'),
    ('<a href="/en/privacy">Privacy Policy</a><br><a href="/en/privacy">Privacy Policy</a>', '<a href="/en/privacy">Privacy Policy</a>'),
    ('<a href="/de/privacy">Privacy Policy</a><br><a href="/de/privacy">Privacy Policy</a>', '<a href="/de/privacy">Privacy Policy</a>'),
]

# 5) Interleaved RPA/Provajderi duplicates in Usluge column (bs/en/de)
RPA_REPLACEMENTS = [
    ('<a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a><br><a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a>',
     '<a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a>'),
    ('<a href="/en/services/rpa">RPA i Automatizacija</a><br><a href="/en/ai-providers">AI Provajderi i Licence</a><br><a href="/en/services/rpa">RPA i Automatizacija</a><br><a href="/en/ai-providers">AI Provajderi i Licence</a>',
     '<a href="/en/services/rpa">RPA i Automatizacija</a><br><a href="/en/ai-providers">AI Provajderi i Licence</a>'),
    ('<a href="/de/services/rpa">RPA i Automatizacija</a><br><a href="/de/ai-providers">AI Provajderi i Licence</a><br><a href="/de/services/rpa">RPA i Automatizacija</a><br><a href="/de/ai-providers">AI Provajderi i Licence</a>',
     '<a href="/de/services/rpa">RPA i Automatizacija</a><br><a href="/de/ai-providers">AI Provajderi i Licence</a>'),
]

changed = []
for path in iter_html():
    with open(path, encoding="utf-8") as f:
        content = f.read()
    new = content
    # collapse immediate repeats until stable (max 5 passes)
    for _ in range(5):
        prev = new
        new = REPEAT_RE.sub(r'\1', new)
        if new == prev:
            break
    for pat, repl in BLOCK_REPLACEMENTS:
        new = re.sub(pat, repl, new)
    for old, repl in TAIL_REPLACEMENTS:
        new = new.replace(old, repl)
    for old, repl in PRIVACY_REPLACEMENTS:
        new = new.replace(old, repl)
    for old, repl in RPA_REPLACEMENTS:
        new = new.replace(old, repl)
    if new != content:
        changed.append(path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)

print(f"Files cleaned: {len(changed)}")
