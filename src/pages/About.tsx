export default function About() {
  const stats = [
    { num: '15+', label: 'Godina iskustva', desc: 'Od 2011. uspješno implementiramo digitalna rješenja za firme u BiH, Švicarskoj, Njemačkoj i regiji.' },
    { num: '25+', label: 'Certifikacija', desc: 'Registered partner za Bitrix24, Zoho, Salesforce, Pipedrive i HubSpot. Licencirani za Microsoft i Google Cloud.' },
    { num: '100+', label: 'Realizovanih projekata', desc: 'CRM implementacije, AI integracije, RPA automatizacije i cloud migracije za različite industrije.' },
  ]

  const services = [
    { title: 'CRM Implementacija', desc: 'Bitrix24, Zoho, Salesforce, HubSpot, Pipedrive. Migracija i integracija sa postojećim sistemima.' },
    { title: 'AI Agenti i Automatizacija', desc: 'Custom AI agenti, RPA, nabavka AI licenci (ChatGPT, Gemini, Claude). Kompletna AI podrška.' },
    { title: 'Digitalno Radno Mjesto', desc: 'Digital Office sa kolaboracijom, task menadžmentom i dokumentima na jednom mjestu.' },
    { title: 'Private & Hybrid Cloud', desc: 'Cloud infrastruktura sa sigurnosnim slojevima. Hibridni model za maksimalnu zaštitu.' },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">O nama</span>
      <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 leading-tight">Više od decenije<br />digitalne transformacije</h1>
      <p className="text-lg text-muted max-w-2xl mb-16">BIXIE je full-service digitalna agencija specijalizovana za CRM, AI agente, RPA automatizaciju i digitalno radno mjesto. Osnovani 2011. godine.</p>

      {/* Stats */}
      <div className="grid md:grid-cols-3 gap-6 mb-20">
        {stats.map((s, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <div className="text-3xl font-bold gradient-text mb-2">{s.num}</div>
            <h3 className="text-lg font-semibold text-white mb-2">{s.label}</h3>
            <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
          </div>
        ))}
      </div>

      {/* Services */}
      <h2 className="text-2xl font-bold text-white mb-8">Šta radimo</h2>
      <div className="grid md:grid-cols-2 gap-4 mb-20">
        {services.map((s, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-2">{s.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{s.desc}</p>
          </div>
        ))}
      </div>

      {/* Why */}
      <div className="bg-[#0f1629] border border-gray-800 rounded-xl p-8">
        <h2 className="text-2xl font-bold text-white mb-4">Zašto BIXIE?</h2>
        <p className="text-muted mb-6">Ne prodajemo softver — rješavamo poslovne probleme. Svaki projekat počinjemo analizom procesa.</p>
        <div className="flex flex-wrap gap-3">
          {['Lokalna podrška', 'BHS jezik', '24h SLA', 'GDPR', '15+ godina iskustva'].map((tag, i) => (
            <span key={i} className="inline-flex px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20">{tag}</span>
          ))}
        </div>
      </div>
    </div>
  )
}
