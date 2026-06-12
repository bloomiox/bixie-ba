import { Link, useLocation } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

export default function Footer() {
  const { t } = useTranslation()
  const location = useLocation()
  const lang = location.pathname.startsWith('/en') ? 'en' : location.pathname.startsWith('/de') ? 'de' : 'bs'

  return (
    <footer className="border-t border-gray-800/50 py-12 mt-20">
      <div className="max-w-6xl mx-auto px-4">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mb-8">
          <div>
            <img src="/images/logo/bixie-logo.png" alt="BIXIE" style={{ height: 28 }} className="mb-4" />
            <p className="text-xs text-muted leading-relaxed">CRM, AI Agenti & Digitalna Transformacija</p>
          </div>
          <div>
            <h4 className="text-white text-sm font-medium mb-3">Usluge</h4>
            <div className="space-y-2 text-xs text-muted">
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}services/crm`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">CRM</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}services/ai-agents`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">AI Agenti</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}services/digital-transformation`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">Digitalna Transformacija</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}services/rpa`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">RPA</Link>
            </div>
          </div>
          <div>
            <h4 className="text-white text-sm font-medium mb-3">Kompanija</h4>
            <div className="space-y-2 text-xs text-muted">
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}about`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">O nama</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}blog`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">Blog</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}case-studies`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">Case Studies</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}contact`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">Kontakt</Link>
            </div>
          </div>
          <div>
            <h4 className="text-white text-sm font-medium mb-3">Info</h4>
            <div className="space-y-2 text-xs text-muted">
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}faq`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">FAQ</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}privacy`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">Privatnost</Link>
              <Link to={`/${lang === 'bs' ? '' : lang + '/'}ai-providers`.replace(/\/\//g, '/')} className="block hover:text-white transition-colors">AI Provideri</Link>
            </div>
          </div>
        </div>
        <div className="border-t border-gray-800/40 pt-6 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-xs text-muted">© {new Date().getFullYear()} BIXIE. {t('footer.rights')}</p>
          <div className="flex gap-3 text-xs text-muted">
            <a href="https://bloom.ba" className="hover:text-white transition-colors">by Bloom</a>
          </div>
        </div>
      </div>
    </footer>
  )
}
