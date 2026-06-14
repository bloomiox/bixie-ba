import { Link } from 'react-router-dom'

export default function ServicesDigitalTransformation() {
  const services = [
    { title: 'Optimizacija Procesa', desc: 'Analiza i redizajn poslovnih procesa sa ciljem smanjenja operativnih troškova i povećanja efikasnosti. Implementacija digitalnih tokova rada.' },
    { title: 'AI Integracija u ERP/DMS', desc: 'Integracija AI agenata u postojeće ERP i DMS sisteme. Automatizacija unosa podataka, generisanje izvještaja i prediktivna analitika.' },
    { title: 'Automatizacija Radnih Tokova', desc: 'RPA automatizacija repetitivnih zadataka. Sync podataka između sistema, automatsko fakturisanje, upravljanje dokumentima.' },
    { title: 'IT Konsalting i Strategija', desc: 'Izrada digitalne strategije, tehnološki audit, izbor optimalnih alata i platformi za vaše poslovanje.' },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Digitalna Transformacija</span>
      <h1 className="text-4xl font-bold text-white mb-4">Digitalna transformacija</h1>
      <p className="text-muted mb-12 max-w-2xl">Optimizacija poslovnih procesa, AI integracije u ERP/DMS sisteme, automatizacija radnih tokova.</p>

      <div className="grid md:grid-cols-2 gap-4 mb-16">
        {services.map((s, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-2">{s.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
          </div>
        ))}
      </div>

      <div className="bg-[#0f1629] border border-[#00736a]/20 rounded-xl p-8 text-center">
        <p className="text-muted mb-6">Želite unaprijediti vaše poslovanje kroz digitalnu transformaciju?</p>
        <Link to="/contact" className="inline-block bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium hover:bg-[#008a7f] transition-all">
          Zakažite sastanak
        </Link>
      </div>
    </div>
  )
}
