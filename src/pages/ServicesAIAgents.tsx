export default function ServicesAIAgents() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">AI Agenti & Automatizacija</h1>
      <p className="text-muted mb-12 max-w-2xl">Custom AI agenti koji transformišu način na koji vaša firma radi — od customer supporta do lead generationa i marketing automatizacije.</p>

      <div className="grid md:grid-cols-2 gap-6 mb-16">
        {[
          { title: 'Customer Support AI', desc: 'AI agenti koji odgovaraju na korisnička pitanja 24/7, eskaliraju kompleksne slučajeve i uče iz interakcija.' },
          { title: 'Lead Generation AI', desc: 'Automatsko pronalaženje i kvalifikacija potencijalnih klijenata kroz pretragu, analizu i personalizovani outreach.' },
          { title: 'Marketing AI', desc: 'Automatizacija kreiranja sadržaja, personalizacije kampanja i analize performansi.' },
          { title: 'Knowledge Management AI', desc: 'AI agenti koji organizuju, pretražuju i distribuiraju znanje unutar vaše organizacije.' },
          { title: 'Sales AI', desc: 'AI asistenti za prodajne timove — analiza pipeline-a, predikcija zatvaranja i automatsko follow-up.' },
          { title: 'HR AI', desc: 'Automatizacija HR procesa — selekcija kandidata, onboarding, upravljanje performansama.' },
        ].map((ai, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-3">{ai.title}</h3>
            <p className="text-sm text-muted leading-relaxed">{ai.desc}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
