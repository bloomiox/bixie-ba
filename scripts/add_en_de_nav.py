#!/usr/bin/env python3
"""Add Careers/Karriere + AI Services/KI-Services links to en/de legacy navs."""
import os

ROOT = "/root/bixie-site"
# Only walk en/ and de/ dirs
TARGETS = [os.path.join(ROOT, "en"), os.path.join(ROOT, "de")]
EXCLUDE_DIRS = {".git"}

REPLACEMENTS = [
    # EN: Careers after "O nama" (desktop + mobile plain)
    ('<a href="/en/about">O nama</a>',
     '<a href="/en/about">O nama</a><a href="/en/careers">Careers</a>'),
    # EN: AI Services in AI dropdown/mobile
    ('<a href="/en/services/ai-agents">AI Agenti i Automatizacija</a>',
     '<a href="/en/services/ai-agents">AI Agenti i Automatizacija</a><a href="/en/services/ai-services">AI Services</a>'),
    # EN: footer Usluge short link with <br>
    ('<a href="/en/services/ai-agents">AI Agenti</a><br>',
     '<a href="/en/services/ai-agents">AI Agenti</a><br><a href="/en/services/ai-services">AI Services</a><br>'),
    # EN: Usluge dropdown short link
    ('<a href="/en/services/ai-agents">AI Agenti</a>',
     '<a href="/en/services/ai-agents">AI Agenti</a><a href="/en/services/ai-services">AI Services</a>'),

    # DE: Karriere after "O nama"
    ('<a href="/de/about">O nama</a>',
     '<a href="/de/about">O nama</a><a href="/de/karriere">Karriere</a>'),
    # DE: KI-Services in AI dropdown/mobile
    ('<a href="/de/services/ai-agents">AI Agenti i Automatizacija</a>',
     '<a href="/de/services/ai-agents">AI Agenti i Automatizacija</a><a href="/de/services/ki-services">KI-Services</a>'),
    # DE: footer Usluge short link with <br>
    ('<a href="/de/services/ai-agents">AI Agenti</a><br>',
     '<a href="/de/services/ai-agents">AI Agenti</a><br><a href="/de/services/ki-services">KI-Services</a><br>'),
    # DE: Usluge dropdown short link
    ('<a href="/de/services/ai-agents">AI Agenti</a>',
     '<a href="/de/services/ai-agents">AI Agenti</a><a href="/de/services/ki-services">KI-Services</a>'),
]

def iter_html():
    for base in TARGETS:
        for dirpath, dirnames, filenames in os.walk(base):
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
    total += new.count('href="/en/careers"') + new.count('href="/de/karriere"') \
           + new.count('href="/en/services/ai-services"') + new.count('href="/de/services/ki-services"')

print(f"Files changed: {len(changed)}")
for p in changed:
    print("  ", p)
print(f"Total new links: {total}")
