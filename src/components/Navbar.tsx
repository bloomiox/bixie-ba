import { Link, useLocation } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { useState } from 'react'

export default function Navbar() {
  const { t, i18n } = useTranslation()
  const location = useLocation()
  const [mobileOpen, setMobileOpen] = useState(false)
  const lang = location.pathname.startsWith('/en') ? 'en' : location.pathname.startsWith('/de') ? 'de' : 'bs'

  const switchLang = (l: string) => {
    const path = location.pathname.replace(/^\/(en|de|bs)/, '')
    const prefix = l === 'bs' ? '' : `/${l}`
    window.location.href = `${prefix}${path || '/'}`
  }

  const linkClass = (path: string) =>
    `text-sm font-medium transition-colors ${
      location.pathname === path || location.pathname.startsWith(path + '/')
        ? 'text-white'
        : 'text-gray-400 hover:text-white'
    }`

  const navLinks = [
    { path: `/${lang === 'bs' ? '' : lang + '/'}services/crm`.replace(/\/\//g, '/'), label: t('nav.crm'), dropdown: true },
    { path: `/${lang === 'bs' ? '' : lang + '/'}services/ai-agents`.replace(/\/\//g, '/'), label: t('nav.ai') },
    { path: `/${lang === 'bs' ? '' : lang + '/'}services/digital-transformation`.replace(/\/\//g, '/'), label: t('nav.digital') },
    { path: `/${lang === 'bs' ? '' : lang + '/'}services/rpa`.replace(/\/\//g, '/'), label: t('nav.rpa') },
    { path: `/${lang === 'bs' ? '' : lang + '/'}blog`.replace(/\/\//g, '/'), label: t('nav.blog') },
    { path: `/${lang === 'bs' ? '' : lang + '/'}contact`.replace(/\/\//g, '/'), label: t('nav.contact'), cta: true },
  ]

  return (
    <nav className="sticky top-0 z-50 border-b border-gray-800/50 bg-[#0a0f1c]/95 backdrop-blur-xl">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <Link to={lang === 'bs' ? '/' : `/${lang}`} className="flex items-center gap-3">
          <img src="/images/logo/bixie-logo.png" alt="BIXIE" style={{ height: 32 }} />
        </Link>

        <div className="hidden md:flex items-center gap-6">
          {navLinks.map((link) => (
            link.cta ? (
              <Link key={link.path} to={link.path} className="bg-[#00736a] text-white px-5 py-2 rounded-lg text-sm font-medium hover:bg-[#008a7f] transition-all hover:-translate-y-px">
                {link.label}
              </Link>
            ) : (
              <Link key={link.path} to={link.path} className={linkClass(link.path)}>
                {link.label}
              </Link>
            )
          ))}
          <div className="flex items-center gap-1 ml-4 border-l border-gray-800 pl-4">
            {['bs', 'en', 'de'].map((l) => (
              <button key={l} onClick={() => switchLang(l)}
                className={`text-xs px-2 py-1 rounded transition-colors ${lang === l ? 'text-white bg-white/10' : 'text-gray-500 hover:text-gray-300'}`}>
                {l.toUpperCase()}
              </button>
            ))}
          </div>
        </div>

        <button className="md:hidden flex flex-col gap-1.5 p-1" onClick={() => setMobileOpen(!mobileOpen)}>
          {[0,1,2].map(i => <span key={i} className="block w-5 h-0.5 bg-gray-400 rounded transition-all" />)}
        </button>
      </div>

      {mobileOpen && (
        <div className="md:hidden border-t border-gray-800/40 px-4 py-4 bg-[#0a0f1c] space-y-3">
          {navLinks.map((link) => (
            <Link key={link.path} to={link.path} onClick={() => setMobileOpen(false)}
              className={`block py-2 text-sm ${link.cta ? 'text-[#00736a] font-medium' : 'text-gray-400'}`}>
              {link.label}
            </Link>
          ))}
          <div className="flex gap-2 pt-2 border-t border-gray-800/40">
            {['bs', 'en', 'de'].map((l) => (
              <button key={l} onClick={() => { switchLang(l); setMobileOpen(false) }}
                className={`text-xs px-3 py-1.5 rounded ${lang === l ? 'text-white bg-white/10' : 'text-gray-500'}`}>
                {l.toUpperCase()}
              </button>
            ))}
          </div>
        </div>
      )}
    </nav>
  )
}
