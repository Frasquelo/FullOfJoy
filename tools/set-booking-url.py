"""Cambia in tutto il sito l'indirizzo dell'app di prenotazione.

  python tools/set-booking-url.py https://prenota.fullofjoy.it
  python tools/set-booking-url.py https://fullofjoy-prenotazioni.vercel.app    (per tornare indietro)

Va lanciato SOLO quando il nuovo dominio funziona (DNS, Vercel, Supabase: vedi README).
"""
import glob, os, re, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    print(__doc__); sys.exit(1)
new = sys.argv[1].rstrip("/")
pat = re.compile(r"https://(?:fullofjoy-prenotazioni\.vercel\.app|prenota\.fullofjoy\.it)")
n = files = 0
for f in glob.glob("**/*.html", recursive=True) + glob.glob("*.md") + glob.glob("js/*.js"):
    if f.startswith(("node_modules/", "_foto-review/")): continue
    raw = open(f, "rb").read()
    s = raw.decode("utf-8")
    t, k = pat.subn(new, s)
    if k and t != s:
        open(f, "wb").write(t.encode("utf-8")); n += k; files += 1
print(f"{n} link aggiornati in {files} file -> {new}")
