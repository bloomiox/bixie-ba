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
            <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-white leading-tight mb-6 animate-in">
              {t('hero.title')}
            </h1>
            <p className="text-lg md:text-xl text-gray-400 mb-10 max-w-2xl animate-in delay-1">
              {t('hero.subtitle')}
            </p>
            <div className="flex flex-wrap gap-4 animate-in delay-2">
              <Link to={l('/contact')} className="bg-[#00736a] text-white px-8 py-3.5 rounded-xl text-sm font-medium hover:bg-[#008a7f] transition-all hover:-translate-y-0.5 shadow-lg shadow-[#00736a]/20">
                {t('hero.cta')}
              </Link>
              <Link to={l('/services/crm')} className="border border-gray-700 text-gray-300 px-8 py-3.5 rounded-xl text-sm font-medium hover:border-gray-500 hover:text-white transition-all">
                {t('nav.crm')} →
              </Link>
            </div>
            <p className="text-xs text-muted mt-8 animate-in delay-3">{t('hero.partners')}</p>
          </div>
        </div>
      </section>

      {/* Partners */}
      <section className="py-16 border-y border-gray-800/50">
        <div className="max-w-6xl mx-auto px-4">
          <p className="text-xs text-muted text-center mb-8 uppercase tracking-widest">Partneri</p>
          <div className="flex flex-wrap items-center justify-center gap-8 md:gap-12 opacity-50 grayscale">
            {partners.map(p => (
              <img key={p} src={`/images/logos/${p}.${p.includes('jpg') ? 'jpg' : 'png'}`.replace('.jpg.jpg', '.jpg').replace('.png.png', '.png')}
                alt={p} style={{ height: 28 }} className="hover:opacity-100 transition-opacity" />
            ))}
          </div>
        </div>
      </section>

      {/* Services */}
      <section className="py-24">
        <div className="max-w-6xl mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-white text-center mb-4">{t('services.title')}</h2>
          <p className="text-muted text-center mb-16 max-w-xl mx-auto">Implementiramo rješenja koja donose mjerljive rezultate.</p>
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

      {/* CTA */}
      <section className="py-20 bg-gradient-to-b from-[#0f1629] to-[#0a0f1c]">
        <div className="max-w-3xl mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">Spremni za digitalnu transformaciju?</h2>
          <p className="text-muted mb-10 max-w-lg mx-auto">Zakažite besplatne konsultacije i saznajte kako vam možemo pomoći.</p>
          <Link to={l('/contact')} className="inline-block bg-[#00736a] text-white px-10 py-4 rounded-xl font-medium hover:bg-[#008a7f] transition-all hover:-translate-y-0.5 shadow-lg shadow-[#00736a]/20">
            {t('hero.cta')}
          </Link>
        </div>
      </section>
    </div>
  )
}
