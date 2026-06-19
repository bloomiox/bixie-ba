#!/bin/bash
set -e
cd /root/bixie-site-vite
npx wrangler deploy --assets dist 2>&1
echo "EXIT_CODE: $?"
