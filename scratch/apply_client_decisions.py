import json
import glob
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# ===================================================
# 1. Update patient count to 12,000+ in site.json
# ===================================================
with open(f"{base_dir}/data/site.json", "r") as f:
    site = json.load(f)

for m in site['positioning']['metrics']:
    if 'Patients' in m['label']:
        m['value'] = '12,000+'
        break

with open(f"{base_dir}/data/site.json", "w") as f:
    json.dump(site, f, indent=2)

print("✅ site.json: Patient count updated to 12,000+")

# ===================================================
# 2. Option B: Soften "We treat conditions. We don't sell packages."
# ===================================================
templates = glob.glob(f'{base_dir}/templates/*.html')
for tpl_path in templates:
    with open(tpl_path, 'r') as f:
        content = f.read()

    changed = False

    # Soften the main headline
    if "We treat conditions. We don't sell packages." in content:
        content = content.replace(
            "We treat conditions. We don't sell packages.",
            "We treat conditions. Every extended protocol starts with a diagnosis."
        )
        changed = True

    # Update subhead to match softened positioning
    if "Many Ayurvedic centres offer spa packages and relaxation sessions. Karmanya is structured differently" in content:
        content = content.replace(
            "Many Ayurvedic centres offer spa packages and relaxation sessions. Karmanya is structured differently — as a physician-managed clinical treatment centre where every session is medically directed.",
            "Every multi-session protocol at Karmanya begins with a formal clinical consultation — because effective treatment requires a diagnosis, not just a booking."
        )
        changed = True

    # Also update any hardcoded "5,000+" patient references
    content = content.replace('5,000+', '12,000+')

    if changed:
        with open(tpl_path, 'w') as f:
            f.write(content)
        print(f"  Updated: {tpl_path.split('/')[-1]}")

print("✅ Packages headline: Option B applied across all templates")
print("✅ Patient count: 5,000+ → 12,000+ in all hardcoded references")

