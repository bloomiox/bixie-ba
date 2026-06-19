import { Outlet, useLocation } from 'react-router-dom'
import { HelmetProvider } from 'react-helmet-async'
import Navbar from './Navbar'
import Footer from './Footer'
import SEO from './SEO'
import ExitIntentPopup from './ExitIntentPopup'
import { localBusinessSchema } from './schema'

export default function Layout() {
  const location = useLocation()
  const path = location.pathname.replace(/^\/[a-z]{2}\//, '/').replace(/^\/[a-z]{2}$/, '/')

  const pageMeta: Record<string, { title: string; description: string }> = {
    '/': {
      title: 'CRM, AI Agenti & Digitalna Transformacija',
      description: 'BIXIE implementira CRM sisteme (Bitrix24, Zoho, Salesforce), AI agente i digitalnu transformaciju za firme u BiH, Hrvatskoj, Švicarskoj i EU. Official Bitrix24 partner.',
    },
    '/about': {
      title: 'O nama',
      description: 'BIXIE — partner za digitalnu transformaciju od 2011. Preko 100 realizovanih projekata, 25+ certifikacija, 7 CRM platformi. Oficijelni Bitrix24 partner za BiH.',
    },
    '/contact': {
      title: 'Kontakt',
      description: 'Zakažite besplatne konsultacije. BIXIE tim odgovara u roku 24h. Implementacija CRM sistema, AI agenata i digitalne transformacije.',
    },
    '/faq': {
      title: 'Često postavljana pitanja',
      description: 'Odgovori na najčešća pitanja o CRM implementaciji, AI agentima, cijenama i procesu digitalne transformacije.',
    },
    '/services/crm': {
      title: 'CRM Implementacija — Bitrix24, Zoho, Salesforce, HubSpot',
      description: 'Implementacija, migracija i optimizacija CRM sistema. Official partner za Bitrix24, Zoho, Monday.com, Salesforce, Pipedrive, HubSpot. Za firme u BiH, Hrvatskoj i EU.',
    },
    '/services/ai-agents': {
      title: 'AI Agenti — Custom razvoj i implementacija',
      description: 'Razvoj custom AI agenata za customer support, lead generation, marketing automatizaciju i upravljanje znanjem. Integracija sa CRM-om, WhatsApp-om i web chatom.',
    },
    '/services/digital-transformation': {
      title: 'Digitalna Transformacija — Optimizacija poslovnih procesa',
      description: 'Optimizacija poslovnih procesa kroz digitalna rješenja, automatizaciju i modernu tehnologiju. Za firme u BiH, Hrvatskoj i Švicarskoj.',
    },
    '/services/rpa': {
      title: 'RPA Automatizacija — Robotska automatizacija procesa',
      description: 'Robotska automatizacija procesa za eliminaciju ručnih, ponavljajućih zadataka. Uštedite do 70% vremena na administrativnim poslovima.',
    },
    '/blog': {
      title: 'Blog — Savjeti o AI, CRM i digitalnoj transformaciji',
      description: 'Najnoviji članci o AI agentima, CRM sistemima, RPA i digitalnoj transformaciji. Praktični vodiči za BiH firme.',
    },
    '/case-studies': {
      title: 'Case Studies — Primjeri uspješnih implementacija',
      description: 'Stvarni primjeri kako smo firmama pomogli da kroz AI agente, CRM i RPA smanje troškove i povećaju produktivnost.',
    },
    '/ai-providers': {
      title: 'AI Licence — ChatGPT, Gemini, GitHub Copilot, Canva, Microsoft 365',
      description: 'Nabavka i upravljanje licencama za ChatGPT, Google Gemini, GitHub Copilot, Canva i Microsoft 365. Akademski popusti za obrazovne ustanove.',
    },
    '/privacy': {
      title: 'Politika privatnosti',
      description: 'Politika privatnosti BIXIE — kako prikupljamo, koristimo i štitimo vaše podatke u skladu sa GDPR-om.',
    },
  }

  const meta = pageMeta[path] || pageMeta['/']

  return (
    <HelmetProvider>
      <SEO
        title={meta.title}
        description={meta.description}
        canonical={path || '/'}
        schema={localBusinessSchema}
      />
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-1">
          <Outlet />
        </main>
        <Footer />
        <ExitIntentPopup />
      </div>
    </HelmetProvider>
  )
}
