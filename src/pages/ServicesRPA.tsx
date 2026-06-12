export default function ServicesRPA() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">RPA Automatizacija</h1>
      <p className="text-muted mb-12 max-w-2xl">Robotska automatizacija procesa koja eliminiše ručne, ponavljajuće zadatke i oslobađa vaš tim za fokus na vrijednosni rad.</p>

      <div className="grid md:grid-cols-2 gap-6 mb-16">
        {[
          { title: 'Finansije', desc: 'Automatizacija fakturisanja, usaglašavanja izvoda, generisanja izvještaja i knjiženja.' },
          { title: 'HR', desc: 'Automatizacija payroll-a, onboarding dokumentacije, zahtjeva za godišnji i evidencije radnog vremena.' },
          { title: 'Prodaja', desc: 'Automatsko slanje ponuda, praćenje pipeline-a, generisanje ugovora i follow-up emailova.' },
          { title: 'Operacije', desc: 'Automatizacija unosa podataka, obrade dokumenata, generisanja izvještaja i notifikacija.' },
        ].map((rpa, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-3">{rpa.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{rpa.desc}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
