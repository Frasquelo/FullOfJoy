# Design: FullOfJoy ASD

The locked system. Every Hallmark run reads this first and pages share it. Change it on purpose; the file is the rule.

## System
- Genre: editorial
- Shape of the first page: Ledge hero (dark field, the six dogs along the foot), then Rows, Grid, Steps, Split, FAQ rows, a closing statement footer
- Theme: brand (the FullOfJoy green, Fraunces display, Inter body; Poppins and Caveat Brush retired)
- Axes: light/roman-serif/chromatic-green · posture: Ledge

## Tokens
`css/tokens.css` is the source of truth. The roles:
```css
:root {
  --color-paper: oklch(97.4% 0.011 100);  --color-paper-2: oklch(94.6% 0.016 120);  --color-paper-3: oklch(90.5% 0.02 135);
  --color-ink: oklch(26% 0.024 165);  --color-ink-2: oklch(38% 0.022 165);  --color-muted: oklch(47% 0.02 165);  --color-rule: oklch(85% 0.018 135);
  --color-accent: oklch(53.3% 0.109 156);  --color-accent-ink: oklch(98% 0.008 100);  --color-focus: oklch(53% 0.14 156);
  --color-ground / --color-ground-2 / --color-on-ground / --color-on-ground-muted / --color-accent-bright: the dark bands and the footer
  --color-field: the one full green band (the bite work, "senza coercizione")
  --font-display: "Fraunces", Georgia, serif;  --font-body: "Inter", system-ui, sans-serif;  --display-weight: 600;
  --radius-card: 4px;  --radius-pill: 999px;  --rule-hair: 1px;  --shadow-card: none;
}
```
The spacing scale, the type scale, the easings and the durations are the scaffold's and live in `css/tokens.css`.

## Controls
- Primary: accent fill (accent-bright on dark bands, by custom properties, one recipe) · pill · 48px
- Secondary: hairline outline, same pill and height; WhatsApp is a secondary, never a second green

## Motion
- Character: still. No entrance animation; hover moves colour and an arrow by 6px; under reduced motion everything ends at once.

## Rules of the house
- Brand: the logo SVGs in `img/` and the green stay; the photographs are the owner's.
- "Zero coercizione" has the loudest place on the page (hero headline and promise, the full green band); ENCI and FISC are small and subordinate (the quals list in Silvia's section).
- One conversion path: the incontro conoscitivo (contact form or WhatsApp). No link to the booking app on this version.
- No invented figure, quote or logo. The Google reviews are linked, never copied.

## Exports
`css/tokens.css` in this project. Tailwind, DTCG or shadcn blocks are added here on request, per `export-formats.md`.
