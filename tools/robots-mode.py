"""Staging <-> produzione: aggiunge o toglie il meta robots noindex da tutte le pagine.
Uso:  python tools/robots-mode.py staging      (GitHub Pages di prova: noindex, follow)
      python tools/robots-mode.py production   (dominio definitivo: nessun noindex)
"""
import sys, glob, re, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
mode = sys.argv[1] if len(sys.argv) > 1 else ""
TAG = '<!-- STAGING: rimuovere al lancio (tools/robots-mode.py production) -->\n<meta name="robots" content="noindex, follow">'
pages = [f for f in glob.glob("*.html") + glob.glob("servizi/*.html") if "googlee" not in f and f not in ("stile.html", "404.html")]
n = 0
for f in pages:
    s = open(f, encoding="utf-8").read(); o = s
    if mode == "production":
        s = s.replace(TAG + "\n", "")
    elif mode == "staging":
        if 'name="robots"' not in s:
            s = s.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + TAG, 1)
    else:
        print(__doc__); sys.exit(1)
    if s != o:
        open(f, "w", encoding="utf-8", newline="\n").write(s); n += 1
print(mode, "->", n, "pagine modificate")
