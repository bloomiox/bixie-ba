export default function AIProviders() {
  const providers = [
    { name: 'OpenAI', desc: 'GPT-4, GPT-4o, GPT-4o-mini — najnapredniji jezički modeli za AI agente, chatbotove i automatizaciju.' },
    { name: 'Anthropic', desc: 'Claude 3.5 Sonnet, Claude 3 Opus — sigurni i pouzdani AI modeli za enterprise aplikacije.' },
    { name: 'Google AI', desc: 'Gemini 2.0, Gemini 1.5 Pro — multimodalni AI modeli za analizu teksta, slika i videa.' },
    { name: 'Meta (Llama)', desc: 'Llama 3.1, Llama 3 — open-source modeli koje hostamo na privatnoj infrastrukturi.' },
    { name: 'Mistral AI', desc: 'Mistral Large, Mistral Medium — evropski AI modeli sa fokusom na privatnost i performanse.' },
    { name: 'DeepSeek', desc: 'DeepSeek-V3, DeepSeek-R1 — cost-effective modeli za produkcijske AI agente.' },
  ]

  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">AI Provideri</h1>
      <p className="text-muted mb-12 max-w-2xl">Integrišemo najbolje AI modele na tržištu — biramo optimalnog providera za svaki use case.</p>

      <div className="grid md:grid-cols-2 gap-6">
        {providers.map((p, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h3 className="text-lg font-semibold text-white mb-3">{p.name}</h3>
            <p className="text-sm text-muted leading-relaxed">{p.desc}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
