import re

scripts = [
    'scratch/generate_comparison_pages.py',
    'scratch/generate_symptoms_pages.py',
    'scratch/generate_glossary_page.py',
    'scratch/generate_blog.py',
    'scratch/generate_reviews_page.py'
]

TOP_SNIPPET = """    <!-- Top Announcement & Direct Contact Bar -->
    <div class="top-utility-bar">
        <div class="container top-utility-inner">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span class="top-utility-badge" style="color: var(--color-accent); font-weight: 700; font-size: 0.78rem; letter-spacing: 1px;">✦ PUNE'S PHYSICIAN-LED AYURVEDA</span>
                <span style="color: rgba(255,255,255,0.85); font-size: 0.82rem;">Single Clinic at Pimple Saudagar &bull; Mon–Sun: 10 AM – 8 PM</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; font-size: 0.86rem;">
                <a href="tel:+919819820017" style="font-weight: 700; display: inline-flex; align-items: center; gap: 5px;">
                    <span style="color: var(--color-accent);">&#128222;</span> +91 98198 20017
                </a>
                <a href="https://wa.me/919819820017?text=Hello%20Karmanya%20Ayurveda%2C%20I%20would%20like%20to%20inquire%20about%20a%20consultation." target="_blank" rel="noopener" style="color: #25D366; font-weight: 700; display: inline-flex; align-items: center; gap: 4px;">
                    WhatsApp &rarr;
                </a>
            </div>
        </div>
    </div>
"""

STICKY_SNIPPET = """    <!-- Mobile Sticky Action Bar -->
    <div id="mobile-sticky-bar">
        <a href="tel:+919819820017" class="mobile-sticky-btn" style="background: var(--color-primary); color: white;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            Call Clinic
        </a>
        <a href="https://wa.me/919819820017?text=Hello%20Dr.%20Irshad%2C%20I%20would%20like%20to%20book%20a%20consultation%20at%20Karmanya%20Ayurveda." target="_blank" rel="noopener" class="mobile-sticky-btn" style="background: #25D366; color: white;">
            <svg width="16" height="16" viewBox="0 0 32 32" fill="white"><path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.832 6.51L4 29l7.695-1.807A12.94 12.94 0 0016 27c6.627 0 12-5.373 12-12S22.627 3 16 3z"/></svg>
            WhatsApp
        </a>
        <a href="/book-consultation/" class="mobile-sticky-btn" style="background: var(--color-accent); color: white; flex: 0.8;">
            Book
        </a>
    </div>
"""

for s in scripts:
    with open(s) as f:
        code = f.read()
    orig = code
    
    # 1. Insert top snippet before {nav_html} if not present
    if 'top-utility-bar' not in code:
        code = code.replace('{nav_html}', TOP_SNIPPET + '\n    {nav_html}')
        
    # 2. Insert sticky snippet before </body> if not present
    if 'mobile-sticky-bar' not in code:
        code = code.replace('</body>', STICKY_SNIPPET + '\n</body>')
        
    if code != orig:
        with open(s, 'w') as f:
            f.write(code)
        print(f"  ✅ Added Top Bar & Sticky Bar to {s}")

