export default function FAQ() {
  const faqs = [
    { q: 'Koje CRM sisteme podržavate?', a: 'BIXIE je specijalizovan za implementaciju i podršku najpopularnijih CRM sistema: Bitrix24, Zoho CRM, Monday.com, Salesforce, Pipedrive, Twenty CRM i HubSpot. Za svaki sistem imamo certificirane konsultante i dokazanu metodologiju implementacije. Preporučujemo sistem na osnovu veličine vaše firme, budžeta i specifičnih potreba.' },
    { q: 'Koliko traje implementacija CRM-a?', a: 'Vrijeme implementacije zavisi od složenosti i broja korisnika. Bitrix24 i Zoho CRM za manje firme (do 10 korisnika) može biti operativan za 1-2 sedmice. Srednje firme (10-50 korisnika) obično zahtijevaju 3-5 sedmica. Salesforce i napredne implementacije sa custom integracijama mogu trajati 4-8 sedmica. BIXIE nudi i Express implementaciju za hitne slučajeve.' },
    { q: 'Šta su AI agenti i kako mogu pomoći mojoj firmi?', a: 'AI agenti su autonomni softverski sistemi pokrenuti velikim jezičkim modelima (LLM) koji mogu samostalno obavljati zadatke — od odgovaranja na pitanja korisnika do složenih poslovnih procesa. Mogu raditi 24/7, bez odmora i grešaka, i mogu obraditi hiljade zadataka istovremeno. Najčešće primjene u BiH firmama: korisnička podrška, lead generation, automatizacija admin poslova, analiza podataka i upravljanje zalihama.' },
    { q: 'Koliko košta AI agent?', a: 'Cijena AI agenta zavisi od složenosti. Osnovni AI agent za FAQ na web chatu košta od 1.500 KM + 250 KM/mjesečno. Srednji paket sa više kanala i integracijom u CRM je 3.500-5.000 KM + 500 KM/mjesečno. Napredni multi-agent sistemi su 8.000-15.000 KM. U poređenju sa mjesečnim troškom support tima (15.000-25.000 KM), AI agent se isplati za 1-3 mjeseca.' },
    { q: 'Kako funkcioniše licenciranje AI alata za obrazovne ustanove?', a: 'BIXIE je partner za akademsko licenciranje ChatGPT Edu, Google Workspace for Education i Microsoft 365 Education. Akademske licence su značajno povoljnije od komercijalnih. Za .edu.ba domene nudimo ChatGPT Edu od 28 KM/korisnik/mjesečno, Google Workspace for Education sa Gemini AI od 18 KM/korisnik/mjesečno. Minimalni broj korisnika je 10.' },
    { q: 'Da li nudite podršku na bosanskom jeziku?', a: 'Da, BIXIE pruža kompletnu podršku na bosanskom/hrvatskom/srpskom jeziku. Od inicijalnih konsultacija, preko implementacije i obuke, do svakodnevne podrške — naš tim je dostupan putem telefona (033 922 622), emaila (hello@bixie.ba) i uživo u našem uredu u Sarajevu.' },
    { q: 'Koja je razlika između RPA i AI agenta?', a: 'RPA (Robotic Process Automation) automatizira ponavljajuće, pravilo-bazirane zadatke — unos podataka, kopiranje fajlova, slanje emailova. AI agenti, s druge strane, koriste velike jezičke modele za donošenje odluka, razumijevanje konteksta i komunikaciju na prirodnom jeziku. Najbolji rezultati se postižu kombinacijom obje tehnologije.' },
    { q: 'Kako znamo koji CRM je najbolji za nas?', a: 'BIXIE nudi besplatne konsultacije u trajanju od 30 minuta. Analiziramo: veličinu vašeg tima, prodajne procese, budžet, potrebu za integracijama i željeni nivo automatizacije. Na osnovu ove analize preporučujemo 2-3 optimalna sistema. Do sada smo sa preciznošću od 95% preporučili pravi sistem u prvom pokušaju.' },
    { q: 'Da li AI agenti mogu raditi na WhatsApp-u?', a: 'Da, AI agenti se integrišu sa WhatsApp Business API-jem — najpopularnijim kanalom komunikacije u BiH. Agent može odgovarati na poruke, slati notifikacije, potvrđivati rezervacije i pružati podršku 24/7. Integracija je u potpunosti usklađena sa Meta politikama i GDPR-om.' },
    { q: 'Koje načine plaćanja prihvatate?', a: 'Prihvatamo: virmansko plaćanje na žiro račun u KM (domaće fakture sa PDV-om), bankovni transfer u EUR/CHF (za inostrane klijente), i kartice (Visa, Mastercard) za online plaćanja. Sve cijene na našim ponudama su izražene u KM sa uračunatim PDV-om od 17%.' },
  ]

  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">FAQ</span>
      <h1 className="text-4xl font-bold text-white mb-12">Često postavljana pitanja</h1>
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
