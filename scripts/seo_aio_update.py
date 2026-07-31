#!/usr/bin/env python3
"""SEO + AIO (GEO) enhancement: schema markup, meta descriptions, canonicals, llms support."""
import os, re, json

ROOT = "/root/bixie-site"

ORG = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "BIXIE",
    "url": "https://bixie.ba",
    "logo": "https://bixie.ba/og-image.png",
    "description": "CRM, AI Agenti i Digitalna Transformacija za firme u Bosni i Hercegovini. Registered partner Bitrix24, Zoho, Salesforce, HubSpot, Pipedrive.",
    "address": {"@type": "PostalAddress", "streetAddress": "Maglajska 1", "addressLocality": "Sarajevo", "addressCountry": "BA"},
    "contactPoint": {"@type": "ContactPoint", "telephone": "+387-33-922-622", "email": "hello@bixie.ba", "contactType": "sales"},
    "sameAs": ["https://www.linkedin.com/company/bixie"],
}

HOME_FAQ = [
    ("Koje CRM platforme podržavate?",
     "Podržavamo Bitrix24, Zoho CRM, Salesforce, HubSpot, Pipedrive, Microsoft Dynamics, SugarCRM i Twenty CRM. Kao registrovani partner za većinu platformi, nudimo implementaciju, migraciju i optimizaciju."),
    ("Kako funkcioniše proces implementacije?",
     "Proces počinje besplatnim konsultacijama gdje analiziramo vaše potrebe. Nakon toga slijedi plan implementacije, konfiguracija sistema, migracija podataka, obuka korisnika i post-implementacijska podrška."),
    ("Da li nudite AI agente po mjeri?",
     "Da. Razvijamo custom AI agente koji se integriraju sa vašim postojećim sistemima — CRM, ERP, DMS, web i druge platforme. Koristimo OpenClaw platformu i podržavamo ChatGPT, Claude, Gemini i druge modele."),
    ("Koje licence možete nabaviti?",
     "Nabavljamo licence za ChatGPT Team/Enterprise, Google Workspace, Microsoft 365, GitHub Copilot, Canva Pro/Enterprise, Bitrix24 i druge. Za obrazovne institucije nudimo akademske popuste."),
    ("Radite li sa klijentima izvan BiH?",
     "Da. Naši klijenti dolaze iz Švicarske, Njemačke, Austrije, SAD i regiona. Radimo remote-first pristupom sa jasnim miljokazima i redovnom komunikacijom."),
]

def ld_block(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n</script>'

def inject_before_head_end(html, block):
    return html.replace('</head>', block + '\n</head>', 1)

changed = []

# ---------- 1. Homepage: Organization + WebSite + FAQPage ----------
p = os.path.join(ROOT, "index.html")
html = open(p, encoding="utf-8").read()
if "application/ld+json" not in html:
    graph = [
        ORG,
        {"@type": "WebSite", "name": "BIXIE", "url": "https://bixie.ba",
         "potentialAction": {"@type": "SearchAction", "target": "https://bixie.ba/search?q={search_term_string}", "query-input": "required name=search_term_string"}},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in HOME_FAQ
        ]},
    ]
    block = ld_block({"@context": "https://schema.org", "@graph": graph})
    html = inject_before_head_end(html, block)
    open(p, "w", encoding="utf-8").write(html)
    changed.append(p)

# ---------- 2. Careers: JobPosting ItemList ----------
p = os.path.join(ROOT, "karijera/index.html")
html = open(p, encoding="utf-8").read()
if "JobPosting" not in html:
    jobs = [
        ("Sales Development Representative (SDR)", "Sarajevo, BiH (remote)", "Prodaja", "AI-native prodaja: generisanje i kvalifikacija leadova uz AI alate. Full-time."),
        ("Account Executive (AE)", "Sarajevo, BiH (remote)", "Prodaja", "AI-native prodaja: vođenje prodajnih procesa od prvog sastanka do potpisa. Full-time."),
        ("AI Automation Engineer", "Sarajevo, BiH (remote/hybrid)", "Inženjering", "Razvoj custom AI agenata, RPA automatizacija i integracija s CRM/ERP sistemima. 2 pozicije. Full-time."),
        ("AI Consultant", "Sarajevo, BiH (remote/hybrid)", "Konsalting", "Analiza poslovnih procesa i prijedlozi AI rješenja s ROI kalkulacijom. 3 pozicije. Full-time."),
    ]
    items = []
    for title, loc, dept, desc in jobs:
        items.append({
            "@type": "JobPosting",
            "title": title,
            "description": desc,
            "datePosted": "2026-07-31",
            "employmentType": "FULL_TIME",
            "hiringOrganization": {"@type": "Organization", "name": "BIXIE", "sameAs": "https://bixie.ba"},
            "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Sarajevo", "addressCountry": "BA"}},
            "directApply": True,
        })
    block = ld_block({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": it} for i, it in enumerate(items)
    ]})
    html = inject_before_head_end(html, block)
    open(p, "w", encoding="utf-8").write(html)
    changed.append(p)

# ---------- 3. Service pages: Service schema ----------
SERVICES = {
    "services/ai-servisi/index.html": ("AI Servisi — kompletna AI implementacija", "AI audit i strategija, forward deployment (embedded AI inženjer), data readiness, RAG knowledge AI, managed AI i AI governance (EU AI Act)."),
    "services/ai-agents/index.html": ("AI Agenti i Automatizacija", "Razvoj custom AI agenata za customer support, prodaju i interne procese; RPA automatizacija; AI licence."),
    "services/crm/index.html": ("CRM implementacija", "Bitrix24, Zoho, Salesforce, HubSpot, Pipedrive, Twenty — implementacija, migracija i optimizacija CRM sistema."),
    "services/rpa/index.html": ("RPA i Automatizacija", "Robotic Process Automation za repetitivne zadatke: unos podataka, fakturisanje, izvještavanje."),
    "services/digital-transformation/index.html": ("Digitalna Transformacija", "Digitalni ured, privatni/hibridni cloud, optimizacija procesa, AI integracija u ERP/DMS."),
    "ai-providers/index.html": ("AI Licence i Provajderi", "Legalna nabavka AI licenci za firme i institucije — ChatGPT, Gemini, Claude, DeepSeek; domaća faktura sa PDV-om."),
}
for rel, (name, desc) in SERVICES.items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        continue
    html = open(p, encoding="utf-8").read()
    if "application/ld+json" not in html:
        svc = {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": name,
            "description": desc,
            "provider": ORG,
            "areaServed": "BA",
            "url": f"https://bixie.ba/{rel.replace('/index.html', '')}",
        }
        block = ld_block(svc)
        html = inject_before_head_end(html, block)
        open(p, "w", encoding="utf-8").write(html)
        changed.append(p)

# ---------- 4. ai-audit: Organization ----------
p = os.path.join(ROOT, "ai-audit/index.html")
html = open(p, encoding="utf-8").read()
if "application/ld+json" not in html:
    block = ld_block(ORG)
    html = inject_before_head_end(html, block)
    open(p, "w", encoding="utf-8").write(html)
    changed.append(p)

# ---------- 5. Blog posts: meta description + canonical + BlogPosting ----------
blog_dir = os.path.join(ROOT, "blog/posts")
date_re = re.compile(r'(20\d{2})[.\-/](0[1-9]|1[0-2])[.\-/](0[1-9]|[12]\d|3[01])')
for dirpath, dirnames, filenames in os.walk(blog_dir):
    for fn in filenames:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        html = open(p, encoding="utf-8").read()
        orig = html

        title_m = re.search(r'<title>(.*?)</title>', html, re.S)
        desc_m = re.search(r'<meta name="description" content="([^"]*)"', html)
        og_desc_m = re.search(r'<meta property="og:description" content="([^"]*)"', html)
        og_url_m = re.search(r'<meta property="og:url" content="([^"]*)"', html)
        og_image_m = re.search(r'<meta property="og:image" content="([^"]*)"', html)

        if not desc_m and og_desc_m:
            html = html.replace('<meta property="og:description"', '<meta name="description" content="%s">\n<meta property="og:description"' % og_desc_m.group(1), 1)

        if og_url_m and 'rel="canonical"' not in html:
            html = html.replace('</head>', f'<link rel="canonical" href="{og_url_m.group(1)}">\n</head>', 1)

        if "BlogPosting" not in html:
            headline = (title_m.group(1) if title_m else "BIXIE Blog").strip()
            bp_desc = ""
            if desc_m:
                bp_desc = desc_m.group(1)
            elif og_desc_m:
                bp_desc = og_desc_m.group(1)
            bp = {
                "@context": "https://schema.org",
                "@type": "BlogPosting",
                "headline": headline,
                "description": bp_desc,
                "url": og_url_m.group(1) if og_url_m else "https://bixie.ba/blog",
                "image": og_image_m.group(1) if og_image_m else "https://bixie.ba/og-image.png",
                "author": {"@type": "Organization", "name": "BIXIE", "url": "https://bixie.ba"},
                "publisher": {"@type": "Organization", "name": "BIXIE", "url": "https://bixie.ba", "logo": {"@type": "ImageObject", "url": "https://bixie.ba/og-image.png"}},
                "inLanguage": "bs",
            }
            dm = date_re.search(html)
            if dm:
                bp["datePublished"] = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)}"
            block = ld_block(bp)
            html = inject_before_head_end(html, block)

        if html != orig:
            open(p, "w", encoding="utf-8").write(html)
            changed.append(p)

print(f"Files updated: {len(changed)}")
