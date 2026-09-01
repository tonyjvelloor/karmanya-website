import os
import re

base_dir = "/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/templates"

# Regex to match the mobile-cta-bar block exactly, however it's formatted.
pattern = re.compile(r'<!-- Mobile CTA Bar(?: & Tracking)? -->\s*(?:<script>.*?</script>\s*)?<div class="mobile-cta-bar">.*?</div>', re.DOTALL)

cta_bar_new = """<!-- Mobile CTA Bar & Tracking -->
    <script>window.dataLayer = window.dataLayer || [];</script>
    <div class="mobile-cta-bar">
        <a href="{{brand.whatsapp_url}}" onclick="window.dataLayer.push({'event':'whatsapp_click'})" target="_blank" rel="noopener">WhatsApp</a>
        <a href="tel:{{brand.phone}}" onclick="window.dataLayer.push({'event':'phone_click'})">Call</a>
        <a href="/book-consultation/" onclick="window.dataLayer.push({'event':'book_consultation_click'})">Book Consult.</a>
    </div>"""

for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
        
        if 'mobile-cta-bar' in content:
            content = pattern.sub(cta_bar_new, content)
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Regex Updated {filename}")
