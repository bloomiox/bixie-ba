import { Link } from 'react-router-dom'

export default function AIProviders() {
  const providers = [
    {
      name: 'OpenAI — ChatGPT',
      models: 'GPT-4o, GPT-4.5, o3, DALL·E 3, Whisper',
      desc: 'Lider u generativnoj AI tehnologiji. ChatGPT kombinuje napredno razumijevanje prirodnog jezika, generisanje koda, analizu podataka i obradu slika. Enterprise sigurnost: podaci se ne koriste za trening modela, SOC 2 i GDPR usklađeno.',
      best: 'Generisanje sadržaja, analiza podataka, programiranje, customer support, obrazovanje',
    },
    {
      name: 'Google AI — Gemini',
      models: 'Gemini 2.5 Pro, Gemini 2.0 Flash, Imagen 3, Veo 2',
      desc: 'Potpuno integrisan u Google Workspace — Gmail, Docs, Sheets, Meet, Drive. AI piše email umjesto vas, sažima lance emailova, kreira prezentacije i analizira podatke unutar postojećeg Workspace okruženja.',
      best: 'Firme koje koriste Google Workspace, AI u dokumentima i emailu, video analiza',
    },
    {
      name: 'Anthropic — Claude',
      models: 'Claude 4 Opus, Claude 4 Sonnet, Claude 4 Haiku',
      desc: 'Poznat po izuzetnoj sigurnosti, etičkom dizajnu i najdužem kontekstnom prozoru na tržištu — može obraditi čitave knjige ili kompletnu kode bazu odjednom. Izuzetno precizan u analizi pravnih, finansijskih i tehničkih dokumenata.',
      best: 'Analiza dokumenata, programiranje, pravni i finansijski tekstovi, content creation',
    },
    {
      name: 'DeepSeek',
      models: 'DeepSeek-R1, DeepSeek-V3',
      desc: 'Kineski AI model poznat po izuzetno povoljnoj cijeni i impresivnim performansama uporedivim sa vodećim modelima. BIXIE nudi managed pristup sa domaćom fakturom. Do 95% jeftiniji od GPT-4 za sličan kvalitet.',
      best: 'Programiranje, matematika, logičko rezonovanje, cost-efikasne operacije',
    },
    {
      name: 'Mistral AI',
      models: 'Mistral Large 2, Mistral Small, Codestral',
      desc: 'Vodeći evropski AI provajder sa sjedištem u Francuskoj. Svi modeli se hostuju na EU serverima — potpuna GDPR usklađenost. Odlična podrška za višejezične zadatke.',
      best: 'Firme koje zahtijevaju GDPR usklađenost, evropske kompanije, višejezične aplikacije',
    },
  ]

  return (
    <div className="max-w-5xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">AI Licence</span>
      <h1 className="text-4xl font-bold text-white mb-4">AI provajderi i licence</h1>
      <p className="text-muted mb-12 max-w-2xl">Zvanični distributer i reseller AI licenci za Bosnu i Hercegovinu. Domaća faktura sa PDV-om, legalna nabavka, podrška na bosanskom jeziku.</p>

      <div className="space-y-6">
        {providers.map((p, i) => (
          <div key={i} className="bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all">
            <h2 className="text-xl font-bold text-white mb-3">{p.name}</h2>
            <div className="space-y-3 text-sm">
              <div>
                <span className="text-xs text-muted uppercase tracking-wider">Ključni modeli</span>
                <p className="text-gray-300 mt-1">{p.models}</p>
              </div>
              <p className="text-muted leading-relaxed">{p.desc}</p>
              <div>
                <span className="text-xs text-muted uppercase tracking-wider">Najbolje za</span>
                <p className="text-gray-300 mt-1">{p.best}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-12 bg-[#0f1629] border border-[#00736a]/20 rounded-xl p-8 text-center">
        <h3 className="text-xl font-bold text-white mb-3">Spremni za AI?</h3>
        <p className="text-muted mb-6">Pretplatite se na AI modele po vašoj mjeri. Domaća faktura, legalna nabavka, podrška na bosanskom.</p>
        <Link to="/contact" className="inline-block bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium hover:bg-[#008a7f] transition-all">
          Pretplatite se na AI modele
        </Link>
      </div>
    </div>
  )
}
