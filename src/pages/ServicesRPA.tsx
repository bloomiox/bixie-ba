import { Link } from 'react-router-dom'

export default function ServicesRPA() {
  const services = [
    { title: 'Unos Podataka', desc: 'Automatsko preuzimanje iz emaila, PDF-ova i Excel tabela u CRM/ERP.' },
    { title: 'Obrada Dokumenata', desc: 'AI ekstrakcija podataka iz faktura i ugovora. Automatska kategorizacija.' },
    { title: 'Izvještaji', desc: 'Automatsko generisanje izvještaja sa slanjem na email i dashboard.' },
    { title: 'Email Automatizacija', desc: 'Sortiranje, odgovaranje i AI klasifikacija email poruka.' },
    { title: 'CRM Automatizacija', desc: 'Automatski leadovi, kontakti i aktivnosti u Bitrix24, Zoho, Salesforce.' },
    { title: 'Workflow', desc: 'Povezivanje sistema. Approval workflow i notifikacije bez kodiranja.' },
  ]

  const steps = [
    { step: '01', title: 'Analiza', desc: 'Mapiranje procesa i identifikacija zadataka za automatizaciju.' },
    { step: '02', title: 'PoC', desc: 'Prototip za 1-2 sedmice za jedan specifičan proces.' },
    { step: '03', title: 'Implementacija', desc: 'RPA botovi i AI agenti u produkcijsko okruženje.' },
    { step: '04', title: 'Monitoring', desc: 'Nadzor i kontinuirano poboljšanje automatizacije.' },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">RPA i AI</span>
      <h1 className="text-4xl font-bold text-white mb-4 leading-tight">RPA i AI automatizacija<br />poslovnih procesa</h1>
      <p className="text-muted mb-12 max-w-2xl">Automatizacija ponavljajućih zadataka kombinacijom RPA i AI tehnologija. Uštede do 70% vremena na administraciji.</p>

      <div className="grid md:grid-cols-3 gap-4 mb-16">
        {services.map((s, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-2">{s.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
          </div>
        ))}
      </div>

      <h2 className="text-2xl font-bold text-white mb-6">Proces implementacije</h2>
      <div className="grid md:grid-cols-4 gap-4 mb-16">
        {steps.map((s, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <div className="text-2xl font-bold gradient-text mb-2">{s.step}</div>
            <h3 className="text-lg font-semibold text-white mb-2">{s.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
          </div>
        ))}
      </div>

      <div className="bg-[#0f1629] border border-[#00736a]/20 rounded-xl p-8 text-center">
        <p className="text-muted mb-6">Želite besplatni audit vaših procesa?</p>
        <Link to="/contact" className="inline-block bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium hover:bg-[#008a7f] transition-all">
          Zakažite audit
        </Link>
      </div>
    </div>
  )
}
