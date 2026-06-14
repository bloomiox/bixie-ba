// Cloudflare Workers entry — SPA fallback for React Router
// Handles static assets and falls back to index.html for client-side routing
// API routes are forwarded to the Pages Functions handlers

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // API routes pass through to the static asset server
    // Workers will serve them from the functions/ directory
    // Only needed when deployed as Workers (not Pages)

    try {
      const response = await env.ASSETS.fetch(request);
      if (response.status !== 404) {
        return response;
      }
    } catch {
      // Asset not found, fall through to SPA handler
    }

    // SPA fallback: serve index.html so React Router handles routing
    const indexUrl = new URL('/index.html', request.url);
    const indexResponse = await env.ASSETS.fetch(new Request(indexUrl, request));

    return new Response(indexResponse.body, {
      status: 200,
      headers: {
        'content-type': 'text/html;charset=UTF-8',
        ...Object.fromEntries(indexResponse.headers),
      },
    });
  },
};
