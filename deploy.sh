#!/bin/bash
# Deploy bixie.ba (Vite/React) to Cloudflare Pages
set -e

SITE_DIR="/root/bixie-site-vite"

echo "🚀 Building & Deploying bixie.ba (React/Vite)..."

cd "$SITE_DIR"

# Build
echo "📦 Building..."
npx vite build

# Copy _redirects for SPA routing
cp public/_redirects dist/_redirects 2>/dev/null || true

# Deploy
echo "☁️ Deploying to Cloudflare Pages..."
npx wrangler pages deploy dist --project-name=bixie-ba --branch=main

echo ""
echo "✅ Deployment complete!"
echo "   https://bixie.ba"
