import { Link, useLocation } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

export default function Home() {
  const { t } = useTranslation()
  const location = useLocation()
  const lang = location.pathname.startsWith('/en') ? 'en' : location.pathname.startsWith('/de') ? 'de' : 'bs'

  const l = (p: string) => (lang === 'bs' ? p : `/${lang}${p}`)

  const services = [
    { icon: '▣', title: t('services.crm.title'), desc: t('services.crm.desc'), href: l('/services/crm') },
    { icon: '◇', title: t('services.ai.title'), desc: t('services.ai.desc'), href: l('/services/ai-agents') },
    { icon: '○', title: t('services.digital.title'), desc: t('services.digital.desc'), href: l('/services/digital-transformation') },
    { icon: '□', title: t('services.rpa.title'), desc: t('services.rpa.desc'), href: l('/services/rpa') },
  ]

  const partners = ['bitrix24', 'hubspot', 'salesforce', 'zoho', 'pipedrive', 'microsoft-dynamics', 'sugarcrm']

  const projects = [
    { tag: 'CRM', title: 'Bitrix24 implementacija', desc: 'Kompletna CRM implementacija za transportnu kompaniju sa 50+ korisnika.', href: l('/services/crm') },
    { tag: 'AI', title: 'AI agent za customer support', desc: 'Custom AI agent integrisan sa Bitrix24 i WhatsApp za automatsku podršku.', href: l('/services/ai-agents') },
    { tag: 'Digitalna transformacija', title: 'Digitalni ured za SME', desc: 'Implementacija digitalnog radnog prostora sa privatnim cloudom i RPA.', href: l('/services/digital-transformation') },
    { tag: 'RPA', title: 'RPA automatizacija nabavke', desc: 'Automatizacija cjelokupnog procesa nabavke sa AI validacijom dokumenata.', href: l('/services/ai-agents') },
  ]

  const whyBixie = [
    { num: '01', title: 'Bitrix24 Official Partner', desc: 'Certificirani partner sa iskustvom u implementaciji Bitrix24 rješenja za firme svih veličina.' },
    { num: '02', title: 'AI Integracije', desc: 'Razvoj custom AI agenata koji se integriraju sa postojećim sistemima — CRM, ERP, DMS, web.' },
    { num: '03', title: 'Lokalna Podrška', desc: 'Podrška na BHS jeziku, razumijevanje lokalnih poslovnih procesa i regulative.' },
    { num: '04', title: 'Licence i Nabavka', desc: 'Nabavka i upravljanje licencama za ChatGPT, Gemini, GitHub Copilot, Canva i Microsoft 365.' },
  ]

  const testimonials = [
    { initials: 'MK', name: 'Mirsad K.', role: 'CEO, transportna kompanija', text: 'Profesionalan pristup i odlično poznavanje Bitrix24 platforme. Implementacija je protekla glatko, a podrška je uvijek dostupna.' },
    { initials: 'AH', name: 'Amela H.', role: 'Direktorica prodaje', text: 'AI agent kojeg su nam razvili potpuno je transformirao naš customer support. Automatski odgovara na 80% upita.' },
    { initials: 'ED', name: 'Edin D.', role: 'Operativni menadžer', text: 'Kombinacija RPA i AI agenata nam je uštedila preko 40 sati mjesečno na administrativnim poslovima.' },
  ]

  const blogPosts = [
    { tag: 'AI Licence', title: 'AI Licence za Obrazovne Ustanove', desc: 'ChatGPT Edu, Google Workspace for Education, Microsoft 365 Education. Cijene i akademski popusti.', href: '/blog/posts/ai-licence-obrazovne-ustanove' },
    { tag: 'CRM', title: 'Bitrix24 vs AI-Powered CRM', desc: 'Poređenje Bitrix24 i modernih AI CRM rješenja. Kada ostati na Bitrix24, a kada uvesti AI?', href: '/blog/posts/bitrix24-vs-ai-crm' },
    { tag: 'RPA', title: 'RPA i AI Automatizacija', desc: 'Kako automatizirati poslovne procese kombinacijom RPA i AI agenata. Uštede do 70%.', href: '/blog/posts/rpa-automatizacija-procesa' },
  ]

  const faqs = [
    { q: 'Koje CRM platforme podržavate?', a: 'Podržavamo Bitrix24, Zoho CRM, Salesforce, HubSpot, Pipedrive, Microsoft Dynamics, SugarCRM i Twenty CRM. Kao registrovani partner za većinu platformi, nudimo implementaciju, migraciju i optimizaciju.' },
    { q: 'Kako funkcioniše proces implementacije?', a: 'Proces počinje besplatnim konsultacijama gdje analiziramo vaše potrebe. Nakon toga slijedi plan implementacije, konfiguracija sistema, migracija podataka, obuka korisnika i post-implementacijska podrška.' },
    { q: 'Da li nudite AI agente po mjeri?', a: 'Da. Razvijamo custom AI agente koji se integriraju sa vašim postojećim sistemima — CRM, ERP, DMS, web i druge platforme. Podržavamo ChatGPT, Claude, Gemini i druge modele.' },
  ]

  return (
    <div>
      {/* Hero */}
      <section className="relative min-h-[85vh] flex items-center overflow-hidden">
        <div className="absolute inset-0 z-0">
          <video autoPlay muted loop playsInline className="w-full h-full object-cover" poster="/og-image.png">
            <source src="/assets/video/hero.mp4" type="video/mp4" />
          </video>
          <div className="absolute inset-0 bg-gradient-to-br from-[#0a0f1c]/95 via-[#0a0f1c]/80 to-[#0a0f1c]/90 z-[1]" />
        </div>
        <div className="relative z-10 max-w-6xl mx-auto px-4 w-full">
          <div className="max-w-3xl">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/15 text-[#00a396] border border-[#00736a]/25 mb-6 animate-in">Partner od 2011 · 25+ Certifikacija</span>
            <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-white leading-tight mb-6 animate-in">
              CRM, AI Agenti i<br />
              <span className="gradient-text">Digitalna Transformacija</span>
            </h1>
            <p className="text-lg md:text-xl text-gray-400 mb-10 max-w-2xl animate-in delay-1">
              Pomažemo firmama da unaprijede poslovanje kroz pametan odabir i implementaciju CRM sistema, AI agenata i RPA rješenja.
            </p>
            <div className="flex flex-wrap gap-4 animate-in delay-2">
              <Link to={l('/contact')} className="bg-[#00736a] text-white px-8 py-3.5 rounded-xl text-sm font-medium hover:bg-[#008a7f] transition-all hover:-translate-y-0.5 shadow-lg shadow-[#00736a]/20">
                Zatražite ponudu
              </Link>
              <Link to={l('/services/crm')} className="border border-gray-700 text-gray-300 px-8 py-3.5 rounded-xl text-sm font-medium hover:border-gray-500 hover:text-white transition-all">
                Pogledajte usluge →
              </Link>
            </div>
            <p className="text-xs text-muted mt-8 animate-in delay-3">Povjerenje vodećih platformi</p>
          </div>
        </div>
      </section>

      {/* Partners */}
      <section className="py-16 border-y border-gray-800/50">
        <div className="max-w-6xl mx-auto px-4">
          <p className="text-xs text-muted text-center mb-8 uppercase tracking-widest">Povjerenje vodećih platformi</p>
          <div className="flex flex-wrap items-center justify-center gap-8 md:gap-12 opacity-50 grayscale">
            {partners.map(p => (
              <img key={p} src={`/images/logos/${p}.${p.includes('jpg') ? 'jpg' : 'png'}`.replace('.jpg.jpg', '.jpg').replace('.png.png', '.png')}
                alt={p} style={{ height: 28 }} className="hover:opacity-100 transition-opacity" />
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { num: '15+', label: 'Godina iskustva' },
              { num: '25+', label: 'Certifikacija' },
              { num: '100+', label: 'Realizovanih projekata' },
              { num: '7', label: 'CRM platformi' },
            ].map((s, i) => (
              <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 text-center hover:border-[#00736a]/30 transition-all">
                <div className="text-3xl font-bold gradient-text mb-1">{s.num}</div>
                <p className="text-sm text-muted">{s.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services */}
      <section className="py-24">
        <div className="max-w-6xl mx-auto px-4">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Rješenja</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">Kompletna digitalna rješenja</h2>
          <p className="text-muted mb-16 max-w-xl">Od digitalnog ureda do privatnog clouda — sve što vam treba za digitalnu transformaciju.</p>
          <div className="grid md:grid-cols-2 gap-6">
            {services.map((s, i) => (
              <Link key={i} to={s.href}
                className="group bg-[#0f1629] border border-gray-800 rounded-xl p-8 hover:border-[#00736a]/40 transition-all hover:-translate-y-0.5">
                <div className="text-2xl text-[#00736a] mb-4">{s.icon}</div>
                <h3 className="text-xl font-semibold text-white mb-2 group-hover:text-[#00736a] transition-colors">{s.title}</h3>
                <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Projects */}
      <section className="py-24 bg-[#0f1629]/50">
        <div className="max-w-6xl mx-auto px-4">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Projekti</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">Izdvojeni projekti</h2>
          <p className="text-muted mb-12 max-w-xl">Svaki projekat je prilagođen ciljevima i dugoročnoj skalabilnosti.</p>
          <div className="grid md:grid-cols-2 gap-4">
            {projects.map((p, i) => (
              <Link key={i} to={p.href} className="bg-[#0a0f1c] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/40 transition-all">
                <span className="inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-3">{p.tag}</span>
                <h3 className="text-lg font-semibold text-white mb-2">{p.title}</h3>
                <p className="text-sm text-muted leading-relaxed">{p.desc}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Why BIXIE */}
      <section className="py-24">
        <div className="max-w-6xl mx-auto px-4">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Zašto BIXIE</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">Što nas izdvaja</h2>
          <p className="text-muted mb-12 max-w-xl">Kombiniramo tehnološku ekspertizu sa razumijevanjem lokalnog tržišta.</p>
          <div className="grid md:grid-cols-2 gap-4">
            {whyBixie.map((w, i) => (
              <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 flex gap-4 hover:border-[#00736a]/30 transition-all">
                <span className="inline-flex items-center justify-center w-12 h-12 bg-[#00736a]/15 rounded-xl text-[#00a396] font-bold shrink-0">{w.num}</span>
                <div>
                  <h3 className="text-lg font-semibold text-white mb-1">{w.title}</h3>
                  <p className="text-sm text-muted leading-relaxed">{w.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-24 bg-[#0f1629]/50">
        <div className="max-w-6xl mx-auto px-4">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Testimonijali</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-12">Šta kažu klijenti</h2>
          <div className="grid md:grid-cols-3 gap-4">
            {testimonials.map((t, i) => (
              <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6">
                <p className="text-muted text-sm leading-relaxed mb-4">&ldquo;{t.text}&rdquo;</p>
                <div className="flex items-center gap-3">
                  <div className="w-9 h-9 rounded-full bg-[#00736a]/20 flex items-center justify-center text-[#00a396] text-xs font-bold">{t.initials}</div>
                  <div>
                    <div className="text-sm font-medium text-white">{t.name}</div>
                    <div className="text-xs text-muted">{t.role}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Blog Preview */}
      <section className="py-24">
        <div className="max-w-6xl mx-auto px-4">
          <div className="flex items-end justify-between mb-10">
            <div>
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Blog</span>
              <h2 className="text-3xl font-bold text-white">Savjeti i vodiči</h2>
            </div>
            <Link to="/blog" className="text-[#00a396] hover:text-[#00a396] text-sm font-medium hidden md:block">Svi članci →</Link>
          </div>
          <div className="grid md:grid-cols-3 gap-4">
            {blogPosts.map((bp, i) => (
              <Link key={i} to={bp.href} className="block bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/40 transition-all group">
                <span className="inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-3">{bp.tag}</span>
                <h3 className="text-base font-semibold text-white mb-2 group-hover:text-[#00a396] transition-colors">{bp.title}</h3>
                <p className="text-sm text-muted leading-relaxed">{bp.desc}</p>
              </Link>
            ))}
          </div>
          <Link to="/blog" className="text-[#00a396] text-sm font-medium mt-4 block md:hidden">Svi članci →</Link>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-24 bg-[#0f1629]/50">
        <div className="max-w-6xl mx-auto px-4">
          <div className="max-w-3xl mx-auto">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">FAQ</span>
            <h2 className="text-3xl font-bold text-white mb-12">Često postavljana pitanja</h2>
            <div className="space-y-3">
              {faqs.map((faq, i) => (
                <details key={i} className="group bg-[#0f1629] border border-gray-800 rounded-xl overflow-hidden">
                  <summary className="px-6 py-4 cursor-pointer text-white font-medium text-sm hover:bg-white/5 transition-colors list-none flex justify-between items-center">
                    {faq.q}
                    <span className="text-muted group-open:rotate-180 transition-transform">▾</span>
                  </summary>
                  <div className="px-6 pb-4 text-sm text-muted leading-relaxed">{faq.a}</div>
                </details>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-gradient-to-b from-[#0f1629] to-[#0a0f1c]">
        <div className="max-w-3xl mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">Spremni za digitalnu transformaciju?</h2>
          <p className="text-muted mb-10 max-w-lg mx-auto">Zakažite besplatne konsultacije. Odgovaramo u roku 24h.</p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link to={l('/contact')} className="inline-block bg-[#00736a] text-white px-10 py-4 rounded-xl font-medium hover:bg-[#008a7f] transition-all hover:-translate-y-0.5 shadow-lg shadow-[#00736a]/20">
              Zatražite ponudu
            </Link>
            <a href="mailto:hello@bixie.ba" className="border border-gray-700 text-gray-300 px-10 py-4 rounded-xl font-medium hover:border-gray-500 hover:text-white transition-all">
              hello@bixie.ba
            </a>
          </div>
        </div>
      </section>
    </div>
  )
}
