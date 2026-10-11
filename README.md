# FullOfJoy ASD — sito web

Sito statico (HTML, CSS e JavaScript, senza WordPress) di **FullOfJoy ASD**: educazione canina e sport cinofilo a Podenzano (Piacenza). Nessun passaggio di compilazione: le pagine in questa cartella sono quelle pubblicate.

## Com'è fatto

```
index.html, metodo.html, chi-siamo.html, contatti.html, prezzi.html,
galleria.html, la-storia-di-joy.html, metodo-approfondimento.html,
stage-morso-nord-italia.html, privacy.html, 404.html   pagine principali
servizi/            16 pagine, una per servizio (più l'indice)
css/style.css       tutto il design (colori, font, componenti)
js/                 main.js (menu, form, mappa al click), consent.js (cookie e GA4), tracking.js (eventi)
img/, assets/       immagini (WebP + JPG di riserva) e font in locale
_redirects          301 dai vecchi URL WordPress e blocchi (formato Netlify)
_headers            header di sicurezza e cache (formato Netlify)
tools/              strumenti per il lancio (vedi sotto)
stile.html          guida di stile interna, non pubblica e non indicizzata
_foto-review/       pagine interne di selezione foto: non pubbliche
_src/ + build.js    vecchio sistema a modelli: NON è usato dalle pagine attuali
```

**Attenzione a `build.js`:** le pagine sono scritte a mano. Lanciare `node build.js` genera pagine di esempio (oggi `nuova-pagina.html`) con un'intestazione diversa da quella attuale. Non usarlo finché non si decide di migrare tutte le pagine ai modelli.

Dopo ogni modifica al CSS o al JavaScript aumenta il numero `?v=NN` nel link, in tutte le pagine, così i browser non tengono la versione vecchia (si fa con un `sed`, come negli ultimi commit).

## Anteprima in locale

```bash
python -m http.server 8000      # poi apri http://localhost:8000
```

## Strumenti (`tools/`)

| Comando | A cosa serve |
|---|---|
| `python tools/check-site.py` | Controlla link interni, title, description, h1, canonical, JSON-LD, immagini, sitemap. Esce con errore se qualcosa non va |
| `python tools/check-site.py --live https://www.fullofjoy.it` | In più, sul sito vero: ogni URL della sitemap risponde 200, i 301 di `_redirects` puntano giusto, i file di lavoro danno 404 |
| `python tools/robots-mode.py production` / `staging` | Toglie o rimette il `noindex` da tutte le pagine |
| `python tools/set-booking-url.py https://prenota.fullofjoy.it` | Cambia in tutto il sito l'indirizzo dell'app di prenotazione |

## Stato attuale: staging

Il sito è pubblicato **solo come staging** su GitHub Pages (`frasquelo.github.io/FullOfJoy`). Tutte le pagine hanno `<meta name="robots" content="noindex, follow">`, mentre canonical, Open Graph e sitemap puntano già a `www.fullofjoy.it`. Il sito WordPress su `www.fullofjoy.it` è ancora quello online.

GitHub Pages non sa fare redirect 301 né header di sicurezza, e pubblica anche i file di lavoro (`_src/`, `tools/`, `README.md`). Per questo il lancio avviene su un altro hosting.

## Lancio su Netlify (consigliato) — nell'ordine

Perché Netlify e non Cloudflare Pages: le pagine, i canonical e la sitemap usano gli indirizzi con `.html` (`/metodo.html`). Netlify li lascia così; Cloudflare Pages li riscrive togliendo il `.html` e obbligherebbe a cambiare canonical e sitemap di tutte le pagine.

1. **Collega il repository.** Netlify → *Add new site* → *Import from GitHub* → `Frasquelo/FullOfJoy`. Comando di build: vuoto. Cartella da pubblicare: `.` (il punto). Il sito parte su un indirizzo provvisorio `nome.netlify.app`.
2. **Prova l'indirizzo provvisorio:** `python tools/check-site.py --live https://nome.netlify.app` deve finire con `OK`.
3. **Prepara il DNS su Aruba** *prima* del cambio: abbassa il TTL dei record `fullofjoy.it` e `www` (per esempio 300 secondi) e annota i valori di oggi, per tornare indietro (oggi `fullofjoy.it` e `www` puntano all'IP `89.46.108.47`, il WordPress su Aruba).
4. **Aggiungi il dominio.** Netlify → *Domain management* → aggiungi `www.fullofjoy.it` come dominio principale e `fullofjoy.it` come alias. Su Aruba imposta i record **esattamente come li mostra Netlify** (un CNAME per `www`, un record per il dominio senza www). **Non toccare MX e TXT**: la posta `info@` è su Aruba.
5. **HTTPS.** In Netlify → *HTTPS* → certificato gratuito, poi *Force HTTPS*.
6. **Togli il noindex:** `python tools/robots-mode.py production`, commit e push. Netlify ripubblica da solo.
7. **Collauda il sito vero:** `python tools/check-site.py --live https://www.fullofjoy.it` deve finire con `OK` (include i 301 dai vecchi URL WordPress).
8. **Google.** Search Console: aggiungi la proprietà `www.fullofjoy.it`, invia `sitemap.xml`, chiedi l'indicizzazione della home. In Analytics aggiorna l'indirizzo del flusso dati.
9. **Chiudi lo staging:** in GitHub → Settings → Pages disattiva la pubblicazione. Il WordPress su Aruba resta come copia di sicurezza finché sei tranquillo.

## Dominio `prenota.fullofjoy.it` (app di prenotazione)

1. Aruba: record CNAME `prenota` verso il valore che indica Vercel.
2. Vercel → progetto delle prenotazioni → *Settings → Domains* → aggiungi `prenota.fullofjoy.it`.
3. Vercel → *Environment Variables*: `NEXT_PUBLIC_SITE_URL=https://prenota.fullofjoy.it`, poi nuovo deploy.
4. Supabase → *Authentication → URL Configuration*: aggiorna *Site URL* e aggiungi `https://prenota.fullofjoy.it/**` tra i *Redirect URLs*.
5. Prova registrazione, accesso e reimpostazione password sul nuovo indirizzo.
6. Solo allora, nel sito: `python tools/set-booking-url.py https://prenota.fullofjoy.it`, commit e push.

## Dati dell'associazione

C.F. 91125280338 · P.IVA 01819940337 · Sede legale: solo nel footer (non ripeterla altrove). Campo di addestramento: Via don Luigi Sturzo, Podenzano. Analytics: GA4 `G-C4D3CFZRBG`, caricato solo dopo il consenso (`js/consent.js`). Moduli: Formspree. La Privacy Policy cita questi fornitori: se ne cambi uno, aggiornala (`privacy.html`).
