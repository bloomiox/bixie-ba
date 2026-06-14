import { Link } from 'react-router-dom'

export default function ServicesCRM() {
  const platforms = [
    { name: 'Bitrix24', badge: 'Official Partner', desc: 'Kompletan CRM sa ugrađenom telefonijom, HR modulima, email marketingom i disk prostorom. Od besplatnog plana do enterprise rješenja. On-premise i cloud.', tags: ['CRM + Kolaboracija', 'On-premise i Cloud', 'Telefonija', 'HR Moduli'] },
    { name: 'Zoho CRM', badge: 'Partner', desc: 'Zoho CRM sa AI asistentom Zia. Automatsko bodovanje leadova, predviđanje prodaje i napredna analitika. Integracija sa Zoho ekosistemom od 50+ aplikacija.', tags: ['AI Asistent Zia', 'Omnikanalna podrška', 'Workflow Automatizacija'] },
    { name: 'Monday.com CRM', badge: 'Partner', desc: 'Monday.com sa vizuelnim pipeline-om i AI automatizacijama. Idealno za timove koji žele brzu implementaciju i intuitivno sučelje. Implementacija u roku 1-2 sedmice.', tags: ['Vizuelni Pipeline', 'AI Automatizacije', 'Integracije'] },
    { name: 'Salesforce', badge: 'Partner', desc: 'Salesforce sa Einstein AI. Enterprise CRM za srednje i velike firme. Migracija sa drugih sistema, custom razvoj i integracija. Vodeći globalni CRM.', tags: ['Einstein AI', 'Enterprise', 'Migracija'] },
    { name: 'Pipedrive', badge: 'Partner', desc: 'Pipedrive fokusiran na prodaju. Intuitivan pipeline menadžment, automatizacija follow-upa i AI predviđanje prodaje. Idealno za prodajne timove.', tags: ['Sales Pipeline', 'AI Predictions', 'Automatizacija'] },
    { name: 'HubSpot', badge: 'Partner', desc: 'HubSpot sa besplatnim planom i AI alatima za marketing, prodaju i customer service. Breeze AI za automatizaciju. Kompletan marketing hub.', tags: ['Free CRM', 'Breeze AI', 'Marketing Hub'] },
    { name: 'SugarCRM', badge: '', desc: 'SugarCRM sa inteligentnim automatskim workflow-om i naprednom analitikom. Idealno za firme koje žele potpunu kontrolu nad prodajnim procesom.', tags: ['Intelligent Workflow', 'Analytics', 'Automation'] },
    { name: 'Microsoft Dynamics 365', badge: '', desc: 'Microsoft Dynamics 365 sa AI Copilot integracijom. Kompletno poslovno rješenje koje povezuje CRM i ERP u jedan ekosistem.', tags: ['AI Copilot', 'CRM + ERP', 'Microsoft Ecosystem'] },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">CRM</span>
      <h1 className="text-4xl font-bold text-white mb-4">CRM rješenja</h1>
      <p className="text-muted mb-12 max-w-2xl">Implementacija, migracija i optimizacija CRM sistema. Official Bitrix24 partner za Bosnu i Hercegovinu.</p>

      <div className="space-y-4">
        {platforms.map((p, i) => (
          <div key={i} id={p.name.toLowerCase().replace(/\s+/g, '')} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <div className="flex items-start justify-between mb-3">
              <h2 className="text-xl font-bold text-white">{p.name}</h2>
              {p.badge && <span className="text-[10px] uppercase tracking-wider text-[#00736a] bg-[#00736a]/10 px-2 py-1 rounded">{p.badge}</span>}
            </div>
            <p className="text-sm text-muted leading-relaxed mb-3">{p.desc}</p>
            <div className="flex flex-wrap gap-2">
              {p.tags.map((tag, j) => (
                <span key={j} className="text-[10px] uppercase tracking-wider text-gray-400 bg-white/5 px-2 py-1 rounded">{tag}</span>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="mt-12 bg-[#0f1629] border border-[#00736a]/20 rounded-xl p-8 text-center">
        <p className="text-muted mb-6">Niste sigurni koji CRM je pravi za vas? Radimo besplatne konsultacije i demonstraciju.</p>
        <Link to="/contact" className="inline-block bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium hover:bg-[#008a7f] transition-all">
          Zakažite konsultacije
        </Link>
      </div>
    </div>
  )
}
