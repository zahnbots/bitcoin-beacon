#!/bin/bash
# The Bitcoin Beacon — push to GitHub (triggers Cloudflare Pages deploy).
# Fired by launchd via WatchPaths on _system/deploy.trigger, which the daily
# run writes as its FINAL step — so a push always ships a complete edition.
# Safe to run manually any time: bash "/Users/mzahn/bitcoin beacon/_system/auto-push.sh"
cd "/Users/mzahn/bitcoin beacon" || exit 1
/usr/bin/git add -A
if ! /usr/bin/git diff --cached --quiet; then
  /usr/bin/git commit -m "Daily edition $(date +%Y-%m-%d)"
fi
# Always push — catches commits made earlier that haven't gone out yet.
/usr/bin/git push origin main >> /tmp/bitcoinbeacon-push.log 2>&1
