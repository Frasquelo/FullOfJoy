"""Subset del font Phosphor alle sole icone usate dal sito."""
import re
from pathlib import Path
from fontTools.subset import main as subset_main

ICONS = [
    "binoculars", "bone", "buildings", "envelope", "facebook-logo",
    "google-logo", "graduation-cap", "instagram-logo", "leaf", "map-pin",
    "medal", "megaphone", "paw-print", "phone", "shield-check", "target",
    "tree-evergreen", "trophy", "warning", "whatsapp-logo",
]

css = Path("phosphor-src.css").read_text(encoding="utf-8")
mapping = {}
for name in ICONS:
    m = re.search(
        re.escape(f".ph.ph-{name}:before") + r'\s*\{\s*content:\s*"\\([0-9a-fA-F]+)"',
        css,
    )
    if not m:
        raise SystemExit(f"icona non trovata nel CSS: {name}")
    mapping[name] = m.group(1)

unicodes = ",".join(f"U+{cp}" for cp in mapping.values())
print("Codepoints:", unicodes)

subset_main([
    "Phosphor-full.woff2",
    f"--unicodes={unicodes}",
    "--flavor=woff2",
    "--output-file=phosphor-subset.woff2",
])

Path("icon-map.txt").write_text(
    "\n".join(f"{k}={v}" for k, v in mapping.items()), encoding="utf-8"
)
size = Path("phosphor-subset.woff2").stat().st_size
print(f"phosphor-subset.woff2: {size/1024:.1f} KB")
