// Auto-converted from old static site
// Original: contact/index.html
export default function Contact() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-16">
      <div className="prose prose-invert max-w-none old-site-content"
        dangerouslySetInnerHTML={{
          __html: `<div class="section-inner" >
<div >Kontakt</div>
<h1>Kontaktirajte nas</h1>
<p >Posaljite upit, zatrazite ponudu ili zakazite besplatne konsultacije. Odgovaramo u roku 24h.</p>
<div class="contact-grid">
<div class="card" >
<div class="success-msg" id="successMsg">Vasa poruka je poslana. Odgovaramo u roku 24h.</div>
<form id="contactForm" action="https://api.bloom.ba/api/contact" method="POST">
<input type="hidden" name="source" value="bixie.ba">
<div class="form-group">
<label for="name">Ime i Prezime *</label>
<input type="text" id="name" name="name" required placeholder="Vase ime i prezime">
</div>
<div class="form-group">
<label for="email">Email *</label>
<input type="email" id="email" name="email" required placeholder="vas@email.com">
</div>
<div class="form-group">
<label for="phone">Telefon</label>
<input type="tel" id="phone" name="phone" placeholder="033 922 622">
</div>
<div class="form-group">
<label for="company">Kompanija</label>
<input type="text" id="company" name="company" placeholder="Naziv vase firme">
</div>
<div class="form-group">
<label for="message">Poruka *</label>
<textarea id="message" name="message" required placeholder="Opisite sta vam je potrebno..."></textarea>
</div>
<button type="submit" class="inline-block bg-[#00736a] text-white px-6 py-3 rounded-lg font-medium hover:bg-[#005c54] transition-colors" id="submitBtn">Posaljite upit</button>
<div class="error-msg" id="errorMsg"></div>
</form>
</div>
<div>
<div class="card" >
<h3 >Email</h3>
<p ><a href="mailto:hello@bixie.ba" >hello@bixie.ba</a></p>
<p >Za upite i ponude</p>
</div>
<div class="card" >
<h3 >Telefon</h3>
<p >033 922 622</p>
<p >Radnim danom 09:00 - 17:00</p>
</div>
<div class="card" >
<h3 >Adresa</h3>
<p >Maglajska 1</p>
<p >71000 Sarajevo, Bosna i Hercegovina</p>
</div>
<div class="card">
<h3 >Ponude i Licence</h3>
<p >Bitrix24, AI, Google, Microsoft</p>
<p >Izdajemo ponude za pravna lica sa pecatom i potpisom</p>
</div>
</div>
</div>
</div>`
        }}
      />
    </div>
  )
}