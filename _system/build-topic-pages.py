#!/usr/bin/env python3
"""
Build The Bitcoin Beacon topic pages from _system/catalog.csv (the canonical index).

Outputs, per beat:
  public/topics/<beat>.html   -> latest 10 stories + "Archives ->" link to the full topic archive
  public/archive/<beat>.html  -> the full history for that beat, newest first

Also rebuilds:
  public/archive.html         -> "The Archive" hub: one card per beat -> its full archive

Idempotent: safe to run every day after appending the day's rows to catalog.csv.
Run from the repo root:  python3 _system/build-topic-pages.py
"""
import csv, html, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "_system", "catalog.csv")
PUB = os.path.join(ROOT, "public")
LATEST_N = 10

# beat key -> (H1 label, short nav label, one-line description)
BEATS = [
    ("on-the-ground",        "On the Ground",        "On the Ground",     "Bitcoin as it is actually used — markets, wallets and street corners, reported from the ground up."),
    ("money-macro",          "Money & Macro",        "Money &amp; Macro", "Currencies, inflation and the macro backdrop pushing people toward bitcoin."),
    ("markets",              "Markets & Institutions","Markets",          "Treasuries, exchanges and the institutions putting bitcoin on their books."),
    ("policy-nation-states", "Policy & Nation-States","Nation-States",    "Laws, licenses and the governments deciding what bitcoin is allowed to be."),
    ("network-mining",       "Network & Mining",     "Network &amp; Mining","Miners, energy and the protocol — the machinery that keeps bitcoin running."),
    ("opinion",              "Opinion — The Take","Opinion",         "The Beacon’s argument of the day — one clear position on where bitcoin is heading."),
]
BEAT_KEYS = [b[0] for b in BEATS]
SITE = "https://thebitcoinbeacon.com"
OG_IMG = SITE + "/assets/beacon-badge-400.png"

def clean_url(u):
    u = u.strip()
    if u.endswith(".html"):
        u = u[:-5]
    if not u.startswith("/"):
        u = "/" + u
    return u

def esc(s):
    return html.escape(s, quote=True)

# ---- shared shell pieces ---------------------------------------------------
STYLE = """<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700&display=swap');
  :root{ --ink:#15130f; --muted:#6b6459; --line:#e7e3da; --accent:#e8820c; --paper:#ffffff; --wash:#faf7f1; }
  *{ box-sizing:border-box; } body{ margin:0; background:var(--paper); color:var(--ink); font-family:'Inter',system-ui,Arial,sans-serif; line-height:1.55; }
  a{ color:inherit; text-decoration:none; }
  .nav{ position:sticky; top:0; z-index:20; background:rgba(255,255,255,.94); backdrop-filter:blur(6px); border-bottom:1px solid var(--line); }
  .nav .in{ max-width:1180px; margin:0 auto; display:flex; align-items:center; gap:24px; padding:14px 24px; }
  .nav .links{ display:flex; gap:20px; font-size:13px; font-weight:600; color:#4a463f; } .nav .links a:hover{ color:var(--accent); } .nav .links a.here{ color:var(--accent); }
  .nav .sub{ background:var(--ink); color:#fff; font-size:12px; font-weight:700; padding:9px 15px; border-radius:999px; }
  .wrap{ max-width:900px; margin:0 auto; padding:0 24px 60px; }
  h1{ font-family:'Fraunces',Georgia,serif; font-size:36px; margin:34px 0 6px; }
  .intro{ color:var(--muted); margin:0 0 10px; }
  h2{ font-family:'Fraunces',serif; font-size:22px; border-top:2px solid var(--ink); padding-top:14px; margin:34px 0 6px; }
  ul{ list-style:none; margin:0; padding:0; }
  li{ border-bottom:1px solid var(--line); padding:12px 0; display:flex; gap:16px; align-items:baseline; }
  .d{ font-size:12px; color:var(--muted); white-space:nowrap; font-variant-numeric:tabular-nums; }
  .t{ font-family:'Fraunces',serif; font-size:17px; font-weight:600; } .t:hover{ color:var(--accent); }
  .p{ font-size:12px; color:var(--muted); margin-left:auto; white-space:nowrap; }
  .arch{ display:flex; align-items:center; justify-content:space-between; gap:16px; flex-wrap:wrap; margin:22px 0 0; padding:18px 20px; background:var(--wash); border:1px solid var(--line); border-radius:14px; }
  .arch .lbl{ font-size:13px; color:var(--muted); } .arch .lbl b{ color:var(--ink); }
  .arch a{ display:inline-block; background:var(--ink); color:#fff; font-weight:700; font-size:13px; padding:11px 20px; border-radius:999px; white-space:nowrap; }
  .arch a:hover{ background:var(--accent); }
  .back{ display:inline-block; margin:18px 0 0; font-size:13px; font-weight:600; color:var(--muted); } .back:hover{ color:var(--accent); }
  .cards{ display:grid; grid-template-columns:repeat(2,1fr); gap:16px; margin:26px 0 0; }
  .card{ border:1px solid var(--line); border-radius:14px; padding:20px 22px; background:var(--paper); transition:border-color .15s; }
  .card:hover{ border-color:var(--accent); }
  .card h3{ font-family:'Fraunces',serif; font-size:20px; margin:0 0 6px; }
  .card p{ color:var(--muted); font-size:13px; margin:0 0 12px; }
  .card .meta{ font-size:12px; color:var(--muted); } .card .go{ color:var(--accent); font-weight:700; }
  .cta{ background:var(--ink); color:#fff; border-radius:16px; padding:28px 24px; text-align:center; margin-top:44px; }
  .cta h3{ font-family:'Fraunces',serif; font-size:22px; margin:0 0 6px; } .cta p{ color:#c9c3b8; margin:0 0 14px; font-size:14px; }
  .cta .btn{ display:inline-block; background:var(--accent); color:#fff; font-weight:700; padding:12px 22px; border-radius:999px; font-size:14px; }
  @media(max-width:640px){ .nav .links{ display:none; } .p{ display:none; } .cards{ grid-template-columns:1fr; } }

  /* two-tier masthead (2026-07-06) */
  .mast{ background:var(--paper); border-bottom:1px solid var(--line); }
  .mast a{ display:flex; align-items:center; justify-content:center; gap:18px; padding:20px 24px 16px; }
  .mast img{ height:119px; width:119px; border-radius:50%; }
  .mast span{ font-family:'Fraunces',Georgia,serif; font-weight:700; font-size:42px; letter-spacing:-.5px; color:var(--ink); }
  .nav .in{ position:relative; justify-content:center; }
  .nav .sub{ position:absolute; right:24px; top:50%; transform:translateY(-50%); margin-left:0; }
  .nav .menu-btn{ position:absolute; left:14px; top:50%; transform:translateY(-50%); }
  @media(max-width:768px){
    .mast a{ gap:10px; padding:12px 14px 10px; }
    .mast img{ height:74px; width:74px; }
    .mast span{ font-size:23px; }
    .nav .sub{ position:absolute; right:14px; }
  }

  /* mobile polish (2026-07-06c): deep stacked header, no slide bar */
  html{ -webkit-text-size-adjust:100%; }
  @media(max-width:768px){
    .mast a{ gap:12px; padding:18px 14px 12px; }
    .mast img{ height:64px; width:64px; }
    .mast span{ font-size:24px; letter-spacing:-.3px; }
    .nav{ position:static !important; background:var(--paper) !important; backdrop-filter:none !important; }
    .nav .in{ flex-direction:column !important; align-items:center; padding:12px 14px 16px !important; gap:0 !important; }
    .nav .links{ display:flex !important; flex-direction:row !important; flex-wrap:wrap !important; justify-content:center; overflow:visible !important; gap:9px 18px; padding:0 !important; margin:0; width:100%; font-size:13.5px; position:static !important; box-shadow:none !important; background:transparent !important; border:0 !important; }
    .nav .links a{ white-space:nowrap; border-top:0 !important; padding:0 !important; font-size:13.5px !important; }
    .nav .sub{ display:inline-block !important; position:static !important; transform:none !important; margin:14px auto 0 !important; padding:9px 26px; box-shadow:none !important; font-size:13px; }
    .nav .menu-btn{ display:none !important; }
  }
</style>"""

def nav_html(current=None):
    links = []
    for key, _h1, navlabel, _desc in BEATS:
        cls = ' class="here"' if key == current else ''
        links.append(f'<a href="/topics/{key}.html"{cls}>{navlabel}</a>')
    return (
        '<div class="mast"><a href="/">\n'
        '    <img src="/assets/beacon-badge-400.png" alt="The Bitcoin Beacon" width="400" height="400">\n'
        '    <span>The Bitcoin Beacon</span>\n'
        '  </a></div>\n'
        '  <div class="nav"><div class="in">\n'
        '    <div class="links">' + "".join(links) + '</div>\n'
        '    <a class="sub" href="/subscribe.html" style="margin-left:auto;">Subscribe</a>\n'
        '  </div></div>'
    )

MODAL = """<!-- subscribe modal (site-wide) -->
<style>
.bb-modal{position:fixed;inset:0;z-index:100;display:none;align-items:center;justify-content:center;background:rgba(21,19,15,.62);padding:20px;}
.bb-modal.open{display:flex;}
.bb-modal .bb-card{background:#faf7f1;border-radius:16px;max-width:620px;width:100%;padding:16px 16px 8px;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.35);}
.bb-modal .bb-x{position:absolute;top:6px;right:12px;background:none;border:0;font-size:28px;color:#6b6459;cursor:pointer;line-height:1;}
.bb-modal iframe{width:100%;height:340px;border:0;border-radius:10px;background:#fff;}
</style>
<div class="bb-modal" id="bb-modal" role="dialog" aria-modal="true" aria-label="Subscribe to The Bitcoin Beacon">
  <div class="bb-card">
    <button class="bb-x" aria-label="Close">&times;</button>
    <iframe data-src="https://subscribe-forms.beehiiv.com/2c9c948c-bcee-4d82-ad46-d31816c72af4" title="Subscribe to The Bitcoin Beacon"></iframe>
  </div>
</div>
<script>
(function(){
  var m=document.getElementById('bb-modal');if(!m)return;
  var f=m.querySelector('iframe');
  function open(e){if(e)e.preventDefault();if(!f.src)f.src=f.getAttribute('data-src');m.classList.add('open');document.body.style.overflow='hidden';}
  function close(){m.classList.remove('open');document.body.style.overflow='';}
  document.addEventListener('click',function(e){
    var a=e.target.closest('a');if(!a)return;
    var h=a.getAttribute('href')||'';
    if(/subscribe\\.html$/.test(h)||h==='#subscribe'){open(e);}
  });
  m.addEventListener('click',function(e){if(e.target===m)close();});
  m.querySelector('.bb-x').addEventListener('click',close);
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();
</script>"""

CTA = ('<div class="cta"><h3>The world’s bitcoin headlines, in your inbox every morning.</h3>'
       '<p>Free. Five minutes. No hype.</p><a class="btn" href="/subscribe.html">Subscribe free</a></div>')
FOOTER = ('<footer style="border-top:1px solid var(--line); padding:26px 24px; text-align:center; color:var(--muted); font-size:12px;">'
          'THE BITCOIN BEACON &bull; The daily record of Bitcoin\'s global adoption &bull; Informational only — not financial advice</footer>')

def li_html(r):
    date = esc(r["date"])
    url = clean_url(r["url"])
    title = esc(r["title"])
    place = esc(r["place"])
    return (f'<li><span class="d">{date}</span>'
            f'<a class="t" href="{url}">{title}</a>'
            f'<span class="p">{place}</span></li>')

def page(head_title, desc, canonical, body, current=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(head_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#15130f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta property="og:site_name" content="The Bitcoin Beacon">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(head_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{OG_IMG}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(head_title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{OG_IMG}">
{STYLE}
</head>
<body>
{nav_html(current)}
<div class="wrap">
{body}
{CTA}
</div>
{FOOTER}

{MODAL}
</body>
</html>"""

def main():
    rows = [r for r in csv.DictReader(open(CATALOG)) if r["status"].strip() == "published"]
    # newest first; stable sort keeps catalog (ascending) order within a date
    rows.sort(key=lambda r: r["date"], reverse=True)
    by_beat = {k: [r for r in rows if r["beat"].strip() == k] for k in BEAT_KEYS}

    os.makedirs(os.path.join(PUB, "topics"), exist_ok=True)
    os.makedirs(os.path.join(PUB, "archive"), exist_ok=True)

    for key, h1, _nav, desc in BEATS:
        items = by_beat[key]
        total = len(items)
        latest = items[:LATEST_N]
        older = max(0, total - LATEST_N)

        # ---- topic landing: latest 10 ----
        lst = "\n".join(li_html(r) for r in latest)
        if older > 0:
            arch = (f'<div class="arch"><div class="lbl">Showing the latest {len(latest)} of <b>{total}</b> '
                    f'{h1.split(" — ")[0]} stories.</div>'
                    f'<a href="/archive/{key}.html">Full archive &rarr;</a></div>')
        else:
            arch = (f'<div class="arch"><div class="lbl">All <b>{total}</b> {h1.split(" — ")[0]} stories.</div>'
                    f'<a href="/archive/{key}.html">Open archive &rarr;</a></div>')
        body = f'<h1>{h1}</h1>\n<p class="intro">{desc}</p>\n<ul>\n{lst}\n</ul>\n{arch}'
        out = page(f"{h1.split(' — ')[0]} — The Bitcoin Beacon", desc,
                   f"{SITE}/topics/{key}", body, current=key)
        open(os.path.join(PUB, "topics", f"{key}.html"), "w").write(out)

        # ---- full archive ----
        lst_all = "\n".join(li_html(r) for r in items)
        label = h1.split(" — ")[0]
        body_a = (f'<h1>{label} — Archive</h1>\n'
                  f'<p class="intro">Every {label} story we’ve run — <b>{total}</b> in all, newest first.</p>\n'
                  f'<ul>\n{lst_all}\n</ul>\n'
                  f'<a class="back" href="/topics/{key}.html">&larr; Back to latest {label}</a>'
                  f'<a class="back" href="/archive.html" style="margin-left:20px;">All topics &rarr;</a>')
        out_a = page(f"{label} — Archive — The Bitcoin Beacon",
                     f"Every {label} story from The Bitcoin Beacon, newest first.",
                     f"{SITE}/archive/{key}", body_a, current=key)
        open(os.path.join(PUB, "archive", f"{key}.html"), "w").write(out_a)

    # ---- archive.html hub ----
    cards = []
    for key, h1, _nav, desc in BEATS:
        label = h1.split(" — ")[0]
        total = len(by_beat[key])
        cards.append(
            f'<a class="card" href="/archive/{key}.html"><h3>{label}</h3>'
            f'<p>{desc}</p>'
            f'<div class="meta"><b>{total}</b> stories &middot; <span class="go">Open archive &rarr;</span></div></a>')
    body_hub = ('<h1>The Archive</h1>\n'
                '<p class="intro">Every story we’ve run, grouped by beat. Pick a topic to browse its full history.</p>\n'
                '<div class="cards">\n' + "\n".join(cards) + '\n</div>')
    hub = page("Archive — The Bitcoin Beacon",
               "Every story The Bitcoin Beacon has published, grouped by beat — Bitcoin adoption reported from the ground up, daily.",
               f"{SITE}/archive", body_hub)
    open(os.path.join(PUB, "archive.html"), "w").write(hub)

    print("Built topic + archive pages for", len(BEATS), "beats;", len(rows), "published stories.")
    for key, h1, _n, _d in BEATS:
        print(f"  {key:22} {len(by_beat[key]):3}  -> topics/{key}.html, archive/{key}.html")

if __name__ == "__main__":
    main()
