import { Link } from 'react-router-dom'

export default function ServicesAIAgents() {
  const agents = [
    { title: 'Customer Support', desc: 'AI agenti za korisničku podršku putem web chata, WhatsAppa i emaila. Automatski odgovori na učestala pitanja i eskalacija ljudskim agentima.' },
    { title: 'Sales Automation', desc: 'AI agenti za kvalifikaciju leadova, automatski follow-up i predviđanje prodaje. Integracija sa Bitrix24, Zoho i Salesforce.' },
    { title: 'RPA Automatizacija', desc: 'Robotic Process Automation za repetitivne zadatke. Unos podataka, sinhronizacija sistema, generisanje izvještaja.' },
  ]

  const steps = [
    { step: '01', title: 'Audit', desc: 'Analiza poslovnih procesa i identifikacija prilika za AI automatizaciju.' },
    { step: '02', title: 'Proof of Concept', desc: 'Razvoj prototipa AI agenta u roku 2 sedmice za jedan specifičan proces.' },
    { step: '03', title: 'Integracija', desc: 'Povezivanje AI agenata sa postojećim sistemima putem API-ja.' },
    { step: '04', title: 'Monitoring', desc: 'Nadzor performansi AI agenata i kontinuirano poboljšanje.' },
  ]

  const licences = [
    { title: 'ChatGPT Team i Enterprise', desc: 'OpenAI licence za timove i institucije. Napredni AI alati uz potpunu kontrolu podataka.' },
    { title: 'Google Gemini', desc: 'Google Workspace sa ugrađenim Gemini AI asistentom. Integracija sa Gmail, Docs i Meet.' },
    { title: 'Microsoft Copilot', desc: 'Microsoft 365 Copilot za automatizaciju u Word, Excel, Teams i Outlook.' },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">AI</span>
      <h1 className="text-4xl font-bold text-white mb-4">AI agenti i automatizacija</h1>
      <p className="text-muted mb-12 max-w-2xl">Razvoj custom AI agenata, RPA automatizacija i nabavka AI licenci za vaše poslovanje.</p>

      <h2 className="text-2xl font-bold text-white mb-6">AI Agenti i Automatizacija</h2>
      <div className="grid md:grid-cols-3 gap-4 mb-16">
        {agents.map((a, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-2">{a.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{a.desc}</p>
          </div>
        ))}
      </div>

      <h2 id="implementacija" className="text-2xl font-bold text-white mb-6">AI Implementacija</h2>
      <div className="grid md:grid-cols-4 gap-4 mb-16">
        {steps.map((s, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <div className="text-2xl font-bold gradient-text mb-2">{s.step}</div>
            <h3 className="text-lg font-semibold text-white mb-2">{s.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
          </div>
        ))}
      </div>

      <h2 id="licence" className="text-2xl font-bold text-white mb-6">AI Licence</h2>
      <div className="grid md:grid-cols-3 gap-4 mb-16">
        {licences.map((l, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-2">{l.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{l.desc}</p>
          </div>
        ))}
      </div>

      <div className="bg-[#0f1629] border border-[#00736a]/20 rounded-xl p-8 text-center">
        <p className="text-muted mb-6">Želite implementirati AI u vašoj firmi?</p>
        <Link to="/contact" className="inline-block bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium hover:bg-[#008a7f] transition-all">
          Zakažite konsultacije
        </Link>
      </div>
    </div>
  )
}
