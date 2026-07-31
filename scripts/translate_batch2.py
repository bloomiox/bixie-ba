#!/usr/bin/env python3
"""Translate remaining EN/DE pages: Bosnian titles + descriptions -> English/German."""
import os, re

ROOT = "/root/bixie-site"

# path -> {title?, desc} (title optional: only when title needs translation)
T = {
    # ---------- EN ----------
    "en/use-cases/on-premise-ai/index.html": {
        "title": "On-Premise AI Infrastructure — BIXIE | Open Source AI Models",
        "desc": "Open source AI model deployment on your infrastructure. Llama 4, DeepSeek R1, Mistral — full control, privacy and independence."},
    "en/use-cases/customer-support-ai/index.html": {
        "title": "AI Agent for Customer Support — BIXIE",
        "desc": "AI agent implementation for customer support. 24/7 automatic responses, CRM integration, support cost reduction up to 60%."},
    "en/use-cases/sales-automation/index.html": {
        "title": "Sales Automation with AI — BIXIE",
        "desc": "AI agents for sales process automation: lead qualification, automatic follow-up, sales forecasting and personalised proposals."},
    "en/services/digital-transformation/index.html": {
        "desc": "Business process optimisation, AI integrations into ERP/DMS systems, workflow automation. IT consulting and strategy."},
    "en/services/rpa/index.html": {
        "desc": "RPA automation of business processes with AI. Automating data entry, document processing and reporting."},
    "en/services/ai-agents/index.html": {
        "desc": "Custom AI agents for customer support and sales. AI implementation and licences for ChatGPT, Gemini, Copilot and Claude."},
    "en/blog/index.html": {
        "desc": "Tips, guides and analyses on CRM systems, AI agents, RPA automation and digital transformation for companies in Bosnia."},
    "en/blog/posts/open-source-ai-finansijski-sektor/index.html": {
        "title": "Open Source AI for the Financial Sector — Privacy and Compliance — BIXIE",
        "desc": "How financial institutions use open source AI models for risk analysis, fraud detection and compliance with full data privacy."},
    "en/blog/posts/buducnost-open-source-ai-2027/index.html": {
        "title": "The Future of Open Source AI — What Does 2027 Bring? — BIXIE",
        "desc": "Predictions for open source AI in 2027. New models, cheaper hardware, multi-agent systems and full democratisation of AI technology."},
    "en/blog/posts/fine-tuning-open-source-modela/index.html": {
        "title": "Fine-Tuning Open Source Models on Your Data — The Complete Guide — BIXIE",
        "desc": "How to adapt an open source AI model to your business. LoRA, QLoRA, full fine-tuning. Examples, tools and best practices."},
    "en/blog/posts/10-primjena-ai-agenta-male-firme/index.html": {
        "title": "10 AI Agent Applications for Small Businesses — BIXIE",
        "desc": "Small companies often think AI agents are only for large corporations. Discover 10 practical applications for your business."},
    "en/blog/posts/case-study-automatizacija-onboardinga/index.html": {
        "title": "Case Study: Automating the Onboarding Process with AI Agents — BIXIE",
        "desc": "How an IT company automated new employee onboarding with AI agents, cutting onboarding time by 60%."},
    "en/blog/posts/agentic-ai-finansijski-sektor/index.html": {
        "title": "Agentic AI for the Financial Sector: Applications and Benefits — BIXIE",
        "desc": "How autonomous AI agents are transforming the financial sector — analysis, reports, anomaly detection."},
    "en/blog/posts/deepseek-r1-lokalni-hardver-performanse/index.html": {
        "title": "DeepSeek R1 on Local Hardware — Performance and Optimisation — BIXIE",
        "desc": "How to host DeepSeek R1 on your own hardware. Benchmarks, quantisation, hardware requirements and optimisation for production use."},
    "en/privacy/index.html": {
        "desc": "Privacy Policy and terms of use of BIXIE services."},
    "en/industries/manufacturing/index.html": {
        "title": "AI for Manufacturing — BIXIE",
        "desc": "AI and RPA solutions for manufacturing companies: predictive maintenance, production optimisation, AI visual inspection and process automation."},
    "en/industries/public-sector/index.html": {
        "title": "AI for the Public Sector — BIXIE",
        "desc": "Digital transformation of public administration: open source AI models for transparency, efficiency and cost reduction with full data security."},
    "en/industries/finance/index.html": {
        "title": "AI for Banking and Finance — BIXIE",
        "desc": "AI solutions for banks and financial institutions: on-premise models for compliance, risk analysis, fraud detection with full data privacy."},
    "en/industries/education/index.html": {
        "title": "AI for Education — BIXIE",
        "desc": "AI solutions for schools and universities: AI licences at academic prices, open source models on school infrastructure, personalised learning."},
    "en/contact/index.html": {
        "desc": "Contact BIXIE. Send an inquiry, request a quote or book free consultations. We respond within 24 hours."},

    # ---------- DE ----------
    "de/services/digital-transformation/index.html": {
        "desc": "Optimierung von Geschäftsprozessen, KI-Integrationen in ERP/DMS-Systeme, Automatisierung von Arbeitsabläufen. IT-Beratung und Strategie."},
    "de/services/rpa/index.html": {
        "desc": "RPA-Automatisierung von Geschäftsprozessen mit KI. Automatisierung der Dateneingabe, Dokumentenverarbeitung und Berichterstellung."},
    "de/services/ai-agents/index.html": {
        "desc": "Maßgeschneiderte KI-Agenten für Kundensupport und Vertrieb. KI-Implementierung und Lizenzen für ChatGPT, Gemini, Copilot und Claude."},
    "de/blog/index.html": {
        "desc": "Tipps, Leitfäden und Analysen zu CRM-Systemen, KI-Agenten, RPA-Automation und digitaler Transformation für Unternehmen in Bosnien."},
    "de/blog/posts/10-primjena-ai-agenta-male-firme/index.html": {
        "title": "10 KI-Agenten-Anwendungen für kleine Unternehmen — BIXIE",
        "desc": "Kleine Unternehmen glauben oft, KI-Agenten seien nur für große Konzerne. Entdecken Sie 10 praktische Anwendungen für Ihr Unternehmen."},
    "de/blog/posts/case-study-automatizacija-onboardinga/index.html": {
        "title": "Fallstudie: Automatisierung des Onboarding-Prozesses mit KI-Agenten — BIXIE",
        "desc": "Wie ein IT-Unternehmen das Onboarding neuer Mitarbeiter mit KI-Agenten automatisierte und die Einarbeitungszeit um 60 % verkürzte."},
    "de/blog/posts/agentic-ai-finansijski-sektor/index.html": {
        "title": "Agentic KI für den Finanzsektor: Anwendungen und Vorteile — BIXIE",
        "desc": "Wie autonome KI-Agenten den Finanzsektor transformieren — Analyse, Berichte, Anomalieerkennung."},
    "de/privacy/index.html": {
        "desc": "Datenschutzerklärung und Nutzungsbedingungen der BIXIE-Dienste."},
    "de/contact/index.html": {
        "desc": "Kontaktieren Sie BIXIE. Anfrage senden, Angebot anfordern oder kostenlose Beratung buchen. Wir antworten innerhalb von 24 Stunden."},
}

changed = []
for rel, tr in T.items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print("MISSING:", rel)
        continue
    html = open(p, encoding="utf-8").read()
    orig = html
    lang = "en" if rel.startswith("en/") else "de"
    html = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang}">', html, count=1)
    if "title" in tr:
        html = re.sub(r'<title>[^<]*</title>', f'<title>{tr["title"]}</title>', html, count=1)
        html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{tr["title"]}"', html, count=1)
        html = re.sub(r'<meta name="twitter:title" content="[^"]*"', f'<meta name="twitter:title" content="{tr["title"]}"', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{tr["desc"]}"', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*"', f'<meta name="twitter:description" content="{tr["desc"]}"', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{tr["desc"]}"', html, count=1)
    if html != orig:
        open(p, "w", encoding="utf-8").write(html)
        changed.append(rel)

print(f"Files translated: {len(changed)}")
