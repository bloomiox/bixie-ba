export interface BlogPost {
  slug: string;
  title: string;
  excerpt: string;
  category: string;
  date: string;
  readTime: string;
  content?: string;
}

const blogPosts: Record<string, BlogPost> = {
  '10-primjena-ai-agenta-male-firme': {
    slug: '10-primjena-ai-agenta-male-firme',
    title: '10 primjena AI agenata u malim firmama',
    excerpt: 'Praktični primjeri kako male firme mogu koristiti AI agente za automatizaciju, povećanje prodaje i smanjenje troškova.',
    category: 'AI Agenti',
    date: '2025-03-15',
    readTime: '8 min',
  },
  'agentic-ai-autonomni-agenti': {
    slug: 'agentic-ai-autonomni-agenti',
    title: 'Agentic AI: Šta su autonomni AI agenti i kako rade?',
    excerpt: 'Agentic AI predstavlja novu generaciju AI sistema koji samostalno planiraju, odlučuju i izvršavaju zadatke bez ljudske intervencije.',
    category: 'AI Tehnologija',
    date: '2025-02-20',
    readTime: '10 min',
  },
  'agentic-ai-finansijski-sektor': {
    slug: 'agentic-ai-finansijski-sektor',
    title: 'Agentic AI u finansijskom sektoru: Primjene i prednosti',
    excerpt: 'Kako autonomni AI sistemi transformišu bankarstvo, osiguranje i finansijske usluge kroz automatizaciju i analizu.',
    category: 'AI Tehnologija',
    date: '2025-04-10',
    readTime: '9 min',
  },
  'agentic-ai-vodic-pocetnici': {
    slug: 'agentic-ai-vodic-pocetnici',
    title: 'Agentic AI: Vodič za početnike',
    excerpt: 'Sve što trebate znati o agentic AI — od osnovnih koncepata do praktične primjene u biznisu.',
    category: 'AI Tehnologija',
    date: '2025-01-10',
    readTime: '12 min',
  },
  'ai-agenti-automatizacija-marketinga': {
    slug: 'ai-agenti-automatizacija-marketinga',
    title: 'AI agenti za automatizaciju marketinga',
    excerpt: 'Kako AI agenti transformišu digitalni marketing kroz personalizaciju, automatizaciju kampanja i analizu podataka.',
    category: 'Marketing',
    date: '2025-03-28',
    readTime: '7 min',
  },
  'ai-agenti-customer-support': {
    slug: 'ai-agenti-customer-support',
    title: 'AI agenti u customer supportu',
    excerpt: 'Implementacija AI agenata za korisničku podršku — smanjenje troškova, povećanje zadovoljstva i 24/7 dostupnost.',
    category: 'Customer Support',
    date: '2025-04-05',
    readTime: '8 min',
  },
  'ai-agenti-gdpr-sta-morate-znati': {
    slug: 'ai-agenti-gdpr-sta-morate-znati',
    title: 'AI agenti i GDPR: Šta morate znati',
    excerpt: 'GDPR compliance kod implementacije AI agenata — obrada podataka, privatnost, i pravni okvir u EU i BiH.',
    category: 'Pravna pitanja',
    date: '2025-05-01',
    readTime: '9 min',
  },
  'ai-agenti-lead-generation': {
    slug: 'ai-agenti-lead-generation',
    title: 'AI agenti za lead generation',
    excerpt: 'Automatsko pronalaženje, kvalifikacija i angažman potencijalnih klijenata pomoću AI agenata.',
    category: 'Prodaja',
    date: '2025-04-18',
    readTime: '7 min',
  },
  'ai-agenti-ljudski-resursi': {
    slug: 'ai-agenti-ljudski-resursi',
    title: 'AI agenti u ljudskim resursima',
    excerpt: 'Kako AI transformiše HR — selekcija kandidata, onboarding, upravljanje performansama i razvoj zaposlenika.',
    category: 'HR',
    date: '2025-05-15',
    readTime: '8 min',
  },
  'ai-agenti-transformisu-prodaju': {
    slug: 'ai-agenti-transformisu-prodaju',
    title: 'Kako AI agenti transformišu prodaju',
    excerpt: 'AI agenti u prodaji — od kvalifikacije leadova do automatskog follow-upa i predikcije zatvaranja.',
    category: 'Prodaja',
    date: '2025-02-28',
    readTime: '9 min',
  },
  'ai-agenti-upravljanje-znanjem': {
    slug: 'ai-agenti-upravljanje-znanjem',
    title: 'AI agenti za upravljanje znanjem',
    excerpt: 'Organizacija, pretraga i distribucija znanja unutar organizacije pomoću AI agenata.',
    category: 'AI Tehnologija',
    date: '2025-06-01',
    readTime: '7 min',
  },
  'ai-agenti-vs-tradicionalni-chatbotovi': {
    slug: 'ai-agenti-vs-tradicionalni-chatbotovi',
    title: 'AI agenti vs tradicionalni chatbotovi',
    excerpt: 'Ključne razlike između AI agenata i klasičnih chatbotova — zašto je AI agent bolji izbor za vaš biznis.',
    category: 'AI Tehnologija',
    date: '2025-01-25',
    readTime: '6 min',
  },
  'implementirati-ai-agente-4-sedmice': {
    slug: 'implementirati-ai-agente-4-sedmice',
    title: 'Kako implementirati AI agente u 4 sedmice',
    excerpt: 'Praktični roadmap za implementaciju AI agenata u vašoj firmi — od identifikacije use case-a do produkcije.',
    category: 'Vodiči',
    date: '2025-05-20',
    readTime: '10 min',
  },
  'odabrati-pravog-ai-agenta': {
    slug: 'odabrati-pravog-ai-agenta',
    title: 'Kako odabrati pravog AI agenta za vaš biznis',
    excerpt: 'Kriteriji za odabir AI agenata — cijena, performanse, sigurnost i kompatibilnost sa postojećim sistemima.',
    category: 'Vodiči',
    date: '2025-04-22',
    readTime: '8 min',
  },
  'signali-da-treba-ai-agente': {
    slug: 'signali-da-treba-ai-agente',
    title: 'Signali da vašoj firmi trebaju AI agenti',
    excerpt: 'Prepoznajte znakove da je vrijeme za implementaciju AI agenata — ponavljajući zadaci, preopterećenje tima i propuštene prilike.',
    category: 'AI Tehnologija',
    date: '2025-03-05',
    readTime: '6 min',
  },
  'buducnost-rada-ljudi-ai-agenti': {
    slug: 'buducnost-rada-ljudi-ai-agenti',
    title: 'Budućnost rada: Ljudi i AI agenti',
    excerpt: 'Kako će AI agenti promijeniti način na koji radimo — nove uloge, vještine i prilike u eri AI saradnje.',
    category: 'Trendovi',
    date: '2025-06-10',
    readTime: '9 min',
  },
  'multi-agent-sistemi-kako-rade-zajedno': {
    slug: 'multi-agent-sistemi-kako-rade-zajedno',
    title: 'Multi-agent sistemi: Kako AI agenti rade zajedno',
    excerpt: 'Kako više AI agenata saradjuje na kompleksnim zadacima — arhitektura, komunikacija i koordinacija multi-agent sistema.',
    category: 'AI Tehnologija',
    date: '2025-05-28',
    readTime: '11 min',
  },
  'automatizacija-korisnicke-podrske-ai': {
    slug: 'automatizacija-korisnicke-podrske-ai',
    title: 'Automatizacija korisničke podrške pomoću AI',
    excerpt: 'Vodič kroz automatizaciju customer supporta — od chatbotova do naprednih AI agenata koji uče iz svake interakcije.',
    category: 'Automatizacija',
    date: '2025-02-10',
    readTime: '8 min',
  },
  'bitrix24-crm-implementacija-vodic': {
    slug: 'bitrix24-crm-implementacija-vodic',
    title: 'Bitrix24 CRM implementacija: Kompletan vodič',
    excerpt: 'Korak po korak vodič za implementaciju Bitrix24 CRM-a u vašoj firmi — od podešavanja do optimizacije.',
    category: 'CRM',
    date: '2025-01-05',
    readTime: '14 min',
  },
  'bitrix24-vs-ai-crm': {
    slug: 'bitrix24-vs-ai-crm',
    title: 'Bitrix24 vs AI CRM: Poređenje',
    excerpt: 'Poređenje tradicionalnog Bitrix24 CRM-a sa modernim AI CRM rješenjima — prednosti, mane i preporuke.',
    category: 'CRM',
    date: '2025-04-30',
    readTime: '9 min',
  },
  'case-study-automatizacija-onboardinga': {
    slug: 'case-study-automatizacija-onboardinga',
    title: 'Case Study: Automatizacija onboarding procesa',
    excerpt: 'Kako smo IT firmi smanjili onboarding sa 2 sedmice na 2 dana kroz AI automatizaciju.',
    category: 'Case Study',
    date: '2025-02-15',
    readTime: '5 min',
  },
  'case-study-etrgovina-povecala-prodaju-40': {
    slug: 'case-study-etrgovina-povecala-prodaju-40',
    title: 'Case Study: E-trgovina povećala prodaju za 40%',
    excerpt: 'Kako je implementacija AI preporuka i automatizacije email marketinga donijela 40% više prodaje.',
    category: 'Case Study',
    date: '2025-03-20',
    readTime: '5 min',
  },
  'case-study-it-firma-smanjila-troskove-60': {
    slug: 'case-study-it-firma-smanjila-troskove-60',
    title: 'Case Study: IT firma smanjila troškove supporta za 60%',
    excerpt: 'AI customer support agent koji rješava 70% upita automatski — rezultat: 60% manji troškovi, veće zadovoljstvo.',
    category: 'Case Study',
    date: '2025-04-25',
    readTime: '6 min',
  },
  'case-study-startup-ustedio-10000-km': {
    slug: 'case-study-startup-ustedio-10000-km',
    title: 'Case Study: Startup uštedio 10,000 KM mjesečno',
    excerpt: 'RPA automatizacija finansijskih procesa — fakturisanje, usaglašavanje i izvještaji potpuno automatizovani.',
    category: 'Case Study',
    date: '2025-05-10',
    readTime: '5 min',
  },
  'ai-licence-obrazovne-ustanove': {
    slug: 'ai-licence-obrazovne-ustanove',
    title: 'AI licence za obrazovne ustanove u bosni i hercegovini',
    excerpt: 'kompletan vodič za nabavku AI licenci za univerzitete, fakultete i škole u BiH. ChatGPT Edu, Google Workspace for Education, Microsoft 365 Education — cijene i popusti.',
    category: 'AI Licence',
    date: '2026-06-03',
    readTime: '8 min',
    content: `<p>Obrazovne ustanove u Bosni i Hercegovini sve više prepoznaju potrebu za implementacijom AI alata u nastavni i administrativni rad. Od univerziteta do srednjih škola, potražnja za ChatGPT-jem, Google Workspaceom i AI alatima raste. Međutim, nabavka ovih licenci za obrazovne institucije nosi specifičnosti koje je važno razumjeti — od akademskih popusta do usklađenosti sa zakonima o javnim nabavkama.</p>
<p>U ovom vodiču ćemo proći kroz sve dostupne AI licence za obrazovanje u BiH, akademske popuste, proces nabavke i praktične savjete za implementaciju.</p>
<h2>Zašto obrazovne ustanove trebaju AI licence?</h2>
<p>AI alati donose revolucionarne promjene u obrazovanju — od automatizacije administrativnih poslova do personaliziranog učenja. Univerziteti u BiH mogu iskoristiti AI za:</p>
<ul>
<li><strong>Automatizaciju administracije</strong> — prijava ispita, obrada zahtjeva, komunikacija sa studentima putem AI chatbota</li>
<li><strong>Asistente za nastavnike</strong> — priprema nastavnih materijala, automatsko ocjenjivanje, analiza napretka studenata</li>
<li><strong>AI asistente za studente</strong> — pomoć pri učenju, istraživanju literature, pisanju radova i pripremi za ispite</li>
<li><strong>Analizu podataka</strong> — budžetsko planiranje, demografske analize, izvještaji za akreditaciju</li>
<li><strong>Istraživanje</strong> — analiza naučnih radova, generisanje hipoteza, obrada eksperimentalnih podataka</li>
</ul>
<h2>Pravni okvir za nabavku AI licenci u BiH</h2>
<p>Kada obrazovna ustanova u BiH nabavlja AI licence, važno je razumjeti pravni okvir. Pošto se radi o uvozu digitalnih usluga (SaaS), primjenjuje se mehanizam obrnutog oporezivanja (reverse charge) kroz mjesečnu PDV prijavu.</p>
<h2>Dostupne AI licence za obrazovne ustanove</h2>
<h3>1. ChatGPT Edu (OpenAI)</h3>
<p>OpenAI je lansirao ChatGPT Edu — poseban plan za univerzitete koji uključuje pristup GPT-4 i GPT-4o modelima, veće limite poruka, mogućnost kreiranja custom GPT-ova, DAPRA za GDPR usklađenost i studentsku privatnost.</p>
<h3>2. Google Workspace for Education</h3>
<p>Google nudi četiri nivoa za obrazovne institucije: besplatni Fundamentals (Gmail, Drive, Classroom), Standard (dodatne sigurnosne opcije), Teaching and Learning Upgrade (Meet do 250 učesnika) i Education Plus (potpuni paket sa Gemini AI).</p>
<h3>3. Microsoft 365 Education</h3>
<p>Microsoft ima tri nivoa: A1 (besplatan web Office), A3 (desktop Office) i A5 (potpuni paket sa AI). Microsoft Copilot za obrazovanje donosi AI asistenciju direktno u Office alate.</p>
<h3>4. Canva za Obrazovanje</h3>
<p>Canva for Education je potpuno besplatan za K-12 škole, dok Canva Campus ima posebnu cijenu za univerzitete.</p>
<h2>Proces nabavke za obrazovne ustanove u BiH</h2>
<p>Obrazovne ustanove prolaze kroz proces javnih nabavki: identifikacija potreba, zahtjev za ponudu, pribavljanje 3+ ponude, izbor najpovoljnije, implementacija i obuka.</p>
<h2>Kako BIXIE može pomoći?</h2>
<p>BIXIE je official provider i reseller za OpenAI, Google, Microsoft i Canva. Nudimo jedinstvenu ponudu — sve licence na jednom mjestu, implementaciju, podršku na bosanskom jeziku, pomoć pri tenderskoj dokumentaciji i edukacijske popuste.</p>
<h2>Poređenje cijena: Akademske vs Komercijalne licence</h2>
<p>ChatGPT Edu 28 KM/mj vs Team 70 KM/mj (ušteda 60%), Google Gemini Education 18 KM/mj vs Business 60 KM/mj (ušteda 70%), Claude Edu 48 KM/mj vs Team 80 KM/mj (ušteda 40%).</p>
<h2>Zaključak</h2>
<p>AI licence za obrazovne ustanove u BiH su dostupne po akademskim cijenama koje su 40-70% niže od komercijalnih. BIXIE nudi kompletnu uslugu — od savjetovanja i nabavke do implementacije i obuke.</p>`,
  },
  'monday-crm-produktivnost': {
    slug: 'monday-crm-produktivnost',
    title: 'Monday.com CRM: produktivnost timova',
    excerpt: 'monday.com CRM za povećanje produktivnosti timova. Automatizacije, integracije, prednosti za BiH firme i preduzeća.',
    category: 'Monday.com',
    date: '2026-04-20',
    readTime: '10 min',
    content: `<h2>Monday.com — više od CRM-a</h2>
<p>Monday.com je jedan od najintuitivnijih CRM sistema na tržištu, poznat po izuzetno jednostavnom korisničkom interfejsu i vizuelnom prikazu podataka. Nudi vizuelne pipeline-e u kanban i tabla formatu, automatske radne tokove bez kodiranja, integraciju sa Gmail-om, Slack-om i Teams-om, napredne dashboard-e i odlične mobilne aplikacije.</p>
<h2>Zašto Monday.com za BiH firme?</h2>
<p>Idealni kandidati su: IT firme i startupi koji već koriste Monday za projekte, agencije koje žele povezati projektni menadžment sa prodajom, konsultantske kuće i firme sa međunarodnim timovima.</p>
<h2>Implementacija Monday.com CRM-a</h2>
<p>BIXIE radi kompletnu implementaciju u roku 1-2 sedmice: postavka pipeline-a, migracija podataka, kreiranje automatizacija, integracija sa alatima, obuka tima.</p>
<h2>Monday AI — pametne funkcionalnosti</h2>
<p>Automatsko sumiranje emailova, predlozi za odgovore, automatsko kreiranje zadataka, preporuke za optimizaciju radnih tokova i automatsko generisanje izvještaja.</p>
<h2>ROI i rezultati</h2>
<p>Povećanje produktivnosti tima za 35%, smanjenje vremena za sastanke za 40%, brže zatvaranje dealova za 25%.</p>
<h2>Monday.com za različite industrije</h2>
<p>IT, marketinške agencije, kreativne industrije, konsultantske firme, neprofitne organizacije — za svaku industriju postoje gotovi šabloni.</p>
<h2>Kada Monday.com nije pravi izbor?</h2>
<p>Ako imate više od 50 korisnika, trebate ugrađenu VoIP telefoniju sa lokalnim operaterima, naprednu automatizaciju marketinga ili offline rad — Bitrix24 ili Zoho su bolji izbori.</p>
<h2>Zaključak</h2>
<p>Monday.com CRM je odličan za firme koje cijene vizuelni prikaz, brzu implementaciju i jednostavnost. Cijene od $12/sjedištu. BIXIE nudi besplatne konsultacije i demonstraciju.</p>`,
  },
  'rpa-automatizacija-procesa': {
    slug: 'rpa-automatizacija-procesa',
    title: 'RPA i AI automatizacija: kompletan vodič za 2026',
    excerpt: 'Kako automatizirati poslovne procese kombinacijom RPA i AI agenata. Praktični primjeri i uštede do 70% za BiH firme.',
    category: 'RPA',
    date: '2026-05-28',
    readTime: '9 min',
    content: `<h2>Šta je RPA?</h2>
<p>RPA (Robotic Process Automation) je tehnologija koja koristi softverske botove za automatsko izvršavanje repetitivnih zadataka — kliktanje, kucanje, kopiranje podataka iz jednog sistema u drugi.</p>
<h2>RPA vs AI Agenti</h2>
<p>RPA slijedi pravila, AI donosi odluke. RPA botovi su brzi za implementaciju (1-2 sedmice) i niži troškovi, dok AI agenti zahtijevaju 2-6 sedmica ali donose veći ROI.</p>
<h2>Kombinacija RPA + AI = Intelligent Automation</h2>
<p>Najbolji rezultati: RPA botovi rade grube zadatke (prikupljanje podataka, unos), AI agenti donose odluke i komuniciraju sa korisnicima.</p>
<h2>Proces implementacije</h2>
<ol>
<li><strong>Audit procesa</strong> — identifikacija zadataka za automatizaciju (1 sedmica)</li>
<li><strong>Izbor tehnologije</strong> — RPA, AI ili kombinacija</li>
<li><strong>Razvoj i testiranje</strong> — izrada bota i/ili AI agenta (2-4 sedmice)</li>
<li><strong>Integracija</strong> — povezivanje sa postojećim sistemima</li>
<li><strong>Obuka i monitoring</strong> — obuka tima i postavljanje nadzora</li>
</ol>
<h2>ROI: Šta možete očekivati?</h2>
<ul>
<li>Ušteda vremena: 50-70% na automatiziranim zadacima</li>
<li>Smanjenje grešaka: do 99%</li>
<li>Brži odgovor kupcima: AI agenti odgovaraju u sekundi</li>
<li>Pokrivenost 24/7</li>
<li>ROI u roku 3-6 mjeseci</li>
</ul>
<h2>Zaključak</h2>
<p>RPA i AI automatizacija nisu samo za velike kompanije. Uz BIXIE, i male i srednje firme u BiH mogu automatizirati ključne procese uz povrat investicije u roku nekoliko mjeseci.</p>`,
  },
  'salesforce-crm-implementacija': {
    slug: 'salesforce-crm-implementacija',
    title: 'Salesforce za srednje kompanije u bih',
    excerpt: 'Salesforce za srednje kompanije u BiH. Cijene, implementacija, Einstein AI, migracija. Da li je Salesforce pravi izbor za vašu firmu?',
    category: 'Salesforce',
    date: '2026-04-28',
    readTime: '12 min',
    content: `<h2>Salesforce za srednje kompanije: mitovi i realnost</h2>
<p>Salesforce se često percipira kao CRM za velike korporacije, ali danas nudi opcije i za srednje kompanije. Ključ je u odabiru pravog plana i partnera.</p>
<h2>Salesforce planovi — detaljan pregled</h2>
<p>Starter ($25/korisnik), Professional ($80/korisnik), Enterprise ($165/korisnik), Unlimited ($330/korisnik). Za srednje kompanije preporučujemo Professional ili Enterprise plan.</p>
<h2>Einstein AI — ugrađeni asistent</h2>
<p>Prediktivni scoring leadova sa preciznošću preko 85%, preporuke za akcije, automatska obrada emailova, analiza sentimenta, automatsko otkrivanje duplikata.</p>
<h2>Migracija na Salesforce</h2>
<p>BIXIE radi kompletnu migraciju: analiza podataka, mapiranje na Salesforce model, čišćenje duplikata, migracija istorije, validacija, obuka i go-live. Prosječno trajanje: 4-8 sedmica.</p>
<h2>Implementacija u BiH — specifičnosti</h2>
<p>Viševalutno poslovanje (KM, EUR, CHF), PDV obračun po bh. zakonodavstvu, fakture na BHS jeziku, integracija sa lokalnim bankama, podrška na bosanskom.</p>
<h2>ROI analiza za srednje kompanije</h2>
<p>Povećanje prodajne produktivnosti 25-35%, smanjenje vremena za izvještavanje 70%, povećanje konverzije 20-30%, prosječni ROI 4.5x u prve dvije godine.</p>
<h2>Zaključak</h2>
<p>Salesforce je strateška investicija za firme sa 15+ prodajnih agenata koje planiraju rast. BIXIE nudi besplatne konsultacije i demonstraciju.</p>`,
  },
  'zoho-crm-implementacija': {
    slug: 'zoho-crm-implementacija',
    title: 'Zoho CRM: kompletan vodič za implementaciju u 2026',
    excerpt: 'Kako implementirati Zoho CRM u vašoj firmi. Zoho CRM prednosti, cijene, integracije. Vodič za BiH firme i preduzeća.',
    category: 'Zoho CRM',
    date: '2026-05-05',
    readTime: '12 min',
    content: `<h2>Zašto Zoho CRM?</h2>
<p>Zoho CRM ima preko 250.000 klijenata u 180 zemalja. Početni plan od $14/korisnik/mjesečno, ugrađeni AI asistent Zia, napredna automatizacija, ugrađena telefonija i 800+ integracija.</p>
<h2>Zoho CRM planovi i cijene</h2>
<p>Standard (Free — do 3 korisnika), Professional ($14/korisnik), Enterprise ($23/korisnik), Ultimate ($35/korisnik). Popust 15-20% na godišnje ugovore.</p>
<h2>Zia AI — vaš pametni asistent</h2>
<p>Predviđanje vjerovatnoće zatvaranja deala (80%+ preciznost), preporuke za akcije, automatsko čišćenje duplikata, analiza sentimenta, glasovne komande.</p>
<h2>Implementacija Zoho CRM u 5 koraka</h2>
<ol>
<li><strong>Postavka organizacije</strong> — profili, uloge, dozvole</li>
<li><strong>Import podataka</strong> — migracija iz Excel, Google Sheets, drugih CRM-ova</li>
<li><strong>Custom moduli</strong> — prilagođena polja, pipeline-i, izvještaji</li>
<li><strong>Automatizacija</strong> — radni tokovi, email šabloni, assignment pravila</li>
<li><strong>Integracija</strong> — Zoho Books, Gmail, društvene mreže, web shop, VoIP</li>
</ol>
<h2>Zoho za BiH firme</h2>
<p>Podrška za više valuta (KM, EUR, CHF), interfejs na hrvatskom/srpskom, cloud rješenje bez infrastrukture, integracija sa Google Workspace i Microsoft 365.</p>
<h2>Zaključak</h2>
<p>Zoho CRM je najbolji izbor za firme koje traže moćan CRM po pristupačnoj cijeni, sa naprednim AI funkcionalnostima. BIXIE nudi besplatne konsultacije, demonstraciju i 14-dnevni probni period.</p>`,
  },
};

export function getBlogPost(slug: string): BlogPost | undefined {
  return blogPosts[slug];
}

export function getAllBlogPosts(): BlogPost[] {
  return Object.values(blogPosts).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}

export default blogPosts;
