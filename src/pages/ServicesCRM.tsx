import { Link, useLocation } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

export default function ServicesCRM() {
  const { t } = useTranslation()
  const location = useLocation()
  const lang = location.pathname.startsWith('/en') ? 'en' : location.pathname.startsWith('/de') ? 'de' : 'bs'
  const l = (p: string) => (lang === 'bs' ? p : `/${lang}${p}`)

  const platforms = [
    {
      name: 'Bitrix24', badge: 'Official Partner', desc: 'Kompletan CRM sa ugrađenom telefonijom, HR modulima, email marketingom i disk prostorom. Od besplatnog plana do enterprise rješenja.',
      features: ['CRM + Kolaboracija', 'On-premise i Cloud', 'Telefonija', 'HR Moduli'],
    },
    {
      name: 'Zoho CRM', badge: 'Partner', desc: 'Zoho CRM sa AI asistentom Zia. Automatsko bodovanje leadova, predviđanje prodaje i napredna analitika. Integracija sa 50+ aplikacija.',
      features: ['AI Asistent Zia', 'Omnikanalna podrška', 'Workflow Automatizacija'],
    },
    {
      name: 'Monday.com', badge: 'Partner', desc: 'Monday.com sa vizuelnim pipeline-om i AI automatizacijama. Idealno za timove koji žele brzu implementaciju i intuitivno sučelje.',
      features: ['Vizuelni Pipeline', 'AI Automatizacije', 'Integracije'],
    },
    {
      name: 'Salesforce', badge: 'Partner', desc: 'Salesforce sa Einstein AI. Enterprise CRM za srednje i velike firme. Migracija sa drugih sistema i custom razvoj.',
      features: ['Einstein AI', 'Enterprise', 'Migracija'],
    },
    {
      name: 'Pipedrive', badge: 'Partner', desc: 'Pipedrive fokusiran na prodaju. Intuitivan pipeline menadžment, automatizacija follow-upa i AI predviđanje prodaje.',
      features: ['Sales Pipeline', 'AI Predictions', 'Automatizacija'],
    },
    {
      name: 'HubSpot', badge: 'Partner', desc: 'HubSpot sa besplatnim planom i AI alatima za marketing, prodaju i customer service. Breeze AI za automatizaciju.',
      features: ['Free CRM', 'Breeze AI', 'Marketing Hub'],
    },
    {
      name: 'SugarCRM', badge: '', desc: 'SugarCRM sa inteligentnim automatskim workflow-om i naprednom analitikom. Potpuna kontrola nad prodajnim procesom.',
      features: ['Intelligent Workflow', 'Analytics', 'Automation'],
    },
    {
      name: 'Microsoft Dynamics 365', badge: '', desc: 'Microsoft Dynamics 365 sa AI Copilot integracijom. Kompletno poslovno rješenje koje povezuje CRM i ERP.',
      features: ['AI Copilot', 'CRM + ERP', 'Microsoft Ecosystem'],
    },
  ]

  const relatedPosts = [
    { slug: 'bitrix24-crm-implementacija-vodic', title: 'Bitrix24 CRM implementacija: Kompletan vodič' },
    { slug: 'bitrix24-vs-ai-crm', title: 'Bitrix24 vs AI-Powered CRM: Poređenje' },
    { slug: 'bitrix24-vs-zoho-crm-poredjenje', title: 'Bitrix24 vs Zoho CRM: Detaljno poređenje' },
    { slug: 'zoho-crm-implementacija', title: 'Zoho CRM: Kompletan vodič za implementaciju' },
    { slug: 'vodic-odabir-crm-sistema-2026', title: 'Vodič za odabir CRM sistema u 2026' },
    { slug: 'najbolji-crm-nekretnine-bih', title: 'Najbolji CRM za nekretnine u BiH' },
    { slug: 'najbolji-crm-ugostiteljstvo-bih', title: 'Najbolji CRM za ugostiteljstvo u BiH' },
    { slug: 'open-source-crm-suitecrm-espo-bih', title: 'Open source CRM rješenja: SuiteCRM i EspoCRM' },
    { slug: 'hubspot-crm-implementacija-bih', title: 'HubSpot CRM: Vodič za implementaciju u BiH' },
    { slug: 'pipedrive-crm-male-firme-bih', title: 'Pipedrive CRM za male firme u BiH' },
    { slug: 'migracija-bitrix24-zoho-crm', title: 'Kako migrirati sa Bitrix24 na Zoho CRM' },
    { slug: 'crm-automatizacija-ustedite-20-sati', title: 'CRM automatizacija: Uštedite 20 sati rada sedmično' },
    { slug: 'salesforce-crm-implementacija', title: 'Salesforce za srednje kompanije u BiH' },
    { slug: 'monday-crm-produktivnost', title: 'Monday.com CRM: Produktivnost timova' },
  ]

  return (
    <div className="max-w-6xl mx-auto px-4 py-20">
      {/* Hero */}
      <div className="mb-16">
        <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Usluge</span>
        <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">CRM Implementacija</h1>
        <p className="text-lg text-muted max-w-2xl">
          Implementacija, migracija i optimizacija CRM sistema. Official Bitrix24 partner za Bosnu i Hercegovinu. 
          Pomažemo firmama da odaberu, implementiraju i maksimalno iskoriste CRM rješenje koje odgovara njihovim potrebama.
        </p>
      </div>

      {/* Why CRM */}
      <section className="mb-16">
        <h2 className="text-2xl font-bold text-white mb-4">Zašto je CRM ključan za vašu firmu?</h2>
        <div className="grid md:grid-cols-3 gap-4">
          {[
            { stat: '30-45%', desc: 'Povećanje produktivnosti prodajnog tima' },
            { stat: '25-35%', desc: 'Veća stopa konverzije leadova' },
            { stat: '3-6 mj', desc: 'Prosječan ROI od CRM implementacije' },
          ].map((s, i) => (
            <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 text-center">
              <div className="text-3xl font-bold gradient-text mb-2">{s.stat}</div>
              <p className="text-sm text-muted">{s.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CRM Platforms Grid */}
      <section className="mb-16">
        <h2 className="text-2xl font-bold text-white mb-8">CRM platforme koje implementiramo</h2>
        <div className="grid md:grid-cols-2 gap-4">
          {platforms.map((p, i) => (
            <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/40 transition-all">
              <div className="flex items-center gap-3 mb-3">
                <h3 className="text-lg font-semibold text-white">{p.name}</h3>
                {p.badge && <span className="text-[10px] uppercase tracking-wider bg-[#00736a]/10 text-[#00a396] px-2 py-0.5 rounded-full">{p.badge}</span>}
              </div>
              <p className="text-sm text-muted leading-relaxed mb-4">{p.desc}</p>
              <div className="flex flex-wrap gap-2">
                {p.features.map((f, j) => (
                  <span key={j} className="text-xs bg-[#1a1f2e] text-gray-400 px-2 py-1 rounded">{f}</span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Process */}
      <section className="mb-16 p-8 bg-[#0f1629] border border-gray-800 rounded-xl">
        <h2 className="text-2xl font-bold text-white mb-6">Naš proces implementacije</h2>
        <div className="grid md:grid-cols-4 gap-4">
          {[
            { step: '01', title: 'Analiza', desc: 'Mapiranje procesa, definisanje ciljeva i KPI-jeva' },
            { step: '02', title: 'Konfiguracija', desc: 'Postavka sistema, migracija podataka, integracije' },
            { step: '03', title: 'Obuka', desc: 'Trening tima, mentorska podrška 30 dana' },
            { step: '04', title: 'Optimizacija', desc: 'Kontinuirano praćenje i prilagođavanje' },
          ].map((s, i) => (
            <div key={i} className="text-center">
              <div className="text-2xl font-bold text-[#00a396] mb-2">{s.step}</div>
              <h3 className="text-white font-semibold mb-1">{s.title}</h3>
              <p className="text-xs text-muted">{s.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Related Blog Posts (Cluster) */}
      <section className="mb-16">
        <h2 className="text-2xl font-bold text-white mb-2">Vodiči i članci o CRM-u</h2>
        <p className="text-muted text-sm mb-8">Detaljni vodiči, poređenja i savjeti za odabir i implementaciju CRM sistema.</p>
        <div className="grid md:grid-cols-2 gap-3">
          {relatedPosts.map((post) => (
            <Link key={post.slug} to={`/blog/posts/${post.slug}`}
              className="bg-[#0a0f1c] border border-gray-800 rounded-xl p-4 hover:border-[#00736a]/30 transition-all group">
              <h3 className="text-sm font-medium text-white group-hover:text-[#00a396] transition-colors">{post.title}</h3>
            </Link>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="text-center p-10 bg-gradient-to-br from-[#00736a]/10 to-[#0f1629] border border-[#00736a]/20 rounded-xl">
        <h2 className="text-2xl font-bold text-white mb-4">Niste sigurni koji CRM je pravi za vas?</h2>
        <p className="text-muted mb-6 max-w-lg mx-auto">Radimo besplatne konsultacije i demonstraciju. Odgovaramo u roku 24h.</p>
        <Link to={l('/contact')} className="inline-block bg-[#00736a] text-white px-8 py-3 rounded-xl font-medium hover:bg-[#008a7f] transition-all">
          Zakažite konsultacije
        </Link>
      </section>
    </div>
  )
}
