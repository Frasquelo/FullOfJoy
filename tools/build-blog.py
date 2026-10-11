#!/usr/bin/env python3
"""Genera blog/index.html e blog/<slug>.html a partire da tools/blog/articles.py.

Usa servizi/brevetto-bh.html come modello per head, header e footer.
Uso:  python tools/build-blog.py
Dopo aver aggiunto/rimosso articoli lancia anche: python tools/check-site.py
"""
import html, json, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "blog"))
from articles import ARTICLES  # noqa: E402

BASE = "https://www.fullofjoy.it"
DATE = "2026-10-11"
DATE_IT = "11 ottobre 2026"
AUTHOR = "FullOfJoy ASD"
TPL = (ROOT / "servizi" / "brevetto-bh.html").read_text(encoding="utf-8")
CSS_V = re.search(r"style\.css\?v=(\d+)", TPL).group(1)

pre = TPL[: TPL.index("<title>")]
links = TPL[TPL.index('<link rel="preload"'): TPL.index("<link rel=\"canonical\"")]
header = TPL[TPL.index("<body>"): TPL.index('<main id="main-content">')]
footer = TPL[TPL.index("</main>"):]

e = html.escape


def dims(img):
    w, h = Image.open(ROOT / "img" / img).size
    return w, h


def head(title, desc, url, img, extra_ld):
    full = f"{title} | FullOfJoy ASD"
    return (
        pre
        + f"<title>{e(full)}</title>\n"
        + f'<meta name="description" content="{e(desc)}">\n'
        + links
        + f'<link rel="canonical" href="{BASE}/{url}">\n'
        + '<meta property="og:type" content="article">\n<meta property="og:locale" content="it_IT">\n'
        + '<meta property="og:site_name" content="FullOfJoy ASD">\n'
        + f'<meta property="og:url" content="{BASE}/{url}">\n'
        + f'<meta property="og:title" content="{e(full)}">\n<meta property="og:description" content="{e(desc)}">\n'
        + f'<meta property="og:image" content="{BASE}/img/{img}">\n'
        + '<meta name="twitter:card" content="summary_large_image">\n'
        + f'<meta name="twitter:title" content="{e(full)}">\n<meta name="twitter:description" content="{e(desc)}">\n'
        + f'<meta name="twitter:image" content="{BASE}/img/{img}">\n'
        + "".join(f'<script type="application/ld+json">\n{json.dumps(o, ensure_ascii=False, indent=2)}\n</script>\n' for o in extra_ld)
        + "</head>\n"
    )


def crumbs(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{BASE}/{u}"} for i, (n, u) in enumerate(items)
        ],
    }


by_slug = {a["slug"]: a for a in ARTICLES}
out_dir = ROOT / "blog"
out_dir.mkdir(exist_ok=True)

WA = "https://wa.me/393283529976?text=Ciao%2C+vorrei+informazioni+sui+percorsi+di+FullOfJoy+per+il+mio+cane+%F0%9F%90%95"

for a in ARTICLES:
    url = f"blog/{a['slug']}.html"
    w, h = dims(a["img"])
    org = {"@type": "Organization", "name": "FullOfJoy ASD", "url": BASE + "/"}
    art = {
        "@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"],
        "image": f"{BASE}/img/{a['img']}", "datePublished": DATE, "dateModified": DATE,
        "author": org, "publisher": org, "mainEntityOfPage": f"{BASE}/{url}",
        "inLanguage": "it-IT",
    }
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a["faq"]],
    }
    bc = crumbs([("Home", ""), ("Blog", "blog/index.html"), (a["h1"], url)])
    rel = "".join(
        f'<a class="card post-card" href="{r}.html"><img class="card-photo" src="../img/{by_slug[r]["img"]}" alt="" width="{dims(by_slug[r]["img"])[0]}" height="{dims(by_slug[r]["img"])[1]}" loading="lazy" decoding="async">'
        f'<span class="eyebrow">{e(by_slug[r]["cat"])}</span><h3>{e(by_slug[r]["title"])}</h3><span class="card-link">Leggi l\'articolo</span></a>'
        for r in a["related"]
    )
    faqs = "".join(
        f'<details><summary>{e(q)}</summary><div class="faq-body">{e(r)}</div></details>' for q, r in a["faq"]
    )
    main = f"""<main id="main-content">

<section class="page-hero page-hero--photo" style="background-image:url('../img/{a['img']}')" id="sez1">
  <div class="container">
    <p class="breadcrumb"><a href="../index.html">Home</a> › <a href="index.html">Blog</a> › {e(a['cat'])}</p>
    <span class="eyebrow">Blog · {e(a['cat'])}</span>
    <h1>{e(a['h1'])}</h1>
    <p class="lead">{e(a['lead'])}</p>
  </div>
</section>

<article class="section" id="articolo">
  <div class="container" style="max-width:780px">
    <p class="post-meta">A cura di {AUTHOR} · {DATE_IT} · {a['mins']} minuti di lettura</p>
    <div class="prose">
{a['body'].strip()}
    </div>
    <div class="cta-box post-cta">
      <h2>Parliamo del tuo cane</h2>
      <p>Ogni cane è diverso: raccontaci la tua situazione e partiamo da un incontro conoscitivo.</p>
      <div class="btn-row" style="justify-content:center">
        <a href="../{a['svc'][0]}" class="btn btn--ghost">{e(a['svc'][1])}</a>
        <a href="../contatti.html" class="btn btn--primary">Richiedi l'incontro conoscitivo</a>
        <a href="{WA}" class="btn btn--wa" target="_blank" rel="noopener">Scrivici su WhatsApp</a>
      </div>
    </div>
  </div>
</article>

<section class="section section--alt" id="faq">
  <div class="container" style="max-width:820px">
    <div class="center"><span class="eyebrow">FAQ</span><h2>Domande frequenti</h2></div>
    <div class="faq" style="margin-top:32px">{faqs}</div>
  </div>
</section>

<section class="section" id="correlati">
  <div class="container">
    <div class="center"><h2>Continua a leggere</h2></div>
    <div class="grid grid--3 mt-40">{rel}</div>
  </div>
</section>

"""
    (out_dir / f"{a['slug']}.html").write_text(head(a["title"], a["desc"], url, a["img"], [art, faq, bc]) + header + main + footer, encoding="utf-8")

# ---- indice del blog
cards = "".join(
    f'<a class="card post-card" href="{a["slug"]}.html"><img class="card-photo" src="../img/{a["img"]}" alt="{e(a["alt"])}" width="{dims(a["img"])[0]}" height="{dims(a["img"])[1]}" loading="lazy" decoding="async">'
    f'<span class="eyebrow">{e(a["cat"])}</span><h3>{e(a["title"])}</h3><p>{e(a["desc"])}</p><span class="card-link">Leggi l\'articolo</span></a>'
    for a in ARTICLES
)
idx_main = f"""<main id="main-content">

<section class="page-hero" id="sez1">
  <div class="container">
    <p class="breadcrumb"><a href="../index.html">Home</a> › Blog</p>
    <span class="eyebrow">Blog e consigli</span>
    <h1>Consigli per vivere meglio con il tuo cane</h1>
    <p class="lead">Guide pratiche su educazione, comportamento e sport cinofili, scritte con il nostro metodo: motivazione, rispetto e zero coercizione.</p>
  </div>
</section>

<section class="section" id="articoli">
  <div class="container">
    <div class="grid grid--3">{cards}</div>
  </div>
</section>

<section class="section section--alt" id="cta">
  <div class="container">
    <div class="cta-box">
      <h2>Non trovi la tua situazione?</h2>
      <p>Raccontaci il tuo cane: ti aiutiamo a capire da dove iniziare.</p>
      <div class="btn-row" style="justify-content:center">
        <a href="../contatti.html" class="btn btn--primary">Richiedi l'incontro conoscitivo</a>
        <a href="{WA}" class="btn btn--wa" target="_blank" rel="noopener">Scrivici su WhatsApp</a>
      </div>
    </div>
  </div>
</section>

"""
idx_ld = [
    {"@context": "https://schema.org", "@type": "Blog", "name": "Blog FullOfJoy", "url": f"{BASE}/blog/index.html",
     "inLanguage": "it-IT", "publisher": {"@type": "Organization", "name": "FullOfJoy ASD", "url": BASE + "/"}},
    crumbs([("Home", ""), ("Blog", "blog/index.html")]),
]
(out_dir / "index.html").write_text(
    head("Blog: consigli su educazione cinofila e sport", "Guide pratiche su cuccioli, guinzaglio, richiamo, cani reattivi, brevetti e sport cinofili, con un metodo senza coercizione. A cura di FullOfJoy ASD, Podenzano (Piacenza).",
         "blog/index.html", "hero-cani.webp", idx_ld) + header + idx_main + footer, encoding="utf-8")

# ---- sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
sm = re.sub(r"\s*<url><loc>https://www\.fullofjoy\.it/blog/[^<]*</loc>.*?</url>", "", sm)
new = "".join(f"\n  <url><loc>{BASE}/blog/{n}</loc><lastmod>{DATE}</lastmod></url>" for n in ["index.html"] + [a["slug"] + ".html" for a in ARTICLES])
sm = sm.replace("</urlset>", new.lstrip("\n") and (new + "\n</urlset>"))
(ROOT / "sitemap.xml").write_text(sm, encoding="utf-8")
print(f"Generati {len(ARTICLES)} articoli + indice in blog/, sitemap aggiornata.")
