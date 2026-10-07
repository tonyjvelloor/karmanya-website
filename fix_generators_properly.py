import re
import os

files = [
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/scratch/generate_condition_locations.py',
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/scratch/generate_occupational_health.py'
]

for fpath in files:
    with open(fpath, 'r') as f:
        content = f.read()
    
    # We just replace the "{{seo.og_url}}" replacement line with the canonical line AND the og_url line
    if 'generate_condition_locations' in fpath:
        content = content.replace(
            "html = html.replace('{{seo.og_url}}', f\"https://karmanyaayurveda.com/treatments/local/{slug}/\")",
            "html = html.replace('{{seo.og_url}}', f\"https://karmanyaayurveda.com/treatments/local/{slug}/\")\n        html = html.replace('<head>', f'<head>\\n    <link rel=\"canonical\" href=\"https://karmanyaayurveda.com/treatments/local/{slug}/\">')"
        )
    else:
        content = content.replace(
            "html = html.replace('{{seo.og_url}}', f\"https://karmanyaayurveda.com/occupational/{slug}/\")",
            "html = html.replace('{{seo.og_url}}', f\"https://karmanyaayurveda.com/occupational/{slug}/\")\n        html = html.replace('<head>', f'<head>\\n    <link rel=\"canonical\" href=\"https://karmanyaayurveda.com/occupational/{slug}/\">')"
        )

    with open(fpath, 'w') as f:
        f.write(content)
print("Generators fixed properly!")
