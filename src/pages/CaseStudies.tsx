export default function CaseStudies() {
  const cases = [
    {
      tag: 'AI Agenti', tagColor: 'text-[#00736a]',
      title: 'IT firma smanjila troškove podrške za 60%',
      industry: 'IT i Softverski Razvoj',
      location: 'Sarajevo, Bosna i Hercegovina',
      solution: 'AI Agent za Customer Support (WhatsApp + Web Chat)',
      desc: 'IT firma sa 45 zaposlenih i preko 2.000 aktivnih korisnika suočavala se sa rastućim troškovima korisničke podrške. Implementirali smo AI agenta koji pokriva prvi nivo podrške na WhatsApp-u i web chatu. Agent samostalno rješava 73% upita, dok složene slučajeve eskalira ljudskim agentima.',
      result: 'Smanjenje support tima sa 3 na 1 agenta, vrijeme odgovora sa 6 sati na 45 sekundi.',
      metrics: [{ num: '-60%', label: 'Troškovi podrške' }, { num: '73%', label: 'Automatsko rješavanje' }, { num: '45s', label: 'Vrijeme odgovora' }, { num: '94%', label: 'Zadovoljstvo' }],
    },
    {
      tag: 'RPA & AI', tagColor: 'text-[#10b981]',
      title: 'E-trgovina povećala prodaju za 40%',
      industry: 'E-trgovina / Online Shop',
      location: 'Mostar, Bosna i Hercegovina',
      solution: 'AI Prodajni Agent + RPA Automatizacija Zaliha',
      desc: 'Online shop sa 15.000 proizvoda imao je problem sa upravljanjem zalihama i gubitkom prodaje zbog sporog odgovaranja. Implementirali smo AI prodajnog agenta koji automatski odgovara na pitanja i RPA bota koji upravlja zalihama.',
      result: 'Prodaja porasla za 40%, napuštene korpe smanjene za 35%.',
      metrics: [{ num: '+40%', label: 'Prodaja' }, { num: '-35%', label: 'Napuštene korpe' }, { num: '-25%', label: 'Vezani kapital' }],
    },
    {
      tag: 'CRM', tagColor: 'text-[#f59e0b]',
      title: 'Proizvodna firma digitalizovala prodaju sa Bitrix24',
      industry: 'Proizvodnja',
      location: 'Tuzla, Bosna i Hercegovina',
      solution: 'Bitrix24 CRM + Automatizacija Prodajnog Procesa',
      desc: 'Proizvodna firma sa 120 zaposlenih koristila je Excel za praćenje prodaje. Implementacijom Bitrix24 CRM-a digitalizovali smo kompletan prodajni proces — od prvog kontakta do fakture.',
      result: 'Produktivnost povećana 45%, izrada ponuda sa 2 dana na 2 sata.',
      metrics: [{ num: '+45%', label: 'Produktivnost' }, { num: '2h', label: 'Izrada ponude' }, { num: '+30%', label: 'Konverzija' }],
    },
    {
      tag: 'Agentic AI', tagColor: 'text-[#8b5cf6]',
      title: 'Autonomni agent za lead generation u IT sektoru',
      industry: 'IT Konsulting',
      location: 'Banja Luka, Bosna i Hercegovina',
      solution: 'Autonomni AI Agent za Prodaju',
      desc: 'IT konsulting firma željela je povećati broj kvalifikovanih leadova bez povećanja prodajnog tima. Razvili smo autonomnog AI agenta koji svakodnevno pretražuje internet, analizira potrebe, kreira personalizovane emailove i automatski zakazuje sastanke.',
      result: 'Kvalifikovani sastanci povećani sa 8 na 35 mjesečno.',
      metrics: [{ num: '337%', label: 'Više sastanaka' }, { num: '35', label: 'Sastanaka/mjesec' }, { num: '24/7', label: 'Autonomni rad' }],
    },
    {
      tag: 'AI Licence', tagColor: 'text-[#00736a]',
      title: 'Univerzitet opremio 500 studenata AI alatima',
      industry: 'Obrazovanje',
      location: 'Sarajevo, Bosna i Hercegovina',
      solution: 'ChatGPT Edu + Google Workspace for Education + Gemini AI',
      desc: 'Privatni univerzitet u Sarajevu želio je studentima i nastavnom osoblju omogućiti pristup najnovijim AI alatima. Kroz BIXIE-ov program akademskog licenciranja osigurali smo ChatGPT Edu, Google Workspace for Education i Microsoft 365 A3 licence.',
      result: 'Prvi univerzitet u BiH sa integrisanim AI alatima u nastavni proces.',
      metrics: [{ num: '500', label: 'Studenata' }, { num: '50', label: 'Nastavnika' }, { num: '3', label: 'AI platforme' }],
    },
    {
      tag: 'RPA', tagColor: 'text-[#00736a]',
      title: 'Startup uštedio 10.000 KM sa RPA automatizacijom',
      industry: 'Finansijske Usluge',
      location: 'Sarajevo, Bosna i Hercegovina',
      solution: 'RPA + AI za Automatizaciju Finansijskih Izvještaja',
      desc: 'Finansijski startup sa 8 zaposlenih trošio je preko 40 sati mjesečno na ručno generisanje izvještaja. Implementirali smo RPA rješenje koje automatski povlači podatke, kategorizira transakcije i generiše izvještaje.',
      result: 'Ušteđeno 40 sati mjesečno, 10.000 KM godišnje.',
      metrics: [{ num: '40h', label: 'Ušteđeno/mjesečno' }, { num: '10.000KM', label: 'Godišnja ušteda' }, { num: '0', label: 'Grešaka' }],
    },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Reference</span>
      <h1 className="text-4xl font-bold text-white mb-4">Reference i case studies</h1>
      <p className="text-muted mb-12 max-w-2xl">Rezultati koje smo postigli za naše klijente u Bosni i Hercegovini i regionu.</p>
      <div className="space-y-8">
        {cases.map((c, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-8 hover:border-[#00736a]/30 transition-all">
            <div className="flex flex-wrap items-start justify-between gap-4 mb-4">
              <div>
                <span className={`inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#00736a]/10 ${c.tagColor} border border-[#00736a]/20 mb-3`}>{c.tag}</span>
                <h2 className="text-2xl font-bold text-white">{c.title}</h2>
              </div>
            </div>
            <div className="grid md:grid-cols-3 gap-6 mb-6">
              <div><span className="text-xs text-muted uppercase tracking-wider">Industrija</span><p className="text-sm text-gray-300">{c.industry}</p></div>
              <div><span className="text-xs text-muted uppercase tracking-wider">Lokacija</span><p className="text-sm text-gray-300">{c.location}</p></div>
              <div><span className="text-xs text-muted uppercase tracking-wider">Rješenje</span><p className="text-sm text-gray-300">{c.solution}</p></div>
            </div>
            <p className="text-sm text-muted leading-relaxed mb-4">{c.desc}</p>
            <p className="text-sm text-gray-300 font-medium mb-6">{c.result}</p>
            <div className="flex flex-wrap gap-4">
              {c.metrics.map((m, j) => (
                <div key={j} className="bg-[#0a0f1c] border border-gray-800 rounded-lg px-4 py-3 text-center min-w-[100px]">
                  <div className="text-lg font-bold gradient-text">{m.num}</div>
                  <div className="text-xs text-muted mt-1">{m.label}</div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
