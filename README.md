# FullOfJoy ASD — Sito statico

Versione statica (HTML/CSS/JS, senza WordPress) del sito di **FullOfJoy ASD** — educazione canina e sport cinofilo a Podenzano (Piacenza).

## Struttura

```
fullofjoy-static/
├── index.html              # Homepage
├── metodo.html             # Il nostro metodo
├── chi-siamo.html          # Silvia Guglieri
├── contatti.html           # Contatti + mappa
├── privacy.html            # Privacy Policy (GDPR)
├── servizi/
│   ├── puppy-training.html
│   ├── educazione-base.html
│   ├── convivenza.html
│   ├── sport-cinofili.html
│   ├── ricerca-tartufi.html
│   ├── classi-socializzazione.html
│   └── supporto-specifico.html
├── css/style.css           # Design system completo
├── js/main.js              # Menu mobile
└── assets/                 # (immagini locali — da popolare)
```

## Anteprima locale

Apri `index.html` nel browser, oppure avvia un server locale:

```bash
cd fullofjoy-static
python -m http.server 8000
# poi apri http://localhost:8000
```

## Pubblicazione su GitHub Pages

1. Crea un repository su GitHub (es. `fullofjoy-site`)
2. Carica il contenuto di questa cartella
3. Settings → Pages → Source: `main` branch, cartella `/ (root)`
4. Il sito sarà su `https://<username>.github.io/fullofjoy-site/`

Per usare il dominio `fullofjoy.it`: aggiungere un file `CNAME` con il dominio e configurare il DNS su Aruba.

## Note / da completare

- **Immagini**: hero e sezione "Perché FullOfJoy" referenziano temporaneamente le immagini sul sito WordPress (`fullofjoy.it/staging/...`). Prima della pubblicazione definitiva conviene scaricarle in `assets/` e aggiornare i `src`.
- **Form contatti**: la pagina contatti usa link diretti (telefono, email, WhatsApp). Se serve un vero form, integrare un servizio statico (es. Formspree, Netlify Forms).
- **Analytics**: aggiungere lo snippet GA4 (`G-C4D3CFZRBG`) prima della chiusura `</head>` se si vuole tracciare.
- **Dati**: C.F. 91125280338 · P.IVA 01819940337 · Sede legale Via Caselle 71/A, Podenzano (PC).

Generato il 2026-06-01.
