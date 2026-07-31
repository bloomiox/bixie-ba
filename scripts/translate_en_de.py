#!/usr/bin/env python3
"""Translate EN/DE page titles and meta descriptions from Bosnian to English/German."""
import os, re

ROOT = "/root/bixie-site"

# path -> {title, desc} in the target language (EN for en/*, DE for de/*)
TRANSLATIONS = {
    # ---------- EN ----------
    "en/index.html": {
        "title": "BIXIE — CRM, AI Agents & Digital Transformation",
        "desc": "Registered HubSpot, Salesforce, Zoho, Pipedrive and Bitrix Consulting Partner. CRM implementation, AI agents, Private Cloud and digital transformation for your business."},
    "en/ai-providers/index.html": {
        "title": "AI Providers & Licences — BIXIE | ChatGPT, Gemini, Claude",
        "desc": "AI licence procurement for companies and education. ChatGPT, Gemini, Claude, DeepSeek with local invoice and VAT."},
    "en/services/crm/index.html": {
        "title": "CRM Solutions — BIXIE",
        "desc": "Bitrix24, Zoho CRM, Salesforce, HubSpot, Pipedrive, Twenty CRM and SugarCRM. CRM implementation, migration and optimisation."},
    "en/use-cases/document-processing/index.html": {
        "title": "Intelligent Document Processing — BIXIE",
        "desc": "IDP (Intelligent Document Processing) for automatic processing of contracts, invoices and claims. AI recognises, classifies and extracts data."},
    "en/blog/posts/case-study-etrgovina-povecala-prodaju-40/index.html": {
        "title": "Case Study: E-commerce Increased Sales by 40% with AI Agents — BIXIE",
        "desc": "How an online shop with 15,000 products increased sales by 40% using an AI sales agent and RPA automation."},
    "en/blog/posts/llama-4-vs-deepseek-r1-poredjenje/index.html": {
        "title": "Llama 4 vs DeepSeek R1 — Which Open Source Model to Choose in 2026? — BIXIE",
        "desc": "Detailed comparison of Meta Llama 4 and DeepSeek R1. Performance, pricing, hardware requirements and recommendations for different use cases."},
    "en/blog/posts/case-study-startup-ustedio-10000-km/index.html": {
        "title": "Case Study: How a Startup Saved 10,000 KM with RPA and AI — BIXIE",
        "desc": "A fintech startup with 8 employees saved 10,000 KM per year by automating financial processes with RPA and AI."},
    "en/blog/posts/buducnost-rada-ljudi-ai-agenti/index.html": {
        "title": "The Future of Work: Humans and AI Agents Together — BIXIE",
        "desc": "How AI agents will change the way we work and how to prepare for a future of working with AI systems."},
    "en/blog/posts/open-source-ai-modeli-vodic-2026/index.html": {
        "title": "Open Source AI Models — The Complete 2026 Guide — BIXIE",
        "desc": "Everything you need to know about open source AI models: Llama 4, DeepSeek R1, Mistral, Qwen 3, Phi-4, Gemma 3. Comparison, performance, hosting costs."},
    "en/blog/posts/implementirati-ai-agente-4-sedmice/index.html": {
        "title": "How to Implement AI Agents in 4 Weeks — BIXIE",
        "desc": "A practical guide to implementing AI agents in your company. Step-by-step 4-week plan."},
    "en/blog/posts/signali-da-treba-ai-agente/index.html": {
        "title": "Signs Your Company Needs AI Agents — BIXIE",
        "desc": "10 signs that it's time to consider implementing AI agents in your business."},
    "en/blog/posts/sigurnost-on-premise-ai-sistema/index.html": {
        "title": "On-Premise AI Security — Best Practices — BIXIE",
        "desc": "How to secure an on-premise AI system. Encryption, authentication, audit logging, network security and protecting models from unauthorised access."},
    "en/blog/posts/open-source-ai-obrazovanje/index.html": {
        "title": "Open Source AI in Education — From Primary School to University — BIXIE",
        "desc": "How educational institutions use open source AI models for personalised learning, teacher assistants and administrative tasks."},
    "en/blog/posts/ai-agenti-vs-tradicionalni-chatbotovi/index.html": {
        "title": "AI Agents vs Traditional Chatbots: Key Differences — BIXIE",
        "desc": "What sets AI agents apart from traditional chatbots? Comparison of capabilities, costs and applications."},
    "en/blog/posts/ai-agenti-lead-generation/index.html": {
        "title": "How AI Agents Help with Lead Generation — BIXIE",
        "desc": "AI agents for lead generation — strategies, tools and best practices for Bosnian companies."},
    "en/blog/posts/gpu-server-za-ai-infrastruktura-troskovi/index.html": {
        "title": "GPU Server for AI — How Much Does Open Source Model Infrastructure Cost? — BIXIE",
        "desc": "Detailed cost analysis of GPU servers for AI. From single-GPU setups to production clusters. Comparison with subscription models."},
    "en/blog/posts/odabrati-pravog-ai-agenta/index.html": {
        "title": "How to Choose the Right AI Agent for Your Company — BIXIE",
        "desc": "A guide to choosing an AI agent tailored to your needs. Comparison of agent types, prices and features."},
    "en/blog/posts/ai-agenti-upravljanje-znanjem/index.html": {
        "title": "AI Agents for Knowledge Management — BIXIE",
        "desc": "How AI agents can help organise, store and search your company's business knowledge."},
    "en/blog/posts/ollama-vllm-llama-cpp-poredjenje-enginea/index.html": {
        "title": "Ollama, vLLM, llama.cpp — Which Inference Engine to Choose for Open Source AI? — BIXIE",
        "desc": "Detailed comparison of popular inference engines for open source AI models. Performance, simplicity, flexibility and recommendations."},
    "en/blog/posts/multi-agent-sistemi-kako-rade-zajedno/index.html": {
        "title": "Multi-Agent Systems: How Multiple Agents Work Together — BIXIE",
        "desc": "How multi-agent systems work and why they are more efficient than single-agent solutions for complex business tasks."},
    "en/blog/posts/zasto-firme-prelaze-na-open-source-ai/index.html": {
        "title": "Why Companies Are Moving to Open Source AI Models? Trend Analysis — BIXIE",
        "desc": "More and more companies are leaving subscription AI models and moving to open source. We analyse the reasons: costs, privacy, independence and performance."},
    "en/blog/posts/ai-agenti-gdpr-sta-morate-znati/index.html": {
        "title": "AI Agents and GDPR: What You Need to Know — BIXIE",
        "desc": "Everything you need to know about aligning AI agents with GDPR regulations. Data privacy and legal security."},
    "en/blog/posts/ai-agenti-transformisu-prodaju/index.html": {
        "title": "How AI Agents Are Transforming Sales in 2026 — BIXIE",
        "desc": "AI agents are changing the way companies sell. Discover how autonomous sales agents increase conversion and reduce costs."},
    "en/blog/posts/ai-agenti-automatizacija-marketinga/index.html": {
        "title": "AI Agents for Marketing Automation — BIXIE",
        "desc": "How AI agents can automate your marketing campaigns — from segmentation to personalisation and A/B testing."},
    "en/blog/posts/automatizacija-korisnicke-podrske-ai/index.html": {
        "title": "How to Automate Customer Support with AI Agents — BIXIE",
        "desc": "A step-by-step guide to automating customer support with AI agents. Reduce costs and increase satisfaction."},
    "en/blog/posts/qwen-3-alibabin-model-rekordi-konteksta/index.html": {
        "title": "Qwen 3 — Alibaba's AI Model Breaking Context Records — BIXIE",
        "desc": "An overview of the Qwen 3 model family. 1M token context, tool-use capabilities, performance and practical business applications."},
    "en/blog/posts/ai-agenti-ljudski-resursi/index.html": {
        "title": "AI Agents for Human Resources: The HR Revolution — BIXIE",
        "desc": "How AI agents transform HR processes — from recruitment to onboarding and performance management."},
    "en/blog/posts/case-study-it-firma-smanjila-troskove-60/index.html": {
        "title": "Case Study: IT Company Cut Support Costs by 60% — BIXIE",
        "desc": "How an IT company with 45 employees cut customer support costs by 60% by implementing AI agents. Detailed case study."},
    "en/blog/posts/microsoft-phi-4-mali-modeli-velike-stvari/index.html": {
        "title": "Microsoft Phi-4 — Small Models Doing Big Things — BIXIE",
        "desc": "An overview of the Microsoft Phi-4 family. Performance, hardware requirements and use cases for small and medium businesses."},
    "en/blog/posts/postavljanje-on-premise-ai-servera/index.html": {
        "title": "How to Set Up an On-Premise AI Server — Step-by-Step Guide — BIXIE",
        "desc": "A complete guide to setting up an on-premise AI server. From hardware selection to model deployment. Llama, DeepSeek, Mistral on your hardware."},
    "en/blog/posts/mistral-large-2-evropski-ai-model/index.html": {
        "title": "Mistral Large 2 — The European AI Model Competing with GPT-4 — BIXIE",
        "desc": "A detailed overview of Mistral Large 2. Performance, GDPR compliance, multilingual support and comparison with leading models."},
    "en/blog/posts/agentic-ai-vodic-pocetnici/index.html": {
        "title": "Agentic AI: A Beginner's Guide — BIXIE",
        "desc": "What is Agentic AI and how does it work? Everything you need to know about autonomous agents that take actions on your behalf."},

    # ---------- DE ----------
    "de/index.html": {
        "title": "BIXIE — CRM, KI-Agenten & Digitale Transformation",
        "desc": "Registrierter HubSpot-, Salesforce-, Zoho-, Pipedrive- und Bitrix-Consulting-Partner. CRM-Implementierung, KI-Agenten, Private Cloud und digitale Transformation für Ihr Unternehmen."},
    "de/ai-providers/index.html": {
        "title": "KI-Anbieter & Lizenzen — BIXIE | ChatGPT, Gemini, Claude",
        "desc": "Beschaffung von KI-Lizenzen für Unternehmen und Bildung. ChatGPT, Gemini, Claude, DeepSeek mit lokaler Rechnung und MwSt."},
    "de/services/crm/index.html": {
        "title": "CRM-Lösungen — BIXIE",
        "desc": "Bitrix24, Zoho CRM, Salesforce, HubSpot, Pipedrive, Twenty CRM und SugarCRM. Implementierung, Migration und Optimierung von CRM-Systemen."},
    "de/blog/posts/case-study-etrgovina-povecala-prodaju-40/index.html": {
        "title": "Fallstudie: E-Commerce steigerte den Umsatz um 40 % mit KI-Agenten — BIXIE",
        "desc": "Wie ein Online-Shop mit 15.000 Produkten den Umsatz um 40 % steigerte — mit einem KI-Vertriebsagenten und RPA-Automation."},
    "de/blog/posts/case-study-startup-ustedio-10000-km/index.html": {
        "title": "Fallstudie: Wie ein Startup 10.000 KM mit RPA und KI sparte — BIXIE",
        "desc": "Ein Fintech-Startup mit 8 Mitarbeitern sparte 10.000 KM pro Jahr durch die Automatisierung von Finanzprozessen mit RPA und KI."},
    "de/blog/posts/buducnost-rada-ljudi-ai-agenti/index.html": {
        "title": "Die Zukunft der Arbeit: Menschen und KI-Agenten zusammen — BIXIE",
        "desc": "Wie KI-Agenten unsere Arbeitsweise verändern werden und wie Sie sich auf die Zukunft der Arbeit mit KI-Systemen vorbereiten."},
    "de/blog/posts/implementirati-ai-agente-4-sedmice/index.html": {
        "title": "KI-Agenten in 4 Wochen implementieren — BIXIE",
        "desc": "Ein praktischer Leitfaden zur Implementierung von KI-Agenten in Ihrem Unternehmen. Schritt-für-Schritt-Plan für 4 Wochen."},
    "de/blog/posts/signali-da-treba-ai-agente/index.html": {
        "title": "Anzeichen, dass Ihr Unternehmen KI-Agenten braucht — BIXIE",
        "desc": "10 Anzeichen, dass es Zeit ist, über die Implementierung von KI-Agenten in Ihrem Unternehmen nachzudenken."},
    "de/blog/posts/ai-agenti-vs-tradicionalni-chatbotovi/index.html": {
        "title": "KI-Agenten vs. traditionelle Chatbots: Die wichtigsten Unterschiede — BIXIE",
        "desc": "Was unterscheidet KI-Agenten von traditionellen Chatbots? Vergleich von Fähigkeiten, Kosten und Anwendungen."},
    "de/blog/posts/ai-agenti-lead-generation/index.html": {
        "title": "Wie KI-Agenten bei der Lead-Generierung helfen — BIXIE",
        "desc": "KI-Agenten zur Lead-Generierung — Strategien, Tools und Best Practices für Unternehmen in Bosnien."},
    "de/blog/posts/odabrati-pravog-ai-agenta/index.html": {
        "title": "Den richtigen KI-Agenten für Ihr Unternehmen wählen — BIXIE",
        "desc": "Ein Leitfaden zur Auswahl des passenden KI-Agenten. Vergleich von Agententypen, Preisen und Funktionen."},
    "de/blog/posts/ai-agenti-upravljanje-znanjem/index.html": {
        "title": "KI-Agenten für das Wissensmanagement im Unternehmen — BIXIE",
        "desc": "Wie KI-Agenten helfen, das Geschäftswissen Ihres Unternehmens zu organisieren, zu speichern und zu durchsuchen."},
    "de/blog/posts/multi-agent-sistemi-kako-rade-zajedno/index.html": {
        "title": "Multi-Agenten-Systeme: Wie mehrere Agenten zusammenarbeiten — BIXIE",
        "desc": "Wie Multi-Agenten-Systeme funktionieren und warum sie für komplexe Geschäftsaufgaben effizienter sind als Einzelagenten-Lösungen."},
    "de/blog/posts/ai-agenti-gdpr-sta-morate-znati/index.html": {
        "title": "KI-Agenten und DSGVO: Was Sie wissen müssen — BIXIE",
        "desc": "Alles, was Sie über die DSGVO-Konformität von KI-Agenten wissen müssen. Datenschutz und rechtliche Sicherheit."},
    "de/blog/posts/ai-agenti-transformisu-prodaju/index.html": {
        "title": "Wie KI-Agenten den Vertrieb 2026 transformieren — BIXIE",
        "desc": "KI-Agenten verändern die Art, wie Unternehmen verkaufen. Entdecken Sie, wie autonome Vertriebsagenten die Konversion steigern und Kosten senken."},
    "de/blog/posts/ai-agenti-automatizacija-marketinga/index.html": {
        "title": "KI-Agenten für die Marketing-Automatisierung — BIXIE",
        "desc": "Wie KI-Agenten Ihre Marketingkampagnen automatisieren — von der Segmentierung bis zur Personalisierung und A/B-Tests."},
    "de/blog/posts/automatizacija-korisnicke-podrske-ai/index.html": {
        "title": "Kundensupport mit KI-Agenten automatisieren — BIXIE",
        "desc": "Eine Schritt-für-Schritt-Anleitung zur Automatisierung des Kundensupports mit KI-Agenten. Kosten senken und Zufriedenheit steigern."},
    "de/blog/posts/ai-agenti-ljudski-resursi/index.html": {
        "title": "KI-Agenten für Human Resources: Die HR-Revolution — BIXIE",
        "desc": "Wie KI-Agenten HR-Prozesse transformieren — von der Rekrutierung bis zum Onboarding und Leistungsmanagement."},
    "de/blog/posts/case-study-it-firma-smanjila-troskove-60/index.html": {
        "title": "Fallstudie: IT-Unternehmen senkte Supportkosten um 60 % — BIXIE",
        "desc": "Wie ein IT-Unternehmen mit 45 Mitarbeitern die Supportkosten durch KI-Agenten um 60 % senkte. Detaillierte Fallstudie."},
    "de/blog/posts/agentic-ai-vodic-pocetnici/index.html": {
        "title": "Agentic AI: Ein Leitfaden für Einsteiger — BIXIE",
        "desc": "Was ist Agentic AI und wie funktioniert es? Alles, was Sie über autonome Agenten wissen müssen, die Aktionen in Ihrem Namen ausführen."},
}

changed = []
for rel, tr in TRANSLATIONS.items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print("MISSING:", rel)
        continue
    html = open(p, encoding="utf-8").read()
    orig = html
    # lang attribute
    lang = "en" if rel.startswith("en/") else "de"
    html = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang}">', html, count=1)
    # title
    html = re.sub(r'<title>[^<]*</title>', f'<title>{tr["title"]}</title>', html, count=1)
    # og:title / twitter:title
    html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{tr["title"]}"', html, count=1)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*"', f'<meta name="twitter:title" content="{tr["title"]}"', html, count=1)
    # descriptions (og, twitter, meta)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{tr["desc"]}"', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*"', f'<meta name="twitter:description" content="{tr["desc"]}"', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{tr["desc"]}"', html, count=1)
    if html != orig:
        open(p, "w", encoding="utf-8").write(html)
        changed.append(rel)

print(f"Files translated: {len(changed)}")
