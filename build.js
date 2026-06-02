#!/usr/bin/env node
/**
 * FullOfJoy — Static Site Builder
 * ================================
 * Assembla le pagine HTML a partire da:
 *   _src/components/  → header, footer, cta-block, seo-head
 *   _src/pages/*.json → metadati SEO per ogni pagina
 *   _src/pages/*.html → contenuto unico della pagina (senza <head>, <header>, <footer>)
 *
 * Uso:
 *   node build.js            → genera tutte le pagine
 *   node build.js --watch    → rigenera al salvataggio di qualsiasi file in _src/
 *
 * Dopo aver modificato header o footer, esegui semplicemente: node build.js
 */

const fs   = require('fs');
const path = require('path');

const SRC        = path.join(__dirname, '_src');
const COMPONENTS = path.join(SRC, 'components');
const PAGES_SRC  = path.join(SRC, 'pages');
const ROOT       = __dirname;

// ── Carica componenti ──────────────────────────────────────────────────────
function loadComponent(name) {
  return fs.readFileSync(path.join(COMPONENTS, name), 'utf8');
}

// ── Sostituisce tutti i placeholder {{KEY}} ────────────────────────────────
function render(template, vars) {
  return template.replace(/\{\{(\w+)\}\}/g, (_, key) =>
    vars[key] !== undefined ? vars[key] : `{{${key}}}`
  );
}

// ── Genera BreadcrumbList JSON-LD da array items ───────────────────────────
function breadcrumbLD(items) {
  if (!items || items.length === 0) return '';
  const elements = items.map((item, i) => ({
    '@type': 'ListItem',
    position: i + 1,
    name: item.name,
    item: item.url,
  }));
  return `<script type="application/ld+json">
${JSON.stringify({ '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: elements }, null, 2)}
</script>`;
}

// ── Assembla una singola pagina ────────────────────────────────────────────
function buildPage(jsonFile) {
  const meta        = JSON.parse(fs.readFileSync(jsonFile, 'utf8'));
  const contentFile = jsonFile.replace(/\.json$/, '.html');

  if (!fs.existsSync(contentFile)) {
    console.warn(`⚠  Contenuto mancante: ${contentFile}`);
    return;
  }

  const content    = fs.readFileSync(contentFile, 'utf8');
  const rootPrefix = meta.root || '';          // '' per root, '../' per servizi/

  // Schema aggiuntivo (LocalBusiness, Person, ecc.) opzionale nel JSON
  const extraSchema = meta.schema
    ? `<script type="application/ld+json">\n${JSON.stringify(meta.schema, null, 2)}\n</script>`
    : '';

  const schemaLD = [
    extraSchema,
    breadcrumbLD(meta.breadcrumb),
  ].filter(Boolean).join('\n');

  const seoHead = render(loadComponent('seo-head.html'), {
    SEO_TITLE:   meta.title,
    SEO_DESCRIPTION: meta.description,
    CANONICAL:   meta.canonical,
    OG_TYPE:     meta.ogType || 'website',
    OG_IMAGE:    meta.ogImage || 'https://www.fullofjoy.it/assets/hero-cane.jpg',
    ROOT:        rootPrefix,
    SCHEMA_LD:   schemaLD,
  });

  const header = render(loadComponent('header.html'), { ROOT: rootPrefix });
  const footer = render(loadComponent('footer.html'), { ROOT: rootPrefix });

  const html = `<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-C4D3CFZRBG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-C4D3CFZRBG');
</script>

${seoHead}
</head>
<body>

${header}

${content}

${footer}

<script src="${rootPrefix}js/main.js?v=3"></script>
</body>
</html>`;

  const outDir  = path.join(ROOT, meta.outputDir || '');
  const outFile = path.join(outDir, meta.outputFile);
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(outFile, html, 'utf8');
  console.log(`✅  ${meta.outputFile}  →  ${path.relative(ROOT, outFile)}`);
}

// ── Entry point ────────────────────────────────────────────────────────────
function build() {
  console.log('\n🔨  FullOfJoy build started…\n');
  const jsonFiles = fs.readdirSync(PAGES_SRC)
    .filter(f => f.endsWith('.json'))
    .map(f => path.join(PAGES_SRC, f));

  if (jsonFiles.length === 0) {
    console.log('ℹ  Nessuna pagina in _src/pages/ — aggiungi un file .json per iniziare.');
    return;
  }

  jsonFiles.forEach(buildPage);
  console.log(`\n✨  Build completata (${jsonFiles.length} pagine)\n`);
}

build();

// ── Watch mode ─────────────────────────────────────────────────────────────
if (process.argv.includes('--watch')) {
  console.log('👀  Watch mode attivo — in ascolto su _src/…\n');
  fs.watch(SRC, { recursive: true }, (event, filename) => {
    if (filename) {
      console.log(`🔄  Modificato: ${filename}`);
      build();
    }
  });
}
