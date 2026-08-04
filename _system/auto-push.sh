#!/bin/bash
# The Bitcoin Beacon — push the site to GitHub (Cloudflare Pages auto-deploys).
# Safe to run any time, as often as you like:  bash "/Users/mzahn/bitcoin beacon/_system/auto-push.sh"
# Also fired automatically by launchd when the daily run writes _system/deploy.trigger.

cd "/Users/mzahn/bitcoin beacon" || { echo "ERROR: beacon folder not found"; exit 1; }

# Clear a stale lock left by a crashed git process (only when git isn't running)
if [ -f .git/index.lock ] && ! /usr/bin/pgrep -x git >/dev/null; then
  rm -f .git/index.lock && echo "Cleared stale git lock."
fi

/usr/bin/git add -A

if /usr/bin/git diff --cached --quiet; then
  echo "Nothing new to commit."
else
  /usr/bin/git commit -m "Daily edition $(date +%Y-%m-%d)" || { echo "ERROR: commit failed (see above)"; exit 1; }
fi

if /usr/bin/git push origin main; then
  echo "PUSHED — site deploys in ~1-2 min: https://thebitcoinbeacon.com"
else
  echo "ERROR: push failed (see above). Check network or GitHub credentials."
  exit 1
fi
