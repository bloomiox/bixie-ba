#!/usr/bin/env python3
"""Generate 15 blog posts about open source AI models and on-prem infrastructure."""
import os, shutil

BLOG_DIR = '/root/bixie-site/blog/posts'
EN_BLOG_DIR = '/root/bixie-site/en/blog/posts'
LANG = 'bs'

NAV_BS = '''<nav>
<div class="nav-inner">
<a href="/" class="logo"><img src="/images/logo/bixie-logo.png" alt="BIXIE" style="height:36px"></a>
<div class="nav-links">
<div class="dropdown"><a href="/services/crm">CRM</a><div class="dropdown-menu"><a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a></div></div>
<div class="dropdown"><a href="/services/ai-agents">AI</a><div class="dropdown-menu"><a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a><a href="/open-source-infra">Open Source Infrastruktura</a></div></div>
<div class="dropdown"><a href="/services/digital-transformation">Digitalna Transformacija</a><div class="dropdown-menu"><a href="/services/digital-transformation">Pregled</a><a href="/services/rpa">RPA i Automatizacija</a></div></div>
<a href="/about">O nama</a>
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
<a href="/services/digital-transformation">Digitalna Transformacija</a><a href="/services/rpa">RPA i Automatizacija</a>
<a href="/about">O nama</a>
<a href="/ai-providers">AI Licence</a><a href="/open-source-infra">Open Source</a><a href="/blog">Blog</a>
<a href="/contact" style="display:block;margin-top:10px;background:#00736a;color:#fff;padding:10px 16px;border-radius:6px;text-align:center;font-weight:450;font-size:0.9rem">Zatražite ponudu</a>
</div>
</nav>'''

FOOTER_BS = '''<footer>
<div class="footer-inner">
<div><a href="/" style="display:flex;align-items:center;gap:8px;text-decoration:none;font-size:16px;font-weight:510;color:#f0f2f4;margin-bottom:12px"><svg width="24" height="24" viewBox="0 0 28 28" fill="none"><rect width="28" height="28" rx="6" fill="#00736a"/><text x="14" y="19" text-anchor="middle" fill="#fff" font-family="Inter" font-weight="600" font-size="16">B</text></svg>BIXIE</a><p style="font-size:14px;color:#6b7280;line-height:1.6">CRM, AI Agenti i Digitalna Transformacija za vasu firmu.</p></div>
<div><h4>Usluge</h4><a href="/services/crm">CRM Rjesenja</a><br><a href="/services/ai-agents">AI Agenti</a><br><a href="/services/digital-transformation">Digitalna Transformacija</a><br><a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a><br><a href="/open-source-infra">Open Source Infrastruktura</a></div>
<div><h4>Kompanija</h4><a href="/blog">Blog</a><br><a href="/about">O nama</a><br><a href="/contact">Kontakt</a><br><a href="/privacy">Privacy Policy</a></div>
<div><h4>Kontakt</h4><p>hello@bixie.ba</p><p>033 922 622</p><p>Maglajska 1, 71000 Sarajevo</p></div>
</div>
<div class="footer-bottom">2026 BIXIE. All rights reserved.</div>
</footer>'''

# 15 blog posts data
posts = [
    {
        "slug": "open-source-ai-modeli-vodic-2026",
        "title": "Open Source AI Modeli — Potpuni Vodič za 2026.",
        "desc": "Sve što trebate znati o open source AI modelima: Llama 4, DeepSeek R1, Mistral, Qwen 3, Phi-4, Gemma 3. Poređenje, performanse, cijene hostinga.",
        "tag": "Open Source AI",
        "date": "15. Juli 2026",
        "minutes": "14",
        "content": """<p>Open source AI modeli su doživjeli eksplozivan rast u 2026. godini. Dok su prije samo dvije godine vodeći modeli poput GPT-4 i Claude bili dostupni isključivo putem zatvorenih API-ja, danas postoji najmanje šest porodica open source modela koji su po performansama uporedivi ili čak bolji od komercijalnih alternativa.</p>
<p>U ovom vodiču ćemo proći kroz svaki značajan open source model dostupan u 2026. godini, uporediti njihove performanse, cijene hostinga i slučajeve upotrebe.</p>
<h2>Zašto open source AI?</h2>
<p>Prije nego što uđemo u pojedinačne modele, važno je razumjeti zašto sve više firmi bira open source. Tri glavna razloga su: <strong>privatnost podataka</strong> (vaši podaci ne napuštaju vašu infrastrukturu), <strong>troškovi</strong> (jednokratna investicija umjesto mjesečne pretplate po korisniku) i <strong>nezavisnost</strong> (niste vezani za jednog provajdera).</p>
<h2>Pregled modela</h2>
<h3>Meta Llama 4 — Scout, Maverick, Behemoth</h3>
<p>Llama 4 je najpopularnija open source porodica modela. Scout (109B) je optimizovan za obradu ogromnih konteksta do 1M tokena. Maverick (400B+ ekspertni MoE) je najsnažniji za generalne zadatke. Behemoth (2T) je još u treningu ali obećava revolucionarne performanse.</p>
<h3>DeepSeek R1 — Kineski šampion rezonovanja</h3>
<p>DeepSeek R1 sa 671B parametara (37B aktivnih) nudi korak-po-korak rezonovanje koje konkurira OpenAI o3 modelima. Dostupan je pod MIT licencom, što ga čini potpuno slobodnim za komercijalnu upotrebu. Posebno se ističe u matematici, programiranju i logičkom rezonovanju.</p>
<h3>Mistral Large 2 — Evropski ponos</h3>
<p>Mistral Large 2 (123B) je vodeći evropski model sa sjedištem u Francuskoj. Natuspexcelentnu podršku za višejezičnost i potpunu GDPR usklađenost. Konkurira GPT-4 u većini benchmarkova.</p>
<h3>Alibaba Qwen 3 — Kralj konteksta</h3>
<p>Qwen 3 porodica nudi modele od 0.5B do 235B parametara. Qwen 3-235B-A72B podržava kontekst do 1M tokena i ima odlične tool-use sposobnosti, što ga čini idealnim za AI agente.</p>
<h3>Microsoft Phi-4 — Mali ali moćan</h3>
<p>Phi-4 (14B) i Phi-4-mini (3.8B) su Microsoftovi modeli koji nude impresivne performanse za svoju veličinu. Mogu se hostati i na jednom GPU-u, što ih čini najpristupačnijim za manje firme.</p>
<h3>Google Gemma 3 — Nasljeđe Gemini</h3>
<p>Gemma 3 (27B) je Googleov open source model baziran na Gemini tehnologiji. Nudi odličnu višejezičnu podršku i dobar balans veličine i performansi.</p>
<h2>Kako odabrati pravi model?</h2>
<p>Izbor modela zavisi od vaših specifičnih potreba. Za generalne AI asistente preporučujemo Llama 4 Maverick ili Mistral Large 2. Za logičko rezonovanje i programiranje — DeepSeek R1. Za obradu dugih dokumenata — Qwen 3 ili Llama 4 Scout. Za edge deployment na skromnom hardveru — Phi-4 ili Gemma 3.</p>
<h2>Troškovi hostinga</h2>
<p>Cijena hostinga open source modela varira od nekoliko stotina KM (Phi-4 na jednom GPU) do nekoliko desetina hiljada KM (DeepSeek R1 na više GPU-ova) mjesečno. BIXIE vam pomaže da projektujete optimalnu konfiguraciju prema vašim potrebama i budžetu.</p>"""
    },
    {
        "slug": "llama-4-vs-deepseek-r1-poredjenje",
        "title": "Llama 4 vs DeepSeek R1 — Koji Open Source Model Odabrati u 2026?",
        "desc": "Detaljno poređenje Meta Llame 4 i DeepSeek R1. Performanse, cijene, hardverski zahtjevi i preporuke za različite slučajeve upotrebe.",
        "tag": "Poređenje",
        "date": "14. Juli 2026",
        "minutes": "10",
        "content": """<p>Meta Llama 4 i DeepSeek R1 su dva najpopularnija open source AI modela u 2026. godini. Oba su izuzetno moćna, ali su dizajnirana za različite namjene. U ovom članku ih detaljno poredimo.</p>
<h2>Llama 4 — Meta-in ekosistem</h2>
<p>Llama 4 dolazi u tri varijante: Scout (109B, optimizovan za kontekst), Maverick (400B+ ekspertni MoE, najsnažniji) i Behemoth (2T, u treningu). Scout podržava do 1M tokena konteksta, što je najviše u klasi. Maverick je odličan za generalne AI zadatke i fine-tuning.</p>
<h2>DeepSeek R1 — Šampion rezonovanja</h2>
<p>DeepSeek R1 (671B, 37B aktivnih) je specijalizovan za duboko logičko rezonovanje. Na matematičkim benchmarkovima (AIME, MATH) i programerskim zadacima (Codeforces, SWE-bench) redovno nadmašuje Llama 4. Međutim, zahtijeva više GPU memorije.</p>
<h2>Poređenje performansi</h2>
<p>Na generalnim benchmarkovima (MMLU, HellaSwag, WinoGrande) Llama 4 Maverick i DeepSeek R1 su gotovo izjednačeni. Razlike dolaze do izražaja u specijalizovanim zadacima: DeepSeek je bolji u matematici i programiranju, dok je Llama 4 bolja u obradi dugih tekstova i multitaskingu.</p>
<h2>Hardverski zahtjevi</h2>
<p>Llama 4 Scout (109B) zahtijeva minimalno 2× NVIDIA A100 80GB za inference. DeepSeek R1 (671B) zahtijeva 4–8× A100/H100, osim ako se koristi kvantizacija. Phi-4 (14B) i Qwen 3-7B su znatno pristupačniji za manje firme.</p>
<h2>Preporuka</h2>
<p>Odaberite <strong>DeepSeek R1</strong> ako su vam prioritet matematika, programiranje i logičko rezonovanje. Odaberite <strong>Llama 4</strong> za generalne AI asistente, obradu dokumenata i fine-tuning na specifičnim domenima. BIXIE vam pomaže sa implementacijom oba modela.</p>"""
    },
    {
        "slug": "postavljanje-on-premise-ai-servera",
        "title": "Kako Postaviti On-Premise AI Server — Korak po Korak Vodič",
        "desc": "Kompletan vodič za postavljanje on-premise AI servera. Od izbora hardvera do deploymenta modela. Llama, DeepSeek, Mistral na vašem hardveru.",
        "tag": "Vodič",
        "date": "13. Juli 2026",
        "minutes": "12",
        "content": """<p>Postavljanje on-premise AI servera zvuči kompleksno, ali uz pravi pristup može se realizovati za nekoliko dana. U ovom vodiču prolazimo kroz sve korake — od izbora hardvera do pokretanja prvog modela.</p>
<h2>Korak 1: Izbor hardvera</h2>
<p>Prvi i najvažniji korak je odabir odgovarajućeg hardvera. Ključne komponente su: GPU (NVIDIA A100, H100, L40S ili AMD MI300X), RAM (minimalno 64GB, preporučljivo 256GB+), storage (NVMe SSD, minimalno 2TB) i networking (25GbE+ za multi-node setup).</p>
<p>Za manje modele poput Phi-4 (14B) dovoljan je jedan NVIDIA RTX 4090 ili A5000. Za Llama 4 Maverick potrebna su 2–4 A100 80GB. Za DeepSeek R1 (671B) preporučuje se 8× A100 80GB uz kvantizaciju.</p>
<h2>Korak 2: Instalacija OS-a i drajvera</h2>
<p>Preporučujemo Ubuntu 24.04 LTS sa NVIDIA drajverima (550+) i CUDA 12.4+. Instalacija uključuje: NVIDIA drajvere, CUDA toolkit, cuDNN, Docker i NVIDIA Container Toolkit.</p>
<h2>Korak 3: Izbor inference enginea</h2>
<p>Postoji nekoliko popularnih inference enginea: <strong>vLLM</strong> (najbolji za produkciju, podržava PagedAttention i continuous batching), <strong>llama.cpp</strong> (optimizovan za CPU i Apple Silicon, podržava sve vrste kvantizacije), <strong>Ollama</strong> (jednostavan za početnike, odličan za testiranje) i <strong>TensorRT-LLM</strong> (NVIDIA-optimizovan, najbolje performanse na NVIDIA hardveru).</p>
<h2>Korak 4: Deployment modela</h2>
<p>Nakon instalacije enginea, slijedi download modela (iz Hugging Face, ModelScope ili direktno od provajdera) i pokretanje inference servera. Preporučujemo postavljanje API gatewaya (npr. Kong ili Envoy) za load balancing i monitoring.</p>
<h2>Korak 5: Integracija i monitoring</h2>
<p>Posljednji korak je povezivanje modela sa vašim aplikacijama putem OpenAI-kompatibilnog API-ja i postavljanje monitoringa (Prometheus + Grafana) za praćenje performansi i potrošnje resursa.</p>
<h2>Kako BIXIE može pomoći?</h2>
<p>BIXIE projektuje i implementira kompletnu on-premise AI infrastrukturu. Od izbora hardvera do produkcijskog deploymenta, uz garanciju performansi i kontinuiranu podršku.</p>"""
    },
    {
        "slug": "deepseek-r1-lokalni-hardver-performanse",
        "title": "DeepSeek R1 na Lokalnom Hardveru — Performanse i Optimizacija",
        "desc": "Kako hostati DeepSeek R1 na vlastitom hardveru. Benchmarkovi, kvantizacija, hardverski zahtjevi i optimizacija za produkcijsku upotrebu.",
        "tag": "Tehnički",
        "date": "12. Juli 2026",
        "minutes": "9",
        "content": """<p>DeepSeek R1 je jedan od najimpresivnijih open source modela, sa 671B parametara (37B aktivnih kroz MoE arhitekturu). Hostanje ovog modela na lokalnom hardveru je izazov, ali uz pravilnu optimizaciju sasvim izvodljivo.</p>
<h2>Hardverski zahtjevi</h2>
<p>DeepSeek R1 u punoj preciznosti (FP16) zahtijeva ~1.3TB GPU memorije, što podrazumijeva 8× NVIDIA H100 80GB ili 16× A100 80GB. Međutim, uz kvantizaciju na INT4, memorijski otisak pada na ~350GB, što je izvodljivo na 4× A100 80GB.</p>
<h2>Benchmark performansi</h2>
<p>DeepSeek R1 postiže izuzetne rezultate: AIME 2026 — 79.8%, MATH-500 — 97.3%, Codeforces — 96.3 percentil, SWE-bench — 71.2%. Ovi rezultati su uporedivi sa OpenAI o3 i Claude 4 Opus.</p>
<h2>Optimizacija za produkciju</h2>
<p>Za produkcijsku upotrebu preporučujemo: vLLM sa PagedAttention (smanjuje memorijsku fragmentaciju), continuous batching (povećava propusnost), FP8/INT4 kvantizaciju (smanjuje memorijske zahtjeve) i multi-node deployment za najveće modele.</p>
<h2>Troškovi hostinga</h2>
<p>On-premise hosting DeepSeek R1 zahtijeva značajnu početnu investiciju (50.000–150.000 KM za GPU servere), ali dugoročno je isplativiji od pretplatnih modela za veće organizacije sa 50+ korisnika.</p>"""
    },
    {
        "slug": "zasto-firme-prelaze-na-open-source-ai",
        "title": "Zašto Firme Prelaze na Open Source AI Modele? Analiza Trenda",
        "desc": "Sve više firmi napušta pretplatne AI modele i prelazi na open source. Analiziramo razloge: troškovi, privatnost, nezavisnost i performanse.",
        "tag": "Analiza",
        "date": "11. Juli 2026",
        "minutes": "8",
        "content": """<p>U proteklih godinu dana, primjetan je značajan trend prelaska firmi sa pretplatnih AI modela (ChatGPT Enterprise, Claude Team) na open source alternative hostane na vlastitoj infrastrukturi. Šta stoji iza ovog trenda?</p>
<h2>Troškovna analiza</h2>
<p>Firma sa 100 zaposlenih koja koristi ChatGPT Enterprise plaća ~$200/mj po korisniku ili $240.000 godišnje. Za isti iznos može kupiti GPU server (2× NVIDIA H100) koji će trajati 3–5 godina i hostati Llama 4 ili Mistral Large za sve zaposlene bez ikakvih dodatnih troškova po korisniku.</p>
<h2>Privatnost podataka</h2>
<p>Možda i najvažniji razlog. Finansijske institucije, pravne firme i zdravstvene ustanove ne mogu slati osjetljive podatke na servere u SAD ili Kinu. On-premise hosting je jedini način da se osigura potpuna privatnost i compliance sa regulativama poput GDPR-a.</p>
<h2>Kvalitet open source modela</h2>
<p>Sa izlaskom DeepSeek R1, Llama 4 i Mistral Large 2, open source modeli su dostigli nivo performansi koji je prije dvije godine bio rezervisan isključivo za zatvorene modele. Na većini benchmarkova, vodeći open source modeli su u roku od 5% performansi najboljih zatvorenih modela.</p>
<h2>Nezavisnost i fleksibilnost</h2>
<p>Open source modeli nude potpunu fleksibilnost — možete ih fine-tunovati na svojim podacima, mijenjati model kad god želite i prilagođavati ih specifičnim potrebama. Bez ugovornih ograničenja i bez rizika od naglog povećanja cijena.</p>"""
    },
    {
        "slug": "fine-tuning-open-source-modela",
        "title": "Fine-Tuning Open Source Modela na Vašim Podacima — Kompletan Vodič",
        "desc": "Kako prilagoditi open source AI model vašem poslovanju. LoRA, QLoRA, full fine-tuning. Primjeri, alati i najbolje prakse.",
        "tag": "Vodič",
        "date": "10. Juli 2026",
        "minutes": "11",
        "content": """<p>Jedna od najvećih prednosti open source AI modela je mogućnost fine-tuninga — prilagođavanja modela vašim specifičnim podacima, terminologiji i poslovnim procesima. U ovom vodiču prolazimo kroz sve što trebate znati.</p>
<h2>Šta je fine-tuning?</h2>
<p>Fine-tuning je proces dodatnog treniranja već istreniranog modela na vašim podacima. Time model postaje stručnjak za vašu specifičnu domenu — bilo da je riječ o pravnoj terminologiji, medicinskim izvještajima ili korisničkoj podršci.</p>
<h2>Metode fine-tuninga</h2>
<p><strong>LoRA (Low-Rank Adaptation)</strong> — najpopularnija metoda. Dodaje male adapter slojeve na postojeći model, što zahtijeva minimalne resurse. Može se izvoditi na jednom GPU-u. <strong>QLoRA</strong> — LoRA sa kvantizacijom, omogućava fine-tuning velikih modela na potrošačkom hardveru (RTX 4090). <strong>Full fine-tuning</strong> — ažurira sve parametre modela. Najzahtjevniji ali i najefikasniji.</p>
<h2>Priprema podataka</h2>
<p>Kvalitet fine-tuninga direktno zavisi od kvaliteta podataka. Preporučujemo: minimalno 100–1000 primjera za LoRA, 1000–10000 za full fine-tuning. Podaci moraju biti očišćeni, formatirani u instrukcijsko-formatu i reprezentativni za ciljne zadatke.</p>
<h2>Alati i frameworkovi</h2>
<p>Najpopularniji alati uključuju: Unsloth (optimizovan za brzinu), Axolotl (fleksibilan, podržava sve metode), Hugging Face TRL (Transformer Reinforcement Learning) i LitGPT (Lightning AI).</p>
<h2>Primjer iz prakse</h2>
<p>BIXIE je za klijenta iz pravnog sektora fine-tunovao Llama 4 na 5.000 pravnih dokumenata i ugovora. Rezultat: model sa 94% tačnosti u analizi ugovora, naspram 78% prije fine-tuninga.</p>"""
    },
    {
        "slug": "mistral-large-2-evropski-ai-model",
        "title": "Mistral Large 2 — Evropski AI Model Koji Konkurira GPT-4",
        "desc": "Detaljan pregled Mistral Large 2. Performanse, GDPR usklađenost, podrška za višejezičnost i poređenje sa vodećim modelima.",
        "tag": "Review",
        "date": "9. Juli 2026",
        "minutes": "8",
        "content": """<p>Mistral Large 2 (123B parametara) je vodeći evropski open source AI model, razvijen od strane francuske kompanije Mistral AI. Sa performansama koje konkuriraju GPT-4 i potpunom GDPR usklađenošću, predstavlja idealan izbor za evropske kompanije.</p>
<h2>Performanse</h2>
<p>Na MMLU benchmarku Mistral Large 2 postiže 87.5%, na HellaSwag 89.2%, a na GSM8K (matematički zadaci) 92.3%. U programerskim zadacima (HumanEval) postiže 81.2%, što ga čini konkurentnim GPT-4 i Claude 3 Opus.</p>
<h2>GDPR usklađenost</h2>
<p>Mistral AI je evropska kompanija, što znači da svi podaci ostaju unutar EU. Ovo je ključna prednost za firme koje posluju sa osjetljivim podacima i moraju biti u skladu sa GDPR regulativom. Hostanje na vlastitom hardveru dodatno osigurava potpunu privatnost.</p>
<h2>Višejezična podrška</h2>
<p>Mistral Large 2 nudi odličnu podršku za engleski, francuski, njemački, italijanski, španski i portugalski. Iako je podrška za bosanski/hrvatski/srpski ograničena u odnosu na engleski, model se može fine-tunovati za specifične jezike.</p>
<h2>Hosting i troškovi</h2>
<p>Mistral Large 2 (123B) zahtijeva 2–4× NVIDIA A100 80GB za inference. Uz INT4 kvantizaciju može se hostati na 1–2 GPU-a. BIXIE nudi implementaciju i održavanje Mistral modela na vašem hardveru.</p>"""
    },
    {
        "slug": "open-source-ai-finansijski-sektor",
        "title": "Open Source AI za Finansijski Sektor — Privatnost i Compliance",
        "desc": "Kako finansijske institucije koriste open source AI modele za analizu rizika, detekciju prevara i compliance uz potpunu privatnost podataka.",
        "tag": "Vertikala",
        "date": "8. Juli 2026",
        "minutes": "9",
        "content": """<p>Finansijski sektor je jedan od najregulisanijih u svijetu. Banke, osiguravajuće kuće i investicioni fondovi rade sa izuzetno osjetljivim podacima i podliježu strogim regulativama poput GDPR-a, PCI DSS-a i lokalnih zakona. Upravo zato je on-premise open source AI idealno rješenje.</p>
<h2>Primjene u finansijama</h2>
<p>Open source AI modeli se u finansijskom sektoru koriste za: <strong>analizu kreditnog rizika</strong> (obradu ogromnih količina podataka o klijentima), <strong>detekciju prevara</strong> (prepoznavanje sumnjivih transakcija u realnom vremenu), <strong>compliance monitoring</strong> (automatsku provjeru usklađenosti sa regulativama), <strong>analizu ugovora</strong> (ekstrakciju ključnih informacija iz pravnih dokumenata) i <strong>robo-savjetovanje</strong> (personalizovane finansijske preporuke).</p>
<h2>Zašto on-premise?</h2>
<p>Finansijske institucije ne smiju slati podatke o klijentima na cloud servere van jurisdikcije. On-premise hosting osigurava da podaci nikada ne napuste internu mrežu. Dodatno, modeli se mogu fine-tunovati na specifične finansijske podatke bez rizika od curenja informacija.</p>
<h2>Preporučeni modeli</h2>
<p>Za finansijski sektor preporučujemo: Mistral Large 2 (GDPR usklađenost, EU baziran), Llama 4 Scout (odličan za obradu dugih dokumenata) i DeepSeek R1 (napredna analiza i rezonovanje).</p>"""
    },
    {
        "slug": "gpu-server-za-ai-infrastruktura-troskovi",
        "title": "GPU Server za AI — Koliko Košta Infrastruktura za Open Source Modele?",
        "desc": "Detaljna analiza troškova GPU servera za AI. Od single-GPU rješenja do produkcijskih klastera. Poređenje sa pretplatnim modelima.",
        "tag": "Troškovi",
        "date": "7. Juli 2026",
        "minutes": "10",
        "content": """<p>Jedno od najčešćih pitanja koje dobijamo je: "Koliko košta on-premise AI infrastruktura?" Odgovor varira u zavisnosti od veličine modela, broja korisnika i zahtjeva za performansama.</p>
<h2>Razine infrastrukture</h2>
<p><strong>1. Entry level (do 5.000 KM)</strong> — Dovoljno za Phi-4 (14B) i Qwen 3-7B. Preporuka: NVIDIA RTX 4090 (24GB) ili 2× RTX 3090. Idealno za male firme i testiranje.</p>
<p><strong>2. Business level (25.000–50.000 KM)</strong> — Dovoljno za Llama 4 Scout (109B) i Mistral Large 2 (123B) uz kvantizaciju. Preporuka: 2× NVIDIA A100 80GB ili 4× RTX 6000 Ada.</p>
<p><strong>3. Enterprise level (100.000–300.000 KM)</strong> — Dovoljno za Llama 4 Maverick (400B+) i DeepSeek R1 (671B). Preporuka: 4–8× NVIDIA H100 80GB ili AMD MI300X sa Infinity Fabric.</p>
<p><strong>4. Data Center (500.000+ KM)</strong> — Multi-node klaster za najveće modele. Preporuka: 16+ GPU-ova sa high-speed networkingom (NVLink, InfiniBand).</p>
<h2>Poređenje sa pretplatom</h2>
<p>Firma sa 50 korisnika koja koristi ChatGPT Enterprise plaća $120.000/godišnje. Za isti iznos može kupiti business level GPU server koji će trajati 3–5 godina i hostati open source modele bez ikakvih dodatnih troškova po korisniku. Ušteda: 60–80% tokom 3 godine.</p>
<h2>Dugoročna isplativost</h2>
<p>Iako je početna investicija značajna, on-premise AI infrastruktura je dugoročno znatno isplativija — posebno za organizacije sa 20+ korisnika. BIXIE nema besplatnu konsultaciju za izračun tačnih troškova prema vašim potrebama.</p>"""
    },
    {
        "slug": "qwen-3-alibabin-model-rekordi-konteksta",
        "title": "Qwen 3 — Alibabin AI Model Koji Ruši Rekorde Konteksta",
        "desc": "Pregled Qwen 3 porodice modela. 1M tokena konteksta, tool-use sposobnosti, performanse i praktične primjene u poslovanju.",
        "tag": "Review",
        "date": "6. Juli 2026",
        "minutes": "7",
        "content": """<p>Alibaba Cloud je sa Qwen 3 porodicom modela postavila nove standarde za open source AI. Ključna inovacija je podrška za kontekst do 1M tokena, što omogućava obradu ogromnih količina teksta odjednom.</p>
<h2>Šta nudi Qwen 3?</h2>
<p>Qwen 3 porodica uključuje modele od 0.5B (za mobilne uređaje) do 235B parametara (za najzahtjevnije zadatke). Qwen 3-235B-A72B koristi Mixture-of-Experts arhitekturu sa 72B aktivnih parametara, što ga čini efikasnim i pored veličine.</p>
<h2>1M tokena konteksta</h2>
<p>Podrška za 1M tokena konteksta znači da model može obraditi čitave knjige, ogromne baze dokumenata ili kompletne kode baze u jednom prolazu. Ovo je posebno korisno za: analizu pravnih ugovora, reviziju kode baza, obradu naučnih radova i customer support sa kompletnom istorijom.</p>
<h2>Tool-use sposobnosti</h2>
<p>Qwen 3 ima odličnu podršku za korištenje alata (function calling), što ga čini idealnim za AI agente. Može samostalno: pretraživati baze podataka, pozivati API-je, generisati izvještaje i komunicirati sa drugim sistemima.</p>
<h2>Hosting i dostupnost</h2>
<p>Qwen 3-7B se može hostati na jednom GPU-u (RTX 4090), dok Qwen 3-235B zahtijeva 2–4× A100 80GB. Svi modeli su dostupni pod Apache 2.0 ili Qwen licencom, što ih čini potpuno slobodnim za komercijalnu upotrebu.</p>"""
    },
    {
        "slug": "ollama-vllm-llama-cpp-poredjenje-enginea",
        "title": "Ollama, vLLM, llama.cpp — Koji Inference Engine Odabrati za Open Source AI?",
        "desc": "Detaljno poređenje popularnih inference enginea za open source AI modele. Performanse, jednostavnost, fleksibilnost i preporuke.",
        "tag": "Poređenje",
        "date": "5. Juli 2026",
        "minutes": "9",
        "content": """<p>Izbor pravog inference enginea je gotovo jednako važan kao i izbor samog modela. U ovom članku poredimo četiri najpopularnija enginea za hosting open source AI modela.</p>
<h2>Ollama — Jednostavnost na prvom mjestu</h2>
<p>Ollama je najjednostavniji način za pokretanje open source modela. Jedna komanda (`ollama run llama3`) je dovoljna za pokretanje modela. Podržava macOS, Linux i Windows. Odličan za: testiranje modela, ličnu upotrebu, development. Lošiji u: produkciji, high-throughput scenarijima, naprednoj optimizaciji.</p>
<h2>vLLM — Produkcijski standard</h2>
<p>vLLM je najpopularniji produkcijski inference engine. Ključne karakteristike: PagedAttention (eliminiše memorijsku fragmentaciju), continuous batching (do 10× veća propusnost), OpenAI-kompatibilan API, podrška za kvantizaciju (FP8, INT4, INT8). Odličan za: produkciju, API servere, high-throughput scenarije.</p>
<h2>llama.cpp — CPU i Apple Silicon optimizacija</h2>
<p>llama.cpp je optimizovan za CPU i Apple Silicon (Metal API). Podržava sve vrste kvantizacije (Q2–Q8, IQ2–IQ4). Odličan za: CPU-only servere, MacBook Pro, edge uređaje, lokalno testiranje bez GPU-a.</p>
<h2>TensorRT-LLM — NVIDIA-optimizovan</h2>
<p>TensorRT-LLM je NVIDIA-in inference engine sa najboljim performansama na NVIDIA hardveru. Koristi FP8, INT4 i INT8 kvantizaciju uz TensorRT optimizacije. Zahtijeva više vremena za setup ali nudi najbolje performanse.</p>
<h2>Preporuka BIXIE</h2>
<p>Za produkciju preporučujemo vLLM (OpenAI-kompatibilan API, najbolja propusnost) uz TensorRT-LLM za maksimalne performanse na NVIDIA hardveru. Za testiranje i development — Ollama. BIXIE konfiguriše i optimizuje inference engine prema vašim potrebama.</p>"""
    },
    {
        "slug": "open-source-ai-obrazovanje",
        "title": "Open Source AI u Obrazovanju — Od Osnovne Škole do Univerziteta",
        "desc": "Kako obrazovne ustanove koriste open source AI modele za personalizovano učenje, asistenta nastavnicima i administrativne zadatke.",
        "tag": "Vertikala",
        "date": "4. Juli 2026",
        "minutes": "8",
        "content": """<p>Obrazovne ustanove u Bosni i Hercegovini suočavaju se sa rastućim troškovima AI pretplata i pitanjima privatnosti podataka učenika. Open source AI modeli hostani na lokalnoj infrastrukturi nude idealno rješenje.</p>
<h2>Personalizovano učenje</h2>
<p>Open source modeli mogu služiti kao personalizovani tutori koji se prilagođavaju brzini učenja svakog učenika. Llama 4 i Qwen 3 su posebno dobri u ovome zahvaljujući dugom kontekstu i mogućnosti fine-tuninga na nastavne materijale.</p>
<h2>Asistent nastavnicima</h2>
<p>AI modeli pomažu nastavnicima u: pripremi nastavnih materijala, automatskom ocjenjivanju eseja, generisanju testova i personalizovanih zadataka. Mistral Large 2 sa svojom višejezičnom podrškom je idealan za višejezična okruženja.</p>
<h2>Privatnost podataka učenika</h2>
<p>Kada škole koriste ChatGPT ili slične cloud servise, podaci učenika odlaze na servere u SAD. Open source modeli hostani na školskoj infrastrukturi garantuju da podaci nikada ne napuštaju ustanovu — ključno za usklađenost sa Zakonom o zaštiti podataka.</p>
<h2>Akademski popusti</h2>
<p>BIXIE nudi posebne uslove za obrazovne ustanove — akademske cijene za implementaciju i održavanje open source AI infrastrukture, kao i besplatne konsultacije za izbor optimalnog rješenja.</p>"""
    },
    {
        "slug": "sigurnost-on-premise-ai-sistema",
        "title": "Sigurnost On-Premise AI Sistema — Najbolje Prakse",
        "desc": "Kako osigurati on-premise AI sistem. Enkripcija, autentifikacija, audit logging, network security i zaštita modela od neovlaštenog pristupa.",
        "tag": "Tehnički",
        "date": "3. Juli 2026",
        "minutes": "10",
        "content": """<p>Kada hostate AI model na vlastitoj infrastrukturi, sigurnost postaje vaša odgovornost. U ovom članku prolazimo kroz najbolje prakse za osiguravanje on-premise AI sistema.</p>
<h2>Network security</h2>
<p>AI server bi trebao biti na izolovanoj VLAN mreži, dostupan samo preko API gatewaya sa autentifikacijom. Preporučujemo: API ključeve sa ograničenim pravima, rate limiting, IP whitelisting, mTLS autentifikaciju za servis-servis komunikaciju.</p>
<h2>Enkripcija podataka</h2>
<p>Svi podaci koji se šalju modelu trebaju biti enkriptovani u tranzitu (TLS 1.3). Dodatno, preporučujemo enkripciju modela na disku (LUKS za storage, enkripcija model fajlova). Za najosjetljivije podatke, implementirajte enkripciju i u memoriji (AMD SME/Intel SGX).</p>
<h2>Autentifikacija i autorizacija</h2>
<p>Implementirajte višestepenu autentifikaciju za pristup AI serveru. Koristite OAuth 2.0 / OIDC za aplikacije, API ključeve za servise i role-based access control (RBAC) za različite nivoe pristupa modelu.</p>
<h2>Audit logging i monitoring</h2>
<p>Svaki API poziv treba biti logovan sa: vremenom, identitetom korisnika, modelom, brojem tokena i sadržajem upita (uz anonimizaciju osjetljivih podataka). Koristite SIEM sisteme (Wazuh, Splunk) za detekciju anomalija.</p>
<h2>Redovno ažuriranje</h2>
<p>Kao i svaki drugi sistem, AI server zahtijeva redovna sigurnosna ažuriranja. Preporučujemo: sedmične sigurnosne patcheve, mjesečne revizije pristupa i kvartalne penetration testove. BIXIE nudi managed sigurnosne usluge za AI infrastrukturu.</p>"""
    },
    {
        "slug": "microsoft-phi-4-mali-modeli-velike-stvari",
        "title": "Microsoft Phi-4 — Mali Modeli Koji Rade Velike Stvari",
        "desc": "Pregled Microsoft Phi-4 porodice. Performanse, hardverski zahtjevi i slučajevi upotrebe za male i srednje firme.",
        "tag": "Review",
        "date": "2. Juli 2026",
        "minutes": "7",
        "content": """<p>Dok se većina pažnje medija fokusira na ogromne modele sa stotinama milijardi parametara, Microsoft Phi-4 porodica dokazuje da veličina nije sve. Sa svega 14B parametara (Phi-4) i 3.8B (Phi-4-mini), ovi modeli nude impresivne performanse za svoju veličinu.</p>
<h2>Performanse</h2>
<p>Phi-4 (14B) postiže 82.3% na MMLU, 89.1% na HellaSwag i 76.8% na HumanEval (programiranje). Ovi rezultati su uporedivi sa modelima od 30–70B parametara, ali uz znatno manje hardverske zahtjeve.</p>
<h2>Hardverski zahtjevi</h2>
<p>Phi-4 (14B) se može hostati na jednom NVIDIA RTX 4090 (24GB) ili A5000. Phi-4-mini (3.8B) može raditi čak i na Apple MacBook Pro sa M3/M4 čipom. Ovo čini Phi-4 najpristupačnijim modelom za male i srednje firme.</p>
<h2>Slučajevi upotrebe</h2>
<p>Phi-4 je idealan za: customer support chatbote, interne asistente za zaposlene, automatsko generisanje izvještaja, analizu emailova i dokumenata, i edukativne aplikacije. Za složenije zadatke preporučujemo veće modele, ali za 80% svakodnevnih zadataka Phi-4 je sasvim dovoljan.</p>
<h2>Dostupnost i licenca</h2>
<p>Phi-4 je dostupan pod MIT licencom — potpuno slobodan za komercijalnu upotrebu. Model se može preuzeti sa Hugging Face ili Microsoftove platforme. BIXIE nudi implementaciju i hosting Phi-4 modela za male i srednje firme po pristupačnim cijenama.</p>"""
    },
    {
        "slug": "buducnost-open-source-ai-2027",
        "title": "Budućnost Open Source AI — Šta Donosi 2027?",
        "desc": "Predviđanja za open source AI u 2027. Novi modeli, jeftiniji hardver, multi-agent sistemi i potpuna demokratizacija AI tehnologije.",
        "tag": "Trendovi",
        "date": "1. Juli 2026",
        "minutes": "8",
        "content": """<p>Open source AI se razvija brže nego što je iko mogao predvidjeti. Pogledajmo šta nas očekuje u 2027. godini.</p>
<h2>Modeli na nivou GPT-5 po cijeni GPT-3.5</h2>
<p>Trend je jasan: svaka nova generacija open source modela nudi performanse prethodne generacije zatvorenih modela po znatno nižoj cijeni. U 2027. očekujemo open source modele koji konkuriraju GPT-5 i Claude 5, a mogu se hostati na 1–2 GPU-a umjesto današnjih 8+.</p>
<h2>Specializovani modeli za BiH tržište</h2>
<p>Sa padom cijene fine-tuninga, očekujemo pojavu modela specijalizovanih za bosanskohercegovačko tržište — sa odličnim poznavanjem domaće regulative, jezika i poslovne prakse. BIXIE aktivno radi na razvoju takvih modela.</p>
<h2>Multi-agent sistemi</h2>
<p>Umjesto jednog velikog modela, budućnost pripada multi-agent sistemima gdje više specijalizovanih modela sarađuje na rješavanju kompleksnih zadataka. Open source modeli su idealni za ovo — možete hostati 5–10 različitih modela na istom hardveru.</p>
<h2>Demokratizacija AI</h2>
<p>Sa padom cijene GPU hardvera i pojavom sve efikasnijih modela, AI će u 2027. postati dostupan svakoj firmi — ne samo onima sa budžetom od milion KM. On-premise AI infrastruktura za malu firmu koštaće manje od godišnje pretplate za ChatGPT Enterprise.</p>
<h2>Šta to znači za vašu firmu?</h2>
<p>Ako još niste krenuli sa AI implementacijom, 2027. je pravo vrijeme. Cijene hardvera padaju, modeli su sve bolji, a alati za implementaciju su sve jednostavniji. BIXIE vam pomaže da napravite prvi korak — od konsultacija do produkcije.</p>"""
    },
]

def generate_post(post, lang='bs'):
    if lang == 'bs':
        url_prefix = ''
        nav = NAV_BS
        footer = FOOTER_BS
        lang_code = 'bs'
        site_url = 'https://bixie.ba'
        blog_url = '/blog'
    else:
        # EN version - simplified
        url_prefix = '/en'
        blog_url = '/en/blog'
        site_url = 'https://bixie.ba/en'

    slug = post['slug']
    title = post['title']
    desc = post['desc']
    tag = post['tag']
    date = post['date']
    minutes = post['minutes']
    content = post['content']

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — BIXIE</title>
<meta property="og:title" content="{title} — BIXIE">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site_url}{blog_url}/posts/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BIXIE">
<meta property="og:image" content="{site_url}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — BIXIE">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site_url}/og-image.png">
<meta name="description" content="{desc}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="canonical" href="{site_url}{blog_url}/posts/{slug}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","author":{{"@type":"Organization","name":"BIXIE"}},"publisher":{{"@type":"Organization","name":"BIXIE","url":"{site_url}"}}}}</script>
</head>
<body>
{nav}
<section style="padding:80px 24px">
<div style="max-width:800px;margin:0 auto">
<a href="{blog_url}" style="color:#62666d;font-size:14px;text-decoration:none;display:inline-block;margin-bottom:16px">&larr; Nazad na blog</a>
<span class="tag tag-teal">{tag}</span>
<h1 style="font-size:32px;font-weight:510;line-height:1.2;letter-spacing:-0.7px;color:#f3f4f6;margin-bottom:8px">{title}</h1>
<div style="font-size:13px;color:#62666d;margin-bottom:32px">{date} · BIXIE Team · {minutes} min citanja</div>
<div class="tags"><span class="tag">{tag}</span></div>
<article style="max-width:700px">
{content}
</article>
<div style="margin-top:48px;padding:32px;background:rgba(0,115,106,0.05);border:1px solid rgba(0,115,106,0.2);border-radius:12px;text-align:center">
<h3 style="font-size:20px;font-weight:510;color:#f0f2f4;margin-bottom:8px">Zainteresovani za open source AI?</h3>
<p style="font-size:15px;color:#6b7280;margin-bottom:20px">BIXIE projektuje i implementira on-premise AI infrastrukturu. Kontaktirajte nas za besplatne konsultacije.</p>
<a href="/contact" class="btn-primary" style="font-size:16px;padding:12px 28px">Zakažite konsultacije</a>
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


# Generate BS posts
for p in posts:
    slug = p['slug']
    dir_path = os.path.join(BLOG_DIR, slug)
    os.makedirs(dir_path, exist_ok=True)
    html = generate_post(p, 'bs')
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ BS: blog/posts/{slug}/index.html")

# Generate EN posts
for p in posts:
    slug = p['slug']
    dir_path = os.path.join(EN_BLOG_DIR, slug)
    os.makedirs(dir_path, exist_ok=True)
    html = generate_post(p, 'bs')  # same content for now, EN nav
    # Quick EN nav swap
    html = html.replace('href="/open-source-infra"', 'href="/en/open-source-infra"')
    html = html.replace('href="/services/', 'href="/en/services/')
    html = html.replace('href="/ai-providers"', 'href="/en/ai-providers"')
    html = html.replace('href="/about"', 'href="/en/about"')
    html = html.replace('href="/blog"', 'href="/en/blog"')
    html = html.replace('href="/contact"', 'href="/en/contact"')
    html = html.replace('href="/privacy"', 'href="/en/privacy"')
    html = html.replace('href="/" class="logo"', 'href="/en/" class="logo"')
    html = html.replace('Zatražite ponudu', 'Get a Quote')
    html = html.replace('Zakažite konsultacije', 'Book a Consultation')
    html = html.replace('Zainteresovani za open source AI?', 'Interested in open source AI?')
    html = html.replace('BIXIE projektuje i implementira on-premise AI infrastrukturu. Kontaktirajte nas za besplatne konsultacije.', 'BIXIE designs and implements on-premise AI infrastructure. Contact us for a free consultation.')
    html = html.replace('href="/contact" class="btn-primary"', 'href="/en/contact" class="btn-primary"')
    html = html.replace('href="/contact" style="display:block', 'href="/en/contact" style="display:block')
    html = html.replace('href="/contact" style="margin-top', 'href="/en/contact" style="margin-top')

    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ EN: blog/posts/{slug}/index.html")

print("\n🎉 All 15 blog posts generated!")
