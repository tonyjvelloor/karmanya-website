import os

base_dir = "/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/templates"

cta_bar_old = """    <!-- Mobile CTA Bar -->
    <div class="mobile-cta-bar">
        <a href="{{brand.whatsapp_url}}">WhatsApp</a>
        <a href="tel:{{brand.phone}}">Call</a>
        <a href="/book-consultation/">Book Consult.</a>
    </div>"""

cta_bar_new = """    <!-- Mobile CTA Bar & Tracking -->
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
        
        if cta_bar_old in content:
            content = content.replace(cta_bar_old, cta_bar_new)
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Updated {filename}")
