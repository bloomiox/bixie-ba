// AI audit lead form endpoint for Cloudflare Pages
// Forwards to BloomOS API on VPS and returns a success page with checklist download
export async function onRequest(context) {
    const { request } = context;

    if (request.method !== 'POST') {
        return new Response('Method not allowed', { status: 405 });
    }

    try {
        const formData = await request.formData();
        const name = formData.get('name') || '';
        const email = formData.get('email') || '';
        const company = formData.get('company') || '';
        const size = formData.get('size') || '';
        const focus = formData.get('focus') || '';
        const message = formData.get('message') || '';

        if (!email || !email.includes('@')) {
            const html = `<html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="3;url=/ai-audit"></head>
            <body style="background:#08090a;color:#d0d6e0;font-family:system-ui;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center;flex-direction:column;gap:12px">
                <h2 style="color:#f7f8f8;">❌ Neispravna email adresa</h2>
                <p style="color:#8a8f98;">Molimo unesite validnu email adresu.</p>
                <a href="/ai-audit" style="color:#5e6ad2;">← Nazad na AI procjenu</a>
            </body></html>`;
            return new Response(html, { headers: { 'content-type': 'text/html;charset=UTF-8' } });
        }

        // Forward to BloomOS VPS (same pattern as newsletter)
        const payload = JSON.stringify({
            name, email, company, size, focus, message,
            source: 'bixie.ba/ai-audit',
            timestamp: new Date().toISOString()
        });

        try {
            await fetch('http://204.168.130.130:3344/api/ai-audit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: payload
            });
        } catch (e) {
            console.error('Failed to forward to BloomOS:', e.message);
        }

        // Success page with checklist download link
        const html = `<html><head><meta charset="UTF-8"></head>
        <body style="background:#08090a;color:#d0d6e0;font-family:system-ui;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;flex-direction:column;gap:14px;padding:24px">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            <h2 style="color:#f7f8f8;margin:0;">✅ Hvala ${name ? name.split(' ')[0] : ''}! Prijava je primljena.</h2>
            <p style="color:#8a8f98;max-width:440px;margin:0;">Kontaktiramo vas u roku 24h radnim danom. Do tada — preuzmite AI Readiness Checklist i ispunite je prije našeg razgovora.</p>
            <a href="/downloads/ai-readiness-checklist.pdf" style="background:#00736a;color:#fff;text-decoration:none;padding:14px 28px;border-radius:8px;font-weight:600;margin-top:8px;">📋 Preuzmi AI Readiness Checklist (PDF)</a>
            <a href="/" style="color:#5e6ad2;margin-top:16px;">← Nazad na BIXIE.ba</a>
        </body></html>`;

        return new Response(html, {
            headers: { 'content-type': 'text/html;charset=UTF-8' }
        });

    } catch (error) {
        return new Response('Error processing request', { status: 500 });
    }
}
