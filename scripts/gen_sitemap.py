#!/usr/bin/env python3
"""Generise sitemap.xml iz stvarnih fajlova u /root/bixie-site-vite.

Stara verzija je pisala u /root/bixie-site (zastarjela kopija) i imala rucnu listu od 9 postova,
pa je sitemap bio nepotpun. Ova verzija skenira direktorije.
"""
import os

ROOT = '/root/bixie-site-vite'
SITE = 'https://bixie.ba'

SKIP = {'blog', 'en', 'de', 'images', 'assets', 'downloads', 'functions', 'scripts',
        'design-tokens', 'src', 'node_modules', '.git'}


def pages(lang_dir=''):
    base = os.path.join(ROOT, lang_dir) if lang_dir else ROOT
    out = []
    for entry in sorted(os.listdir(base)):
        full = os.path.join(base, entry)
        if os.path.isdir(full) and entry not in SKIP and os.path.exists(os.path.join(full, 'index.html')):
            out.append(entry)
    return out


def posts():
    base = os.path.join(ROOT, 'blog/posts')
    return [d for d in sorted(os.listdir(base)) if os.path.exists(os.path.join(base, d, 'index.html'))]


def url(loc, priority, freq):
    return (f'  <url>\n    <loc>{SITE}/{loc}</loc>\n'
            f'    <priority>{priority}</priority>\n    <changefreq>{freq}</changefreq>\n  </url>\n')


def main():
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    sm += url('', 1.0, 'weekly')
    sm += url('blog', 0.8, 'weekly')
    for p in pages(''):
        sm += url(p, 0.8, 'monthly')
    for p in posts():
        sm += url(f'blog/posts/{p}', 0.7, 'monthly')
    for lang in ('en', 'de'):
        sm += url(lang, 0.6, 'monthly')
        for p in pages(lang):
            sm += url(f'{lang}/{p}', 0.6, 'monthly')
    sm += '</urlset>\n'
    out = os.path.join(ROOT, 'sitemap.xml')
    open(out, 'w', encoding='utf-8').write(sm)
    print(f'sitemap: {sm.count("<url>")} URL-ova -> {out}')


if __name__ == '__main__':
    main()
