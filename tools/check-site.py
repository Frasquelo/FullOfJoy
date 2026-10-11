"""Controlli prima del lancio.

  python tools/check-site.py                       controlli sui file (link interni, SEO, immagini, sitemap)
  python tools/check-site.py --live https://sito   in più: ogni URL della sitemap deve rispondere 200,
                                                   i 301 di _redirects devono puntare dove devono
                                                   e i file di lavoro devono dare 404

Esce con codice 1 se trova errori (warning = solo avviso).
"""
import glob, os, re, sys, json, urllib.request, urllib.error
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors, warns = [], []
def err(m): errors.append(m)
def warn(m): warns.append(m)

def read(p):
    return open(p, encoding="utf-8-sig").read()

pages = sorted(p for p in glob.glob("**/*.html", recursive=True)
               if not p.startswith(("_", "tools/", "node_modules/")) and "googlee" not in p)
bridge = {"educazione-di-base-e-avanzata/index.html", "il-nostro-metodo/index.html",
          "la-storia-di-joy-amore-e-perdita-di-un-husky/index.html", "simply_galleries/index.html"}
real = [p for p in pages if p not in bridge and p not in ("404.html", "stile.html")]

titles = {}
for p in real:
    h = read(p)
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    if not t: err(f"{p}: manca <title>")
    else:
        titles.setdefault(t.group(1).strip(), []).append(p)
        if len(t.group(1).strip()) > 65: warn(f"{p}: title lungo ({len(t.group(1).strip())})")
    if not d: err(f"{p}: manca la description")
    elif len(d.group(1)) > 160: warn(f"{p}: description lunga ({len(d.group(1))})")
    if len(re.findall(r"<h1[ >]", h)) != 1: err(f"{p}: servono esattamente un h1")
    if 'rel="canonical"' not in h: err(f"{p}: manca il canonical")
    if "og:image" not in h: err(f"{p}: manca og:image")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(m)
        except Exception as e: err(f"{p}: JSON-LD non valido ({e})")
    for i in re.findall(r"<img\b[^>]*>", h):
        if "alt=" not in i: err(f"{p}: immagine senza alt: {i[:70]}")
    for a in re.findall(r'<a\b[^>]*target="_blank"[^>]*>', h):
        if "noopener" not in a: err(f"{p}: target=_blank senza rel=noopener")
    base = os.path.dirname(p)
    for href in re.findall(r'(?:href|src)="([^"#?]+)(?:[?#][^"]*)?"', h):
        if re.match(r"(https?:|mailto:|tel:|data:|javascript:|//)", href): continue
        tgt = os.path.normpath(os.path.join(ROOT, href.lstrip("/")) if href.startswith("/") else os.path.join(base, href))
        if os.path.isdir(tgt): tgt = os.path.join(tgt, "index.html")
        if not os.path.exists(tgt): err(f"{p}: link/risorsa non trovata: {href}")
    if "fullofjoy-prenotazioni.vercel.app" in h: warn(f"{p}: usa ancora il dominio Vercel per le prenotazioni")
for t, ps in titles.items():
    if len(ps) > 1: err(f"title duplicato '{t[:50]}': {ps}")

sm = re.findall(r"<loc>https://www\.fullofjoy\.it/(.*?)</loc>", read("sitemap.xml"))
smf = {(s + "index.html") if s.endswith("/") or s == "" else s for s in sm}
for f in smf:
    if not os.path.exists(f): err(f"sitemap: il file {f} non esiste")
for p in real:
    if p not in smf: warn(f"{p}: non è in sitemap")
noidx = [p for p in real if "noindex" in read(p)]
if noidx: warn(f"{len(noidx)} pagine hanno ancora noindex (corretto in staging; al lancio: python tools/robots-mode.py production)")

# ---- controlli sul sito pubblicato
def fetch(url):
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    op = urllib.request.build_opener(NoRedirect)
    try:
        r = op.open(urllib.request.Request(url, headers={"User-Agent": "check-site"}), timeout=20)
        return r.status, r.headers.get("Location")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location")
    except Exception as e:
        return 0, str(e)

if "--live" in sys.argv:
    base = sys.argv[sys.argv.index("--live") + 1].rstrip("/")
    for f in sorted(smf):
        path = "" if f == "index.html" else f
        code, _ = fetch(f"{base}/{path}")
        if code != 200: err(f"live: {base}/{path} risponde {code}")
    for line in read("_redirects").splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[0].startswith("/") and parts[2].rstrip("!") in ("301", "404"):
            code, loc = fetch(base + parts[0].replace("*", "x"))
            want = int(parts[2].rstrip("!"))
            if code != want: err(f"live: {parts[0]} risponde {code}, atteso {want}")
            elif want == 301 and not (loc or "").endswith(parts[1]): err(f"live: {parts[0]} punta a {loc}, atteso {parts[1]}")
    for extra in ("/robots.txt", "/sitemap.xml", "/404-che-non-esiste"):
        code, _ = fetch(base + extra)
        if extra.endswith("esiste"):
            if code != 404: err(f"live: una pagina inesistente risponde {code}, atteso 404")
        elif code != 200: err(f"live: {extra} risponde {code}")

print(f"{len(real)} pagine controllate")
for m in warns: print("  avviso:", m)
for m in errors: print("  ERRORE:", m)
print("OK" if not errors else f"{len(errors)} errori")
sys.exit(1 if errors else 0)
