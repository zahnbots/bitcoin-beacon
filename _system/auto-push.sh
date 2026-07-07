#!/bin/bash
# The Bitcoin Beacon — daily auto-push to GitHub (triggers Cloudflare Pages deploy)
# Runs via launchd at 6:45 AM, after the 6:00 AM edition is built.
cd "/Users/mzahn/bitcoin beacon" || exit 1
/usr/bin/git add -A
if ! /usr/bin/git diff --cached --quiet; then
  /usr/bin/git commit -m "Daily edition $(date +%Y-%m-%d)"
fi
# Always push — catches commits made earlier that haven't gone out yet.
/usr/bin/git push origin main >> /tmp/bitcoinbeacon-push.log 2>&1
