#!/bin/bash
# Deploy bixie.ba (Vite/React) to Cloudflare Workers
set -e

SITE_DIR="/root/bixie-site-vite"

echo "🚀 Building & Deploying bixie.ba (React/Vite)..."

cd "$SITE_DIR"

# Build
echo "📦 Building..."
npx vite build

# The _worker.js in public/ is copied to dist/ by Vite automatically
# It handles SPA routing (replaces _redirects)

# Deploy as Worker (not Pages — Workers supports _worker.js entry)
echo "☁️ Deploying to Cloudflare Workers..."
npx wrangler deploy --assets dist

echo ""
echo "✅ Deployment complete!"
echo "   https://bixie.ba"
