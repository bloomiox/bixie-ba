#!/usr/bin/env python3
"""Gradi HTML za blog post iz ŠABLONA AKTIVNOG SAJTA.

Zašto: stari convert_posts.py je zastaRio (vraća Tailwind Play CDN i briše schema
markup), pa se njime ne smiju regenerisati postojeći postovi. Ova skripta uzima
postojeći, deployani post kao šablon i u njega ubacuje novi sadržaj — isti izgled,
isti meta tagovi, isti JSON-LD.

Upotreba:
    python3 build_post.py                      # svi .md bez generisanog index.html
    python3 build_post.py slug1 slug2 ...      # samo navedeni slugovi
"""
import os
import re
import sys

SITE = "/root/bixie-site"
MD_DIR = "/root/bixie-blog-posts/posts"
TPL_REF = os.path.join(SITE, "blog/posts/ai-agenti-analiza-podataka/index.html")

OLD_SLUG = "ai-agenti-analiza-podataka"
OLD_TITLE_FULL = "AI agenti za analizu podataka: Od podataka do odluka — BIXIE"
OLD_TITLE = "AI agenti za analizu podataka: Od podataka do odluka"
OLD_DESC = ("Kako AI agenti transformišu analizu podataka — automatsko prikupljanje, "
            "čišćenje, vizualizacija i izvještavanje.")
OLD_TAG = "AI Agenti"
OLD_META = "14. Juni 2026 · BIXIE Team · 3 min čitanja"

MJESECI = {1: "Januar", 2: "Februar", 3: "Mart", 4: "April", 5: "Maj", 6: "Juni",
           7: "Juli", 8: "Avgust", 9: "Septembar", 10: "Oktobar", 11: "Novembar",
           12: "Decembar"}


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("nema front matter")
    meta, body = m.group(1), m.group(2)
    fm = {}
    for line in meta.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, body.strip()


def inline(t):
    t = (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def md_to_html(md):
    out, in_list = [], False
    for raw in md.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        if line.startswith("#### "):
            head = 'h4 class="text-2xl font-bold text-white mt-10 mb-4"'
        elif line.startswith("### "):
            head = 'h3 class="text-2xl font-bold text-white mt-10 mb-4"'
        elif line.startswith("## "):
            head = 'h2 class="text-3xl font-bold text-white mt-10 mb-4"'
        elif line.startswith("# "):
            out.append(f'<h2 class="text-3xl font-bold text-white mt-10 mb-4">'
                       f'{inline(line[2:].strip())}</h2>')
            continue
        else:
            head = None

        if head:
            if in_list:
                out.append("</ul>")
                in_list = False
            txt = inline(re.sub(r"^#+ ", "", line))
            out.append(f"<{head}>{txt}</{head}>")
        elif line.startswith("- "):
            if not in_list:
                out.append('<ul class="list-disc pl-6 mb-4 text-gray-300">')
                in_list = True
            out.append(f"<li class=\"mb-2\">{inline(line[2:].strip())}</li>")
        elif line.startswith("> "):
            out.append(f'<p class="text-gray-300 mb-4 italic border-l-2 border-[#00736a] '
                       f'pl-4">{inline(line[2:].strip())}</p>')
        elif re.match(r"^\d+\.\s", line):
            if not in_list:
                out.append('<ul class="list-disc pl-6 mb-4 text-gray-300">')
                in_list = True
            txt = re.sub(r"^\d+\.\s", "", line)
            out.append(f'<li class="mb-2">{inline(txt)}</li>')
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f'<p class="text-gray-300 mb-4">{inline(line.strip())}</p>')
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def build(slug, tpl):
    with open(os.path.join(MD_DIR, slug + ".md"), encoding="utf-8") as f:
        fm, body_md = front_matter(f.read())
    title = fm["title"]
    desc = fm.get("description", "")
    cat = fm.get("category", "AI Agenti")
    y, m, d = (int(x) for x in (fm.get("date") or "2026-01-01").split("-"))
    date_display = f"{d}. {MJESECI[m]} {y}"
    rt = max(2, round(len(body_md.split()) / 200))

    h = tpl.replace(OLD_SLUG, slug)
    h = h.replace(OLD_TITLE_FULL, f"{title} — BIXIE")
    h = h.replace(OLD_TITLE, title)
    h = h.replace(OLD_DESC, desc.replace('"', "'"))
    h = h.replace(f'<span class="tag">{OLD_TAG}</span>', f'<span class="tag">{cat}</span>')
    h = h.replace(OLD_META, f"{date_display} · BIXIE Team · {rt} min čitanja")
    # Bez EN/DE prijevoda za novi post — ne ostavljati hreflang na nepostojeće stranice
    h = re.sub(r'<link rel="alternate" hreflang="(en|de)" href="[^"]*">\n?', "", h)
    # datePublished / dateModified u JSON-LD (AIO: datum objave je često citiran podatak)
    h = h.replace('  "url": "https://bixie.ba/blog/posts/%s",\n' % slug,
                  '  "url": "https://bixie.ba/blog/posts/%s",\n'
                  '  "datePublished": "%s",\n'
                  '  "dateModified": "%s",\n' % (slug, fm.get("date"), fm.get("date")))

    head, rest = h.split('<div class="blog-content">\n', 1)
    _, tail = rest.split("\n</div>\n</section>", 1)
    html_out = head + '<div class="blog-content">\n' + md_to_html(body_md) + "\n</div>\n</section>" + tail

    out_dir = os.path.join(SITE, "blog/posts", slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"✓ {slug} ({rt} min, {len(html_out)} B)")


def main():
    with open(TPL_REF, encoding="utf-8") as f:
        tpl = f.read()
    if sys.argv[1:]:
        slugs = sys.argv[1:]
    else:
        slugs = [fn[:-3] for fn in sorted(os.listdir(MD_DIR)) if fn.endswith(".md")
                 and not os.path.exists(os.path.join(SITE, "blog/posts", fn[:-3], "index.html"))]
    for s in slugs:
        build(s, tpl)


if __name__ == "__main__":
    main()
