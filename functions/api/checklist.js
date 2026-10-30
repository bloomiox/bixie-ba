import { PDF_B64 } from './_checklistPdf.js';

const CONTACT_API = 'https://api.bloom.ba/api/contact';
const SECRET = 'bixie-checklist-2026-gate-v1';   // nije tajna vrijednost, samo potpis cookieja
const COOKIE = 'bm_ck';
const TTL = 60 * 60 * 24 * 30;

function b64url(buf) {
  return btoa(String.fromCharCode(...new Uint8Array(buf)))
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function sign(value) {
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(SECRET),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return b64url(await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(value)));
}

async function makeToken(email) {
  const exp = Math.floor(Date.now() / 1000) + TTL;
  const body = `${email}|${exp}`;
  return `${btoa(email)}.${exp}.${await sign(body)}`;
}

async function validToken(tok) {
  if (!tok) return false;
  const parts = tok.split('.');
  if (parts.length !== 3) return false;
  const email = atob(parts[0]);
  const exp = Number(parts[1]);
  if (!email || !exp || exp < Date.now() / 1000) return false;
  return (await sign(`${email}|${exp}`)) === parts[2];
}

function pdfResponse() {
  const bin = atob(PDF_B64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new Response(bytes, {
    headers: {
      'Content-Type': 'application/pdf',
      'Content-Disposition': 'attachment; filename="BIXIE-AI-Readiness-Checklist.pdf"',
      'Cache-Control': 'private, max-age=0, must-revalidate',
    },
  });
}

function cors(origin) {
  return {
    'Access-Control-Allow-Origin': origin || 'https://bixie.ba',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Credentials': 'true',
  };
}

export async function onRequest(context) {
  const { request } = context;
  const origin = request.headers.get('Origin') || '';
  const url = new URL(request.url);
  const cookie = request.headers.get('Cookie') || '';
  const authed = await validToken((cookie.match(new RegExp(COOKIE + '=([^;]+)')) || [])[1]);

  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: cors(origin) });
  }

  if (request.method === 'POST') {
    let data;
    try { data = await request.json(); } catch { data = {}; }
    const email = String(data.email || '').trim().toLowerCase();
    const name = String(data.name || '').trim();
    if (!/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(email)) {
      return new Response(JSON.stringify({ ok: false, error: 'email' }), {
        status: 400, headers: { 'Content-Type': 'application/json', ...cors(origin) },
      });
    }
    try {
      const r = await fetch(CONTACT_API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: name || email, email, company: '', size: '', focus: 'AI Readiness Checklist',
          message: 'Preuzimanje AI Readiness Checklist (PDF)', source: 'bixie.ba/downloads/ai-readiness-checklist',
        }),
      });
      if (!r.ok) throw new Error('contact ' + r.status);
    } catch (e) {
      return new Response(JSON.stringify({ ok: false, error: 'lead' }), {
        status: 502, headers: { 'Content-Type': 'application/json', ...cors(origin) },
      });
    }
    const token = await makeToken(email);
    return new Response(JSON.stringify({ ok: true, download: url.pathname }), {
      headers: {
        'Content-Type': 'application/json',
        'Set-Cookie': `${COOKIE}=${token}; Path=/; Max-Age=${TTL}; HttpOnly; Secure; SameSite=Lax`,
        ...cors(origin),
      },
    });
  }

  if (!authed) {
    return Response.redirect('https://bixie.ba/ai-audit/?checklist=1#forma', 302);
  }
  return pdfResponse();
}
