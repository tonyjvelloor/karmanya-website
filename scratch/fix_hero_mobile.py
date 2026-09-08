base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(f"{base_dir}/templates/index.html", "r") as f:
    content = f.read()

# Replace the hero block
start_marker = '<div class="hero" style="text-align: center; position: relative;">'
end_marker = '<!-- Kerala Kasavu Decorative Ribbon -->'

new_hero_block = """<div class="hero" style="text-align: center; position: relative; padding: 60px 0 45px; overflow: hidden; background: var(--color-primary);">
        <!-- Malayalam Watermark for true Kerala Essence -->
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: clamp(6rem, 18vw, 22rem); color: rgba(255,255,255,0.03); font-family: sans-serif; white-space: nowrap; z-index: 1; pointer-events: none; font-weight: 800; letter-spacing: -0.05em;">
            കർമ്മണ്യ
        </div>
        
        <!-- Video / Background Image -->
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 0; opacity: 0.28;">
            <img src="/images/hero-treatment.webp" alt="Ayurvedic Treatment at Karmanya Ayurveda" style="width: 100%; height: 100%; object-fit: cover; object-position: center;">
        </div>
        
        <!-- Elegant gradient overlay to ensure text readability -->
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(180deg, rgba(23,46,39,0.92) 0%, rgba(30,61,52,0.85) 100%); z-index: 1;"></div>

        <div class="container" style="display: flex; flex-direction: column; align-items: center; position: relative; z-index: 2; max-width: 900px; padding: 0 16px;">
            <div class="reveal">
                <p style="text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem; font-weight: 700; color: #D4AF37; margin-bottom: 14px;">✦ Physician-Led Kerala Ayurvedic Treatment Centre &middot; Pimple Saudagar, Pune</p>
                <h1 style="font-size: clamp(1.9rem, 5vw, 3.8rem); line-height: 1.15; margin-bottom: 18px; color: #FFFFFF; font-weight: 400; font-family: var(--font-heading);">
                    Ayurvedic Treatment Centre<br><span style="color: #F3E5AB;">in Pimple Saudagar, Pune</span>
                </h1>
                <p style="font-size: clamp(0.95rem, 2.5vw, 1.15rem); color: rgba(255,255,255,0.92); line-height: 1.6; margin-bottom: 14px; max-width: 680px; margin-left: auto; margin-right: auto;">
                    Doctor-diagnosed. Clinically managed. Condition-specific Ayurvedic treatment for chronic pain, hormonal disorders, digestive disease, skin conditions &amp; more.
                </p>
                <p style="font-size: 0.9rem; color: rgba(255,255,255,0.65); margin-bottom: 22px; letter-spacing: 0.02em;">
                    Not a spa. A medical centre. Every patient is assessed by a qualified Ayurvedic physician before any therapy begins.
                </p>
                <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                    <a href="/book-consultation/" class="btn" style="background: #FFFFFF; color: var(--color-primary); font-weight: 700; padding: 13px 24px; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.2); font-size: 0.95rem;">Book Doctor Consultation</a>
                    <a href="/conditions/" class="btn btn-secondary" style="border: 1.5px solid rgba(255,255,255,0.4); color: #FFFFFF; background: rgba(255,255,255,0.08); padding: 13px 20px; border-radius: 8px; backdrop-filter: blur(4px); font-size: 0.95rem;">See Conditions We Treat &rarr;</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Trust Strip Banner (Responsive in document flow) -->
    <div class="trust-strip" style="background: linear-gradient(90deg, #8B6914, #D4AF37, #F3E5AB, #D4AF37, #8B6914); color: #1a1a1a; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.78rem; padding: 11px 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.12); text-align: center;">
        <div class="container" style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span>✦ Direct Kerala Ashtavaidya Lineage</span>
            <span style="opacity: 0.4;">&bull;</span>
            <span>Classical GMP Pharmacy Sourcing</span>
            <span style="opacity: 0.4;">&bull;</span>
            <span>Clinical Diagnosis First</span>
            <span style="opacity: 0.4;">&bull;</span>
            <span>Pimple Saudagar, Pune</span>
        </div>
    </div>
"""

start_pos = content.find(start_marker)
end_pos = content.find(end_marker)

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + new_hero_block + "\n    " + content[end_pos:]
    with open(f"{base_dir}/templates/index.html", "w") as f:
        f.write(content)
    print("Hero section in index.html successfully updated.")
else:
    print(f"Could not find markers: {start_pos}, {end_pos}")

