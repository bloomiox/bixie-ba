// Cloudflare Workers entry — SPA + API handler
// Replaces _redirects (which caused infinite loop on Workers deploy)
// Serves static assets, falls back to index.html for React Router,
// and handles API routes directly.

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // ── API routes ──────────────────────────────
    if (path.startsWith('/api/')) {
      if (path === '/api/newsletter' && request.method === 'POST') {
        return handleNewsletter(request);
      }
      return new Response('Not found', { status: 404 });
    }

    // ── Static assets ───────────────────────────
    try {
      const response = await env.ASSETS.fetch(request);
      if (response.status !== 404) return response;
    } catch {
      // Fall through
    }

    // ── SPA fallback (React Router) ─────────────
    const indexUrl = new URL('/index.html', request.url);
    const indexRes = await env.ASSETS.fetch(new Request(indexUrl, request));

    return new Response(indexRes.body, {
      status: 200,
      headers: {
        'content-type': 'text/html;charset=UTF-8',
        ...Object.fromEntries(indexRes.headers),
      },
    });
  },
};

async function handleNewsletter(request) {
  try {
    const formData = await request.formData();
    const email = formData.get('email') || '';

    if (!email || !email.includes('@')) {
      const html = buildPage('❌ Neispravna email adresa', 'Molimo unesite validnu email adresu.');
      return new Response(html, { headers: { 'content-type': 'text/html;charset=UTF-8' } });
    }

    // Forward to BloomOS VPS
    const payload = JSON.stringify({ email, source: 'bixie.ba', timestamp: new Date().toISOString() });
    try {
      await fetch('http://204.168.130.130:3344/api/newsletter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
      });
    } catch (e) {
      console.error('BloomOS forward failed:', e.message);
    }

    const html = buildPage('✅ Uspješno ste prijavljeni!', 'Hvala na prijavi. Uskoro ćete primati najnovije vijesti.');
    return new Response(html, {
      status: 200,
      headers: { 'content-type': 'text/html;charset=UTF-8' },
    });
  } catch (error) {
    return new Response('Error processing request', { status: 500 });
  }
}

function buildPage(title, message) {
  return `<html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="3;url=/blog"></head>
<body style="background:#08090a;color:#d0d6e0;font-family:system-ui;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center;flex-direction:column;gap:12px">
  <h2 style="color:#f7f8f8;">${title}</h2>
  <p style="color:#8a8f98;">${message}</p>
  <a href="/blog" style="color:#5e6ad2;">← Nazad na blog</a>
</body></html>`;
}
