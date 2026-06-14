export default function Contact() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-20">
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#00736a]/10 text-[#00a396] border border-[#00736a]/20 mb-4">Kontakt</span>
      <h1 className="text-4xl font-bold text-white mb-4">Kontaktirajte nas</h1>
      <p className="text-muted mb-12 max-w-xl">Pošaljite upit, zatražite ponudu ili zakažite besplatne konsultacije. Odgovaramo u roku 24h.</p>

      <div className="grid md:grid-cols-2 gap-12">
        {/* Form */}
        <div>
          <form className="space-y-6" action="https://api.bloom.ba/api/contact" method="POST">
            <input type="hidden" name="source" value="bixie.ba" />
            <div>
              <label className="block text-sm text-gray-400 mb-2">Ime i Prezime *</label>
              <input type="text" name="name" required
                className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors"
                placeholder="Vaše ime i prezime" />
            </div>
            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm text-gray-400 mb-2">Email *</label>
                <input type="email" name="email" required
                  className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors"
                  placeholder="vas@email.com" />
              </div>
              <div>
                <label className="block text-sm text-gray-400 mb-2">Telefon</label>
                <input type="tel" name="phone"
                  className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors"
                  placeholder="033 922 622" />
              </div>
            </div>
            <div>
              <label className="block text-sm text-gray-400 mb-2">Kompanija</label>
              <input type="text" name="company"
                className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors"
                placeholder="Naziv vaše firme" />
            </div>
            <div>
              <label className="block text-sm text-gray-400 mb-2">Poruka *</label>
              <textarea name="message" required rows={5}
                className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors resize-none"
                placeholder="Opišite šta vam je potrebno..." />
            </div>
            <button type="submit"
              className="bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium text-sm hover:bg-[#008a7f] transition-all">
              Pošaljite upit
            </button>
          </form>
        </div>

        {/* Contact Info */}
        <div className="space-y-4">
          <div className="bg-[#0f1629] border border-gray-800 rounded-xl p-6">
            <h3 className="text-white font-medium mb-2">Email</h3>
            <p className="text-sm"><a href="mailto:hello@bixie.ba" className="text-[#00736a] hover:underline">hello@bixie.ba</a></p>
            <p className="text-xs text-muted mt-1">Za upite i ponude</p>
          </div>
          <div className="bg-[#0f1629] border border-gray-800 rounded-xl p-6">
            <h3 className="text-white font-medium mb-2">Telefon</h3>
            <p className="text-sm text-gray-300">033 922 622</p>
            <p className="text-xs text-muted mt-1">Radnim danom 09:00 - 17:00</p>
          </div>
          <div className="bg-[#0f1629] border border-gray-800 rounded-xl p-6">
            <h3 className="text-white font-medium mb-2">Adresa</h3>
            <p className="text-sm text-gray-300">Maglajska 1</p>
            <p className="text-sm text-muted">71000 Sarajevo, Bosna i Hercegovina</p>
          </div>
          <div className="bg-[#0f1629] border border-gray-800 rounded-xl p-6">
            <h3 className="text-white font-medium mb-2">Ponude i Licence</h3>
            <p className="text-sm text-muted">Bitrix24, AI, Google, Microsoft</p>
            <p className="text-xs text-muted mt-1">Izdajemo ponude za pravna lica sa pečatom i potpisom</p>
          </div>
        </div>
      </div>
    </div>
  )
}
