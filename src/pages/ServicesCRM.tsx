export default function ServicesCRM() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">CRM Implementacija</h1>
      <p className="text-muted mb-12 max-w-2xl">Implementacija, migracija i integracija vodećih CRM platformi. Bilo da tek krećete ili mijenjate sistem, mi vas vodimo kroz cijeli proces.</p>

      <div className="grid md:grid-cols-2 gap-6 mb-16">
        {[
          { name: 'Bitrix24', desc: 'Kompletan CRM i poslovna platforma za male i srednje firme. Implementacija, prilagođavanje, integracija i obuka.', badge: 'Partner' },
          { name: 'HubSpot', desc: 'Sales, marketing i service hub. Implementacija, migracija iz drugih sistema i optimizacija.', badge: 'Partner' },
          { name: 'Salesforce', desc: 'Enterprise CRM rješenje. Implementacija, customizacija i integracija sa postojećim sistemima.', badge: 'Partner' },
          { name: 'Zoho CRM', desc: 'Cjenovno pristupačan CRM sa bogatim setom feature-a. Implementacija, migracija i automatizacija.', badge: 'Partner' },
          { name: 'Pipedrive', desc: 'Sales-first CRM za prodajne timove. Implementacija i optimizacija prodajnog pipeline-a.', badge: 'Partner' },
          { name: 'SugarCRM', desc: 'Enterprise CRM sa naprednim mogućnostima prilagođavanja i automatizacije.', badge: 'Partner' },
        ].map((crm, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <div className="flex items-start justify-between mb-3">
              <h3 className="text-lg font-semibold text-white">{crm.name}</h3>
              <span className="text-[10px] uppercase tracking-wider text-[#00736a] bg-[#00736a]/10 px-2 py-1 rounded">{crm.badge}</span>
            </div>
            <p className="text-sm text-muted leading-relaxed">{crm.desc}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
