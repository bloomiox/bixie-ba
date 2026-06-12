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
};

export function getBlogPost(slug: string): BlogPost | undefined {
  return blogPosts[slug];
}

export function getAllBlogPosts(): BlogPost[] {
  return Object.values(blogPosts).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}

export default blogPosts;
