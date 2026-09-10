import glob, re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# 1. Update index.html head style for .trust-strip
with open(f'{base_dir}/templates/index.html', 'r') as f:
    idx_content = f.read()

# Replace the absolute positioning of .trust-strip in style block
old_trust_style = """.trust-strip {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(255,255,255,0.05);
            border-top: 1px solid rgba(255,255,255,0.1);
            padding: var(--space-4) 0;
            text-align: center;
            font-size: 0.9rem;
            letter-spacing: 1px;
            z-index: 1;
        }"""

new_trust_style = """.trust-strip {
            position: relative;
            width: 100%;
            background: linear-gradient(90deg, #8B6914, #D4AF37, #F3E5AB, #D4AF37, #8B6914);
            color: #1a1a1a;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.78rem;
            padding: 11px 16px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.12);
            text-align: center;
            z-index: 2;
        }"""

if old_trust_style in idx_content:
    idx_content = idx_content.replace(old_trust_style, new_trust_style)
    print("✅ Fixed .trust-strip style definition in templates/index.html")
else:
    # Use regex fallback if formatting varies
    idx_content = re.sub(
        r'\.trust-strip\s*\{[^}]*position:\s*absolute[^}]*\}',
        new_trust_style,
        idx_content
    )
    print("✅ Fixed .trust-strip style (via regex) in templates/index.html")

# Also ensure inline style has position: relative explicitly
idx_content = idx_content.replace(
    '<div class="trust-strip" style="background:',
    '<div class="trust-strip" style="position: relative; background:'
)

with open(f'{base_dir}/templates/index.html', 'w') as f:
    f.write(idx_content)


# 2. Modern, high-visibility, branded footer social section
NEW_FOOTER_BOTTOM = """            <div style="border-top: 1px solid var(--color-border); padding-top: var(--space-6); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; font-size: 0.85rem; color: #666; gap: var(--space-4);">
                <div style="line-height: 1.6;">
                    <span>&copy; 2026 Karmanya Ayurveda Chikitsalaya. Single clinic at 27/11 Swaraj Garden Road, Pimple Saudagar, Pune 411027.</span><br>
                    <span>Phone: <a href="tel:+919819820017" style="color: var(--color-primary); font-weight: 600; text-decoration: none;">+91 98198 20017</a> &bull; Mon&ndash;Sun, 10:00 AM &ndash; 8:00 PM</span>
                </div>
                <div style="display: flex; gap: 12px; align-items: center;">
                    <a href="https://www.instagram.com/karmanyaayurveda" target="_blank" rel="noopener" aria-label="Karmanya Ayurveda on Instagram" style="display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: #ffffff; box-shadow: 0 3px 10px rgba(220,39,67,0.3); transition: transform 0.2s, box-shadow 0.2s;" onmouseenter="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 5px 15px rgba(220,39,67,0.45)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 10px rgba(220,39,67,0.3)';">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                    </a>
                    <a href="https://wa.me/919819820017?text=Hello%20Karmanya%20Ayurveda%2C%20I%20would%20like%20to%20inquire%20about%20a%20consultation." target="_blank" rel="noopener" aria-label="Karmanya Ayurveda on WhatsApp" style="display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #25D366; color: #ffffff; box-shadow: 0 3px 10px rgba(37,211,102,0.35); transition: transform 0.2s, box-shadow 0.2s;" onmouseenter="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 5px 15px rgba(37,211,102,0.5)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 10px rgba(37,211,102,0.35)';">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    </a>
                    <a href="https://maps.google.com/?cid=3077549578320836260" target="_blank" rel="noopener" aria-label="Karmanya Ayurveda on Google Maps" style="display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #EA4335; color: #ffffff; box-shadow: 0 3px 10px rgba(234,67,53,0.3); transition: transform 0.2s, box-shadow 0.2s;" onmouseenter="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 5px 15px rgba(234,67,53,0.45)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 10px rgba(234,67,53,0.3)';">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </footer>"""

templates = glob.glob(f'{base_dir}/templates/*.html')
count = 0

for tpl_path in templates:
    with open(tpl_path, 'r') as f:
        content = f.read()

    # Pattern to match the entire old bottom copyright + social block through </footer>
    pattern = re.compile(
        r'<div style="border-top: 1px solid var\(--color-border\); padding-top: var\(--space-6\);.*?'
        r'<!-- Social Links -->.*?'
        r'</footer>',
        re.DOTALL
    )

    if pattern.search(content):
        content = pattern.sub(NEW_FOOTER_BOTTOM, content)
        # Also bump CSS version to v13 for cache busting
        content = re.sub(r'components\.css\?v=\d+', 'components.css?v=13', content)
        content = re.sub(r'base\.css\?v=\d+', 'base.css?v=13', content)
        with open(tpl_path, 'w') as f:
            f.write(content)
        count += 1
        print(f"  Fixed footer in: {tpl_path.split('/')[-1]}")
    else:
        print(f"  ⚠️ Pattern not matched in: {tpl_path.split('/')[-1]}")

print(f"\n✅ Successfully updated footer in {count} templates")
