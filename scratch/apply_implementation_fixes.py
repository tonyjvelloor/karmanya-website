import json
import glob
import re
import os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# ===================================================
# FIX 1: Remove "3+ Years" stat, rebalance to 3-col
# ===================================================
with open(f"{base_dir}/data/site.json", "r") as f:
    site = json.load(f)

site['positioning']['metrics'] = [
    {"value": "5,000+", "label": "Patients Treated"},
    {"value": "100%", "label": "Physician-Prescribed Therapies"},
    {"value": "4.9/5", "label": "Google Patient Rating"}
]

# Fix whatsapp_url to include canonical message
CANONICAL_WA_MSG = "Hello%20Karmanya%20Ayurveda%2C%20I%20would%20like%20to%20inquire%20about%20a%20consultation."
site['brand']['whatsapp_url'] = f"https://wa.me/919819820017?text={CANONICAL_WA_MSG}"

with open(f"{base_dir}/data/site.json", "w") as f:
    json.dump(site, f, indent=2)

print("✅ site.json updated: 3+ Years removed, 3-col metrics, canonical WhatsApp URL set")

# ===================================================
# FIX 2: Update all template hardcoded WhatsApp URLs to canonical message
# + Fix Rahatani/PCMC location labels
# + Fix packages section title
# + Update stats grid to 3 columns
# ===================================================
CANONICAL_WA_URL = f"https://wa.me/919819820017?text={CANONICAL_WA_MSG}"

templates = glob.glob(f'{base_dir}/templates/*.html')
for tpl_path in templates:
    with open(tpl_path, 'r') as f:
        content = f.read()

    # --- Consolidate all WhatsApp links to canonical message ---
    # Replace any wa.me URL that has a different message (Dr. Irshad bias)
    content = re.sub(
        r'https://wa\.me/919819820017(?:\?text=[^"\'>\s]*)?',
        CANONICAL_WA_URL,
        content
    )

    # --- Fix Rahatani "3 mins walk/drive" → "3 mins drive" ---
    content = content.replace('3 mins walk/drive', '3 mins drive')

    # --- Fix PCMC "Central PCMC hub" → "10–15 mins drive" ---
    content = content.replace('4.5 km &bull; Central PCMC hub', '4.5 km &bull; 10–15 mins drive')
    content = content.replace('4.5 km • Central PCMC hub', '4.5 km • 10–15 mins drive')

    # --- Reframe "Curated Therapy Packages" to not contradict "we don't sell packages" ---
    content = content.replace(
        '<h2 style="font-size: clamp(2.2rem, 4vw, 3.2rem); color: var(--color-primary);">Curated Therapy Packages</h2>',
        '<h2 style="font-size: clamp(2.2rem, 4vw, 3.2rem); color: var(--color-primary);">Physician-Prescribed Therapy Sessions</h2>'
    )
    content = content.replace(
        'Multi-therapy treatment combinations designed to synergize relaxation, detoxification, and deep physical rejuvenation with transparent tariffs.',
        'All multi-session protocols are prescribed by your consulting physician following clinical assessment. These tariffs are published for complete transparency.'
    )

    with open(tpl_path, 'w') as f:
        f.write(content)

print("✅ Templates updated: WhatsApp URLs consolidated, Rahatani/PCMC fixed, packages copy reframed")

# ===================================================
# FIX 3: Fix the stats grid → 3 columns in index.html
# ===================================================
index_path = f"{base_dir}/templates/index.html"
with open(index_path, 'r') as f:
    idx = f.read()

# Change the stats grid from grid-4 to grid-3 for the metrics section
# The metrics section has {{#positioning.metrics}} inside it
idx = idx.replace(
    '<div class="grid-4" style="text-align: center;">\n                {{#positioning.metrics}}',
    '<div class="grid-3" style="text-align: center; max-width: 900px; margin: 0 auto;">\n                {{#positioning.metrics}}'
)

# Bump CSS version
idx = re.sub(r'components\.css\?v=\d+', 'components.css?v=12', idx)
idx = re.sub(r'base\.css\?v=\d+', 'base.css?v=12', idx)

with open(index_path, 'w') as f:
    f.write(idx)

# Bump all other templates too
for tpl_path in templates:
    if 'index.html' in tpl_path:
        continue
    with open(tpl_path, 'r') as f:
        content = f.read()
    content = re.sub(r'components\.css\?v=\d+', 'components.css?v=12', content)
    content = re.sub(r'base\.css\?v=\d+', 'base.css?v=12', content)
    with open(tpl_path, 'w') as f:
        f.write(content)

print("✅ Stats grid changed to 3-col. CSS bumped to v12 across all templates.")

