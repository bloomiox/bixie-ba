#!/usr/bin/env python3
"""Generate industry landing pages and use case pages for bixie.ba"""
import os

SITE = '/root/bixie-site'

NAV_BS = '''<nav>
<div class="nav-inner">
<a href="/" class="logo"><img src="/images/logo/bixie-logo.png" alt="BIXIE" style="height:36px"></a>
<div class="nav-links">
<div class="dropdown"><a href="/services/crm">CRM</a><div class="dropdown-menu"><a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a></div></div>
<div class="dropdown"><a href="/services/ai-agents">AI</a><div class="dropdown-menu"><a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a><a href="/open-source-infra">Open Source Infrastruktura</a></div></div>
<div class="dropdown"><a href="/services">Usluge</a><div class="dropdown-menu"><a href="/services">Pregled svih usluga</a><a href="/services/crm">CRM Rjesenja</a><a href="/services/ai-agents">AI Agenti</a><a href="/services/rpa">RPA Automatizacija</a><a href="/open-source-infra">Open Source Infrastruktura</a><a href="/ai-providers">AI Licence</a><a href="/services/digital-transformation">Digitalna Transformacija</a></div></div>
<a href="/industries" style="color:#00736a">Industrije</a>
<a href="/ai-providers">AI Licence</a>
<a href="/open-source-infra">Open Source</a>
<a href="/blog">Blog</a>
<a href="/contact" class="nav-cta">Zatražite ponudu</a>
</div>
<button class="hamburger" onclick="toggleMobile()"><span></span><span></span><span></span></button>
</div>
<div id="mobileMenu" class="mobile-menu">
<div class="mobile-label">CRM</div>
<a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a>
<div class="mobile-label">AI</div>
<a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a><a href="/open-source-infra">Open Source Infrastruktura</a>
<div class="mobile-label">Usluge</div>
<a href="/services">Pregled svih usluga</a><a href="/services/crm">CRM Rjesenja</a><a href="/services/ai-agents">AI Agenti</a><a href="/services/rpa">RPA Automatizacija</a><a href="/open-source-infra">Open Source Infrastruktura</a><a href="/ai-providers">AI Licence</a><a href="/services/digital-transformation">Digitalna Transformacija</a>
<div class="mobile-label">Industrije</div>
<a href="/industries/finance">Bankarstvo i Finansije</a><a href="/industries/education">Obrazovanje</a><a href="/industries/manufacturing">Proizvodnja</a><a href="/industries/public-sector">Javne Ustanove</a>
<a href="/about">O nama</a>
<a href="/ai-providers">AI Licence</a><a href="/open-source-infra">Open Source</a><a href="/blog">Blog</a>
<a href="/contact" style="display:block;margin-top:10px;background:#00736a;color:#fff;padding:10px 16px;border-radius:6px;text-align:center;font-weight:450;font-size:0.9rem">Zatražite ponudu</a>
</div>
</nav>'''

FOOTER_BS = '''<footer>
<div class="footer-inner">
<div><a href="/" style="display:flex;align-items:center;gap:8px;text-decoration:none;font-size:16px;font-weight:510;color:#f0f2f4;margin-bottom:12px"><svg width="24" height="24" viewBox="0 0 28 28" fill="none"><rect width="28" height="28" rx="6" fill="#00736a"/><text x="14" y="19" text-anchor="middle" fill="#fff" font-family="Inter" font-weight="600" font-size="16">B</text></svg>BIXIE</a><p style="font-size:14px;color:#6b7280;line-height:1.6">CRM, AI Agenti i Digitalna Transformacija za vasu firmu.</p></div>
<div><h4>Usluge</h4><a href="/services">Pregled usluga</a><br><a href="/services/crm">CRM Rjesenja</a><br><a href="/services/ai-agents">AI Agenti</a><br><a href="/services/rpa">RPA i Automatizacija</a><br><a href="/open-source-infra">Open Source Infrastruktura</a><br><a href="/ai-providers">AI Provajderi i Licence</a><br><a href="/services/digital-transformation">Digitalna Transformacija</a></div>
<div><h4>Industrije</h4><a href="/industries/finance">Bankarstvo i Finansije</a><br><a href="/industries/education">Obrazovanje</a><br><a href="/industries/manufacturing">Proizvodnja</a><br><a href="/industries/public-sector">Javne Ustanove</a></div>
<div><h4>Kontakt</h4><p>hello@bixie.ba</p><p>033 922 622</p><p>Maglajska 1, 71000 Sarajevo</p></div>
</div>
<div class="footer-bottom">2026 BIXIE. All rights reserved.</div>
</footer>'''

def make_page(title, desc, h1, lead, sections, slug, lang='bs', industries_section=None, cta_text="Zakažite besplatne konsultacije"):
    url_prefix = '' if lang == 'bs' else '/en'
    nav = NAV_BS
    footer = FOOTER_BS
    
    if lang == 'en':
        nav = NAV_BS.replace('href="/industries"', 'href="/en/industries"')
        nav = nav.replace('href="/services/', 'href="/en/services/')
        nav = nav.replace('href="/open-source-infra"', 'href="/en/open-source-infra"')
        nav = nav.replace('href="/ai-providers"', 'href="/en/ai-providers"')
        nav = nav.replace('href="/about"', 'href="/en/about"')
        nav = nav.replace('href="/blog"', 'href="/en/blog"')
        nav = nav.replace('href="/contact"', 'href="/en/contact"')
        nav = nav.replace('Zatražite ponudu', 'Get a Quote')
        nav = nav.replace('Industrije', 'Industries')
        nav = nav.replace('Bankarstvo i Finansije', 'Banking & Finance')
        nav = nav.replace('Obrazovanje', 'Education')
        nav = nav.replace('Proizvodnja', 'Manufacturing')
        nav = nav.replace('Javne Ustanove', 'Public Sector')
        nav = nav.replace('Pregled svih usluga', 'All Services')
        nav = nav.replace('Pregled CRM usluga', 'CRM Services')
        nav = nav.replace('AI Agenti i Automatizacija', 'AI Agents & Automation')
        nav = nav.replace('AI Agenti', 'AI Agents')
        nav = nav.replace('RPA Automatizacija', 'RPA Automation')
        nav = nav.replace('Open Source Infrastruktura', 'Open Source Infrastructure')
        nav = nav.replace('AI Licence', 'AI Licenses')
        nav = nav.replace('Digitalna Transformacija', 'Digital Transformation')
        nav = nav.replace('AI Implementacija', 'AI Implementation')
        nav = nav.replace('Usluge', 'Services')
        nav = nav.replace('Industrije', 'Industries')
        nav = nav.replace('href="/industries/finance"', 'href="/en/industries/finance"')
        nav = nav.replace('href="/industries/education"', 'href="/en/industries/education"')
        nav = nav.replace('href="/industries/manufacturing"', 'href="/en/industries/manufacturing"')
        nav = nav.replace('href="/industries/public-sector"', 'href="/en/industries/public-sector"')
        
        footer = FOOTER_BS.replace('href="/industries/', 'href="/en/industries/')
        footer = footer.replace('Usluge', 'Services')
        footer = footer.replace('Industrije', 'Industries')
        footer = footer.replace('Pregled usluga', 'All Services')
        footer = footer.replace('Bankarstvo i Finansije', 'Banking & Finance')
        footer = footer.replace('Obrazovanje', 'Education')
        footer = footer.replace('Proizvodnja', 'Manufacturing')
        footer = footer.replace('Javne Ustanove', 'Public Sector')
        footer = footer.replace('CRM Rjesenja', 'CRM Solutions')
        footer = footer.replace('AI Agenti', 'AI Agents')
        footer = footer.replace('RPA i Automatizacija', 'RPA & Automation')
        footer = footer.replace('Open Source Infrastruktura', 'Open Source Infrastructure')
        footer = footer.replace('AI Provajderi i Licence', 'AI Providers & Licenses')
        footer = footer.replace('Digitalna Transformacija', 'Digital Transformation')
        footer = footer.replace('Kontakt', 'Contact')

    sections_html = '\n'.join(sections)
    industries_link = ''
    if industries_section:
        industries_link = f'''<div style="margin-top:48px;padding:32px;background:rgba(0,115,106,0.05);border:1px solid rgba(0,115,106,0.2);border-radius:12px">
<h3 style="font-size:18px;font-weight:510;color:#f0f2f4;margin-bottom:16px">Pogledajte i druge industrije</h3>
<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
{industries_section}
</div>
</div>'''

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — BIXIE</title>
<meta property="og:title" content="{title} — BIXIE">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://bixie.ba{url_prefix}/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BIXIE">
<meta property="og:image" content="https://bixie.ba{url_prefix}/og-image.png">
<meta name="description" content="{desc}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="canonical" href="https://bixie.ba{url_prefix}/{slug}">
</head>
<body>
{nav}
<section style="padding:80px 24px">
<div style="max-width:1100px;margin:0 auto">
<span class="tag tag-teal">{'Use Case' if '/use-cases/' in slug else 'Industrija'}</span>
<h1 style="font-size:42px;font-weight:510;line-height:1.1;letter-spacing:-1px;color:#f0f2f4;margin-bottom:16px">{h1}</h1>
<p style="font-size:18px;line-height:1.6;color:#6b7280;max-width:700px;margin-bottom:48px">{lead}</p>
{sections_html}
{industries_link}
<div style="text-align:center;padding:48px 32px;background:rgba(0,115,106,0.05);border:1px solid rgba(0,115,106,0.2);border-radius:12px;margin-top:48px">
<h3 style="font-size:20px;font-weight:510;color:#f0f2f4;margin-bottom:8px">{'Spremni za implementaciju?' if lang=='bs' else 'Ready to implement?'}</h3>
<p style="font-size:15px;color:#6b7280;margin-bottom:20px;max-width:500px;margin-left:auto;margin-right:auto">{'Radimo besplatne konsultacije. Analiziramo vase potrebe i predlazemo najbolje rjesenje.' if lang=='bs' else 'We offer free consultations. We analyze your needs and propose the best solution.'}</p>
<a href="{url_prefix}/contact" class="btn-primary" style="font-size:16px;padding:12px 28px">{cta_text}</a>
</div>
</div>
</section>
{footer}
<script>
function toggleMobile() {{
  var m = document.getElementById("mobileMenu");
  m.classList.toggle("open");
}}
</script>
</body>
</html>'''
    return html

# ─── INDUSTRY PAGES ───

def card(icon, title, text):
    return f'''<div class="card" style="border-left:3px solid #00736a"><h3>{icon} {title}</h3><p style="line-height:1.7;margin-bottom:4px">{text}</p></div>'''

def use_case_item(title, desc, link, label):
    return f'''<a href="{link}" class="card" style="display:block;border-left:3px solid #00736a;margin-bottom:16px;text-decoration:none"><div style="display:flex;justify-content:space-between;align-items:flex-start"><div><h3 style="font-size:18px;color:#f0f2f4;margin-bottom:4px">{title}</h3><p style="color:#6b7280;margin-bottom:4px">{desc}</p><span class="badge" style="background:rgba(0,115,106,0.12);color:#00736a;border:1px solid rgba(0,115,106,0.2);padding:2px 10px;border-radius:100px;font-size:12px">{label}</span></div><span style="color:#00736a;font-size:14px;white-space:nowrap">Saznaj vise →</span></div></a>'''

industries = [
    {
        "slug": "industries/finance",
        "title": "AI za Bankarstvo i Finansije — BIXIE",
        "desc": "AI rjesenja za banke i finansijske institucije: on-premise modeli za compliance, analiza rizika, detekcija prevara uz potpunu privatnost podataka.",
        "h1": "AI Rješenja za Bankarstvo i Finansije",
        "lead": "Potpuna privatnost podataka, GDPR i PPO usklađenost uz napredne AI modele na vašoj infrastrukturi. Bez slanja podataka u oblak.",
        "sections": [
            card("🔐", "Compliance i Regulativa", "AI modeli hostani na vašoj infrastrukturi garantuju potpunu usklađenost sa GDPR-om, PPO-om i lokalnim regulatornim zahtjevima. Podaci o klijentima nikada ne napuštaju vašu mrežu."),
            card("📊", "Analiza Kreditnog Rizika", "DeepSeek R1 i Llama 4 za naprednu analizu kreditnog rizika, obradu ogromnih količina podataka o klijentima i automatsko generisanje izvještaja."),
            card("🚨", "Detekcija Prevara", "AI modeli za prepoznavanje sumnjivih transakcija u realnom vremenu. Fine-tunovani na istorijskim podacima o prevarama za maksimalnu tačnost."),
            card("📄", "Automatizacija Obrade Dokumenata", "IDP (Intelligent Document Processing) za automatsku obradu ugovora, zahtjeva i izvještaja. Smanjenje vremena obrade za 80%."),
            card("⚖️", "PPO Obračun i Izvještaji", "Automatski obračun poreza po odbitku na inostrane licence, generisanje izvještaja za poresku upravu i praćenje rokova."),
            card("🤖", "AI Agent za Customer Support", "AI agent za korisničku podršku koji odgovara na upite klijenata 24/7, integrisan sa CRM sistemom i potpuno usklađen sa sigurnosnim politikama."),
            "<h2 style='font-size:24px;font-weight:510;color:#f0f2f4;letter-spacing:-0.288px;margin:36px 0 20px'>Primjeri iz prakse</h2>",
            use_case_item("On-Premise AI za Compliance", "Implementacija on-premise AI modela za automatsku provjeru usklađenosti sa regulatornim zahtjevima.", "/use-cases/on-premise-ai", "On-Premise AI"),
            use_case_item("AI Agent za Customer Support", "Custom AI agent za bankarsku podršku integrisan sa Bitrix24 CRM-om.", "/use-cases/customer-support-ai", "AI Agent"),
        ],
        "industries_section": '<a href="/industries/education" class="btn-ghost" style="padding:8px 16px;font-size:13px">🎓 Obrazovanje</a><a href="/industries/manufacturing" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏭 Proizvodnja</a><a href="/industries/public-sector" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏛 Javne Ustanove</a>'
    },
    {
        "slug": "industries/education",
        "title": "AI za Obrazovanje — BIXIE",
        "desc": "AI rjesenja za skole i univerzitete: AI licence po akademskim cijenama, open source modeli na skolskoj infrastrukturi, personalizovano ucenje.",
        "h1": "AI Rješenja za Obrazovanje",
        "lead": "Legalna nabavka AI licenci po akademskim cijenama i implementacija open source AI modela na vlastitoj infrastrukturi. Za škole, fakultete i univerzitete.",
        "sections": [
            card("🎓", "AI Licence po Akademskim Cijenama", "ChatGPT Edu, Google Gemini Education, Microsoft 365 Education, Canva Campus — legalna nabavka uz domaću fakturu i PDV. Značajni popusti za obrazovne ustanove."),
            card("🖥️", "Open Source AI na Školskoj Infrastrukturi", "Llama 4, DeepSeek R1 i Mistral hostani na serverima škole. Potpuna privatnost podataka učenika, bez slanja podataka u SAD ili Kinu."),
            card("📚", "Personalizovani Tutor", "AI modeli fine-tunovani na nastavne materijale škole za personalizovano učenje. Svaki učenik dobija prilagođenog asistenta."),
            card("👨‍🏫", "Asistent Nastavnicima", "Automatsko generisanje testova, ocjenjivanje eseja, priprema nastavnih materijala i personalizovanih zadataka za svakog učenika."),
            card("🔐", "Privatnost Podataka", "Za razliku od ChatGPT-a koji podatke šalje u SAD, open source modeli hostani lokalno garantuju da podaci učenika nikada ne napuštaju ustanovu."),
            card("💰", "Ušteda na Licencama", "Open source modeli eliminišu troškove pretplate po korisniku. Jednokratna investicija u hardver koja se isplati za 12-18 mjeseci."),
            "<h2 style='font-size:24px;font-weight:510;color:#f0f2f4;letter-spacing:-0.288px;margin:36px 0 20px'>Primjeri iz prakse</h2>",
            use_case_item("Open Source AI za Univerzitet", "Implementacija Llama 4 i DeepSeek R1 na univerzitetskoj infrastrukturi za 500+ korisnika.", "/use-cases/on-premise-ai", "On-Premise AI"),
            use_case_item("AI Licence za Obrazovne Ustanove", "Legalna nabavka ChatGPT Edu i Google Gemini licenci sa domaćom fakturom.", "/ai-providers", "AI Licence"),
        ],
        "industries_section": '<a href="/industries/finance" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏦 Bankarstvo</a><a href="/industries/manufacturing" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏭 Proizvodnja</a><a href="/industries/public-sector" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏛 Javne Ustanove</a>'
    },
    {
        "slug": "industries/manufacturing",
        "title": "AI za Proizvodnju — BIXIE",
        "desc": "AI i RPA rjesenja za proizvodne firme: prediktivno odrzavanje, optimizacija proizvodnje, AI vizuelna inspekcija i automatizacija procesa.",
        "h1": "AI i RPA Rješenja za Proizvodnju",
        "lead": "Povećajte efikasnost proizvodnje uz AI modele za prediktivno održavanje, vizuelnu inspekciju i RPA automatizaciju administrativnih procesa.",
        "sections": [
            card("🔧", "Prediktivno Održavanje", "AI modeli analiziraju podatke sa IoT senzora i predviđaju kvarove prije nego što se dogode. Smanjenje zastoja do 50% i troškova održavanja do 30%."),
            card("👁️", "AI Vizuelna Inspekcija", "Računarski vid za automatsku detekciju grešaka na proizvodnoj liniji. Brže i preciznije od ljudske inspekcije, radi 24/7."),
            card("📦", "Optimizacija Zaliha", "AI modeli za predikciju potražnje i optimizaciju nivoa zaliha. Smanjenje troškova skladištenja uz istovremeno povećanje dostupnosti proizvoda."),
            card("🤖", "RPA Automatizacija Administracije", "RPA botovi za automatski unos podataka, generisanje izvještaja, obradu narudžbi i fakturisanje. Smanjenje administrativnog opterećenja za 70%."),
            card("📊", "AI za Kontrolu Kvaliteta", "Deep learning modeli za analizu proizvoda u realnom vremenu. Detekcija mikropukotina, deformacija i drugih defekata nevidljivih ljudskom oku."),
            card("🔗", "Integracija sa ERP-om", "Povezivanje AI modela sa postojećim ERP sistemom (Pantheon, SAP, Microsoft Dynamics) za potpunu automatizaciju toka podataka."),
            "<h2 style='font-size:24px;font-weight:510;color:#f0f2f4;letter-spacing:-0.288px;margin:36px 0 20px'>Primjeri iz prakse</h2>",
            use_case_item("RPA za Automatizaciju Nabavke", "Automatizacija cjelokupnog procesa nabavke sa AI validacijom dokumentacije.", "/use-cases/document-processing", "Document Processing"),
            use_case_item("AI Agent za Customer Support", "AI agent za automatsku obradu reklamacija i upita kupaca.", "/use-cases/customer-support-ai", "AI Agent"),
        ],
        "industries_section": '<a href="/industries/finance" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏦 Bankarstvo</a><a href="/industries/education" class="btn-ghost" style="padding:8px 16px;font-size:13px">🎓 Obrazovanje</a><a href="/industries/public-sector" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏛 Javne Ustanove</a>'
    },
    {
        "slug": "industries/public-sector",
        "title": "AI za Javne Ustanove — BIXIE",
        "desc": "Digitalna transformacija javne uprave: open source AI modeli za transparentnost, efikasnost i smanjenje troskova uz potpunu sigurnost podataka.",
        "h1": "AI Rješenja za Javne Ustanove",
        "lead": "Digitalizacija javne uprave kroz open source AI modele, RPA automatizaciju i sigurnu infrastrukturu. Bez zavisnosti od stranih provajdera.",
        "sections": [
            card("🏛️", "Digitalna Transformacija Uprave", "Implementacija digitalnog ureda, automatizacija administrativnih procesa i prelazak na bezpapirno poslovanje. Smanjenje troškova administracije do 40%."),
            card("🔐", "Potpuna Sigurnost Podataka", "Open source AI modeli hostani na državnoj infrastrukturi. Podaci građana nikada ne napuštaju jurisdikciju BiH. Potpuna usklađenost sa Zakonom o zaštiti podataka."),
            card("📄", "Automatizacija Obrade Predmeta", "IDP za automatsku obradu zahtjeva građana, rješenja, ugovora i druge dokumentacije. Smanjenje vremena obrade sa sedmica na sate."),
            card("🤖", "AI Asistent za Građane", "AI agent za automatsko odgovaranje na upite građana putem web portala, emaila i telefona. 24/7 dostupnost, smanjenje opterećenja službenika."),
            card("💰", "Transparentnost i Analiza Budžeta", "AI modeli za analizu budžetske potrošnje, detekciju anomalija i automatsko generisanje izvještaja o transparentnosti."),
            card("♻️", "Nezavisnost od Stranih Provajdera", "Open source modeli eliminišu zavisnost od OpenAI, Google i Microsoft. Potpuna digitalna suverenost uz domaću infrastrukturu i podršku."),
            "<h2 style='font-size:24px;font-weight:510;color:#f0f2f4;letter-spacing:-0.288px;margin:36px 0 20px'>Primjeri iz prakse</h2>",
            use_case_item("On-Premise AI za Javnu Upravu", "Implementacija Llama 4 i DeepSeek R1 na državnoj infrastrukturi za obradu dokumenata.", "/use-cases/on-premise-ai", "On-Premise AI"),
            use_case_item("RPA za Administrativne Procese", "Automatizacija obrade zahtjeva i generisanje rješenja.", "/use-cases/document-processing", "Document Processing"),
        ],
        "industries_section": '<a href="/industries/finance" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏦 Bankarstvo</a><a href="/industries/education" class="btn-ghost" style="padding:8px 16px;font-size:13px">🎓 Obrazovanje</a><a href="/industries/manufacturing" class="btn-ghost" style="padding:8px 16px;font-size:13px">🏭 Proizvodnja</a>'
    },
]

# ─── USE CASE PAGES ───

use_cases = [
    {
        "slug": "use-cases/customer-support-ai",
        "title": "AI Agent za Customer Support — BIXIE",
        "desc": "Implementacija AI agenta za korisnicku podrsku. 24/7 automatski odgovori, integracija sa CRM-om, smanjenje troskova podrske do 60%.",
        "h1": "AI Agent za Customer Support",
        "lead": "Custom AI agent koji odgovara na upite korisnika 24/7 putem web chata, WhatsAppa i emaila. Integrisan sa vašim CRM-om i bazom znanja.",
        "sections": [
            card("⚡", "Trenutni Odgovori 24/7", "AI agent odgovara na upite korisnika u roku od nekoliko sekundi, 24 sata dnevno, 7 dana u sedmici. Bez čekanja, bez redova."),
            card("🔗", "Integracija sa CRM-om", "Automatsko kreiranje i ažuriranje ticketa u Bitrix24, Zoho, Salesforce ili HubSpot. Sva komunikacija se bilježi u CRM-u."),
            card("📚", "Baza Znanja", "AI agent koristi vašu bazu znanja, FAQ i dokumentaciju za tačne odgovore. Lako ažuriranje putem običnog teksta."),
            card("📈", "Analitika i Izvještaji", "Detaljni izvještaji o najčešćim upitima, vremenu odgovora, zadovoljstvu korisnika i trendovima."),
            card("🔐", "Potpuna Privatnost", "Opcija on-premise hostinga za osjetljive podatke. Podaci o korisnicima nikada ne napuštaju vašu infrastrukturu."),
            card("💰", "Smanjenje Troškova do 60%", "AI agent rješava 70-80% upita bez potrebe za ljudskim operaterom. Smanjenje troškova korisničke podrške do 60%."),
        ]
    },
    {
        "slug": "use-cases/sales-automation",
        "title": "Automatizacija Prodaje — BIXIE",
        "desc": "AI agenti za automatizaciju prodajnog procesa: kvalifikacija leadova, automatski follow-up, predviđanje prodaje i personalizovane ponude.",
        "h1": "AI Automatizacija Prodaje",
        "lead": "Automatizacija cjelokupnog prodajnog procesa — od kvalifikacije leadova do zatvaranja posla. Više sastanaka, manje administrativnog posla.",
        "sections": [
            card("🎯", "Kvalifikacija Leadova", "AI agent automatski analizira i kvalifikuje leadove prema vašim kriterijima. Samo kvalifikovani leadovi dolaze do prodajnog tima."),
            card("📧", "Automatski Follow-Up", "Personalizovani emailovi i poruke u pravo vrijeme. AI prati ponašanje leadova i šalje follow-up kad je najveća šansa za konverziju."),
            card("📊", "Predviđanje Prodaje", "AI modeli analiziraju istorijske podatke i predviđaju vjerovatnoću zatvaranja posla, optimalnu cijenu i najbolji trenutak za kontakt."),
            card("🤝", "Personalizovane Ponude", "Automatsko generisanje personalizovanih ponuda na osnovu potreba i budžeta klijenta. Integracija sa Bloom OS sistemom za ponude."),
            card("📱", "Multi-Channel Outreach", "AI agent komunicira sa leadovima putem emaila, LinkedIna, WhatsAppa i telefona. Sve u jednom sistemu."),
            card("📈", "Detaljna Analitika", "Pratite svaki korak prodajnog procesa. Konverzije, pipeline, brzina zatvaranja — sve u realnom vremenu."),
        ]
    },
    {
        "slug": "use-cases/document-processing",
        "title": "Inteligentna Obrada Dokumenata — BIXIE",
        "desc": "IDP (Intelligent Document Processing) za automatsku obradu ugovora, faktura i zahtjeva. AI prepoznaje, klasificira i ekstrahira podatke.",
        "h1": "Inteligentna Obrada Dokumenata",
        "lead": "Automatska obrada ugovora, faktura, zahtjeva i druge dokumentacije uz pomoć AI modela. Smanjenje vremena obrade za 80%.",
        "sections": [
            card("📄", "Automatska Klasifikacija", "AI prepoznaje tip dokumenta (ugovor, faktura, zahtjev, rješenje) i automatski ga klasificira. Bez ručnog sortiranja."),
            card("🔍", "Ekstrakcija Podataka", "Izvlachenje ključnih informacija iz dokumenata: iznosi, datumi, strane, potpisnici. Tačnost preko 95%."),
            card("🔄", "Integracija sa Sistemima", "Automatski unos ekstrahovanih podataka u CRM, ERP ili DMS. Bez ručnog prekucavanja, bez grešaka."),
            card("✅", "Validacija i Verifikacija", "AI provjerava tačnost podataka i ukazuje na potencijalne greške ili nedosljednosti prije unosa u sistem."),
            card("🔐", "Sigurnost i Privatnost", "Svi dokumenti ostaju na vašoj infrastrukturi. Opcija on-premise hostinga za najosjetljivije dokumente."),
            card("📊", "Praćenje i Izvještaji", "Detaljno praćenje svakog dokumenta kroz proces obrade. Izvještaji o učinku, greškama i vremenu obrade."),
        ]
    },
    {
        "slug": "use-cases/on-premise-ai",
        "title": "On-Premise AI Infrastruktura — BIXIE",
        "desc": "Implementacija open source AI modela na vasoj infrastrukturi. Llama 4, DeepSeek R1, Mistral — potpuna kontrola, privatnost i nezavisnost.",
        "h1": "On-Premise AI za Povjerljive Podatke",
        "lead": "Hostajte open source AI modele na vlastitom hardveru. Potpuna privatnost podataka, nema mjesečnih naknada po korisniku, nema zavisnosti od provajdera.",
        "sections": [
            card("🔐", "Potpuna Privatnost", "Vaši podaci nikada ne napuštaju vašu infrastrukturu. Idealno za finansije, zdravstvo, pravni sektor i javnu upravu."),
            card("💰", "Bez Mjesečnih Naknada", "Jednokratna investicija u hardver bez pretplate po korisniku. Ušteda od 60-80% u odnosu na ChatGPT Enterprise za 50+ korisnika."),
            card("🎯", "Fine-Tuning na Vašim Podacima", "Prilagodite model vašoj terminologiji, procesima i domenu. LoRA i QLoRA fine-tuning na vašim podacima."),
            card("🔄", "Sloboda Izmjene Modela", "Koristite Llama 4 danas, DeepSeek R1 sutra. Mijenjate model kad god želite, bez ugovornih ograničenja."),
            card("⚡", "Performance na Vašem Hardveru", "Optimizacija inference enginea (vLLM, llama.cpp, TensorRT-LLM) za maksimalne performanse na vašem hardveru."),
            card("🛠️", "Kompletna Podrška", "Od izbora hardvera do produkcijskog deploymenta. BIXIE pruža kompletnu uslugu implementacije i održavanja."),
        ]
    },
]

# Generate BS pages
for ind in industries:
    html = make_page(
        title=ind['title'], desc=ind['desc'], h1=ind['h1'], lead=ind['lead'],
        sections=ind['sections'], slug=ind['slug'],
        industries_section=ind.get('industries_section')
    )
    path = os.path.join(SITE, ind['slug'], 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ {ind['slug']}/index.html")

for uc in use_cases:
    html = make_page(
        title=uc['title'], desc=uc['desc'], h1=uc['h1'], lead=uc['lead'],
        sections=uc['sections'], slug=uc['slug']
    )
    path = os.path.join(SITE, uc['slug'], 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ {uc['slug']}/index.html")

# Generate EN pages (copy BS with nav/footer replacements)
for ind in industries:
    html = make_page(
        title=ind['title'], desc=ind['desc'], h1=ind['h1'], lead=ind['lead'],
        sections=ind['sections'], slug=ind['slug'], lang='en',
        industries_section=ind.get('industries_section')
    )
    path = os.path.join(SITE, 'en', ind['slug'], 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ en/{ind['slug']}/index.html")

for uc in use_cases:
    html = make_page(
        title=uc['title'], desc=uc['desc'], h1=uc['h1'], lead=uc['lead'],
        sections=uc['sections'], slug=uc['slug'], lang='en'
    )
    path = os.path.join(SITE, 'en', uc['slug'], 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ en/{uc['slug']}/index.html")

print("\n🎉 All pages generated!")
