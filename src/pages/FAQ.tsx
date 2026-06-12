export default function FAQ() {
  const faqs = [
    { q: "Koje CRM platforme podržavate?", a: "Bitrix24, HubSpot, Salesforce, Zoho CRM, Pipedrive i SugarCRM. Specijalizirani smo za implementaciju, migraciju i integraciju." },
    { q: "Koliko traje implementacija CRM-a?", a: "Osnovna implementacija traje 2-4 sedmice, u zavisnosti od kompleksnosti. Prve rezultate vidite već nakon prve sedmice." },
    { q: "Šta su AI agenti i kako mogu pomoći mom biznisu?", a: "AI agenti su inteligentni softverski asistenti koji automatiziraju zadatke poput customer supporta, lead generationa i marketinga. Oni uče iz vaših podataka i konstantno se poboljšavaju." },
    { q: "Radite li sa firmama van Bosne?", a: "Da, radimo sa klijentima u Hrvatskoj, Švicarskoj, Njemačkoj, Austriji i US. Naš tim je raspoređen u više zemalja." },
    { q: "Kako funkcioniše proces onboardinga?", a: "Proces počinje besplatnim konsultacijama gdje analiziramo vaše potrebe, zatim slijedi predlog rješenja, implementacija, testiranje i produkcija sa podrškom." },
  ]

  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">Često postavljana pitanja</h1>
      <p className="text-muted mb-12">Odgovori na najčešća pitanja o našim uslugama.</p>
      <div className="space-y-4">
        {faqs.map((faq, i) => (
          <details key={i} className="group bg-[#0f1629] border border-gray-800 rounded-xl overflow-hidden">
            <summary className="px-6 py-4 cursor-pointer text-white font-medium text-sm hover:bg-white/5 transition-colors list-none flex justify-between items-center">
              {faq.q}
              <span className="text-muted group-open:rotate-180 transition-transform">▾</span>
            </summary>
            <div className="px-6 pb-4 text-sm text-muted leading-relaxed">{faq.a}</div>
          </details>
        ))}
      </div>
    </div>
  )
}
