export default function Contact() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">Kontakt</h1>
      <p className="text-muted mb-12 max-w-xl">Pošaljite nam poruku i javit ćemo vam se u najkraćem mogućem roku.</p>

      <form className="space-y-6 max-w-xl" onSubmit={e => e.preventDefault()}>
        <div className="grid md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm text-gray-400 mb-2">Ime i prezime</label>
            <input type="text" className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors" placeholder="Vaše ime" />
          </div>
          <div>
            <label className="block text-sm text-gray-400 mb-2">Email</label>
            <input type="email" className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors" placeholder="email@primjer.com" />
          </div>
        </div>
        <div>
          <label className="block text-sm text-gray-400 mb-2">Poruka</label>
          <textarea rows={5} className="w-full bg-[#0f1629] border border-gray-800 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-[#00736a] transition-colors resize-none" placeholder="Kako vam možemo pomoći?" />
        </div>
        <button type="submit" className="bg-[#00736a] text-white px-8 py-3 rounded-lg font-medium text-sm hover:bg-[#008a7f] transition-all">
          Pošaljite poruku
        </button>
      </form>

      <div className="mt-16 p-6 bg-[#0f1629] border border-gray-800 rounded-xl max-w-xl">
        <h3 className="text-white font-medium mb-2">Ili nas kontaktirajte direktno</h3>
        <p className="text-sm text-muted">Email: hello@bixie.ba</p>
      </div>
    </div>
  )
}
