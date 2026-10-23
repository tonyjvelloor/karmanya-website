import json
import os
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(os.path.join(base_dir, 'templates', 'index.html'), 'r') as f:
    base_html = f.read()

with open(os.path.join(base_dir, 'data', 'conditions.json'), 'r') as f:
    conditions = json.load(f)

with open(os.path.join(base_dir, 'data', 'locations.json'), 'r') as f:
    locations = json.load(f)

template_html = """
<div style="background: var(--color-bg); border-bottom: 1px solid var(--color-border); padding: var(--space-8) 0;">
    <div class="container">
        <div style="max-width: 800px;">
            <p style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: var(--space-2);">100% NON-SURGICAL CARE NEAR {loc_name}</p>
            <h1 style="font-size: clamp(2rem, 4vw, 3rem); line-height: 1.1; margin-bottom: var(--space-4); font-family: var(--font-serif); color: var(--color-primary);">{heading_title} in {loc_name}, Pune</h1>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #555; margin-bottom: var(--space-6);">Looking for authentic {cond_title} near {loc_name}? Karmanya Ayurveda provides physician-led, traditional Kerala therapies {distance} at our flagship Pimple Saudagar clinic.</p>
            <a href="https://wa.me/919819820017?text=Hello%20Karmanya%20Ayurveda,%20I%20live%20in%20{loc_name}%20and%20want%20to%20consult%20for%20{cond_title}." class="btn btn-primary" style="background: var(--color-accent); color: var(--color-primary); padding: 12px 24px; font-weight: 700;">Consult an Expert Doctor Today</a>
        </div>
    </div>
</div>

<div class="container" style="padding: var(--space-12) 0;">
    <div class="grid-2" style="gap: var(--space-12);">
        <div>
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); margin-bottom: var(--space-4);">Why Patients from {loc_name} Choose Us for {cond_title}</h2>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #444; margin-bottom: var(--space-4);">
                While there are general spas offering massage packages, clinical treatment for <strong>{cond_title}</strong> requires medical expertise. Karmanya Ayurveda is a specialized medical center operating under the direct supervision of qualified BAMS/MD Ayurvedic physicians.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #444; margin-bottom: var(--space-6);">
                {cond_desc}
            </p>
            
            <h3 style="font-family: var(--font-serif); color: var(--color-primary); margin-bottom: var(--space-3);">Commute from {loc_name}</h3>
            <div style="background: rgba(26,61,43,0.03); padding: var(--space-6); border-radius: 8px; border-left: 4px solid var(--color-accent);">
                <p style="margin: 0 0 10px 0;"><strong>Distance:</strong> {distance}</p>
                <p style="margin: 0 0 10px 0;"><strong>Drive Time:</strong> {drive_time}</p>
                <p style="margin: 0;"><strong>Directions:</strong> {landmarks}</p>
            </div>
        </div>
        
        <div>
            <div style="background: white; border: 1px solid var(--color-border); padding: var(--space-8); border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
                <h3 style="font-family: var(--font-serif); color: var(--color-primary); margin-bottom: var(--space-4); font-size: 1.5rem;">Clinical Approach to {cond_title}</h3>
                <p style="color: #555; line-height: 1.5; margin-bottom: var(--space-4);">
                    {cond_approach}
                </p>
                <div style="margin-top: var(--space-6); text-align: center;">
                    <a href="/conditions/{cond_slug}/" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">Read the full clinical guide for {cond_title}</a>
                </div>
            </div>
        </div>
    </div>
</div>
"""

count = 0
for cond in conditions:
    for loc in locations:
        if loc['slug'] == 'pimple-saudagar': continue
        
        slug = f"{cond['slug']}-{loc['slug']}"
        page_dir = os.path.join(base_dir, 'public', 'treatments', 'local', slug)
        os.makedirs(page_dir, exist_ok=True)
        
        heading_title = "Kerala Ayurveda" if cond['slug'] == 'kerala-ayurveda' else f"{cond['title']} Treatment"
        
        main_content = template_html.format(
            loc_name=loc['name'],
            cond_title=cond['title'],
            heading_title=heading_title,
            distance=loc['transit']['distance'],
            cond_desc=cond['marketing']['hero_description'],
            drive_time=loc['transit']['drive_time'],
            landmarks=loc['transit']['landmarks'],
            cond_approach=cond['clinical']['approach'],
            cond_slug=cond['slug']
        )
        
        if cond['slug'] == 'kerala-ayurveda':
            meta_title = f"Kerala Ayurveda in {loc['name']}, Pune | Authentic Kerala Clinic"
            meta_desc = f"Looking for authentic Kerala Ayurveda in {loc['name']}, Pune? Karmanya Ayurveda provides physician-led Ashtavaidya treatments and Panchakarma {loc['transit']['distance']} away."
        else:
            meta_title = f"{cond['title']} Treatment in {loc['name']}, Pune | Ayurvedic Doctor"
            meta_desc = f"Looking for Ayurvedic treatment for {cond['title']} in {loc['name']}? Karmanya Ayurveda provides physician-led, non-surgical therapies {loc['transit']['distance']} away."
        
        head_tags = f"""<title>{meta_title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://karmanyaayurveda.com/treatments/local/{slug}/">
    <meta property="og:title" content="{meta_title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://karmanyaayurveda.com/treatments/local/{slug}/">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="{loc['name']}, Pune">"""
        
        html = base_html.replace('{{seo_head_tags}}', head_tags)
        
        # Replace hero block with empty string, we provide our own
        html = re.sub(r'<!-- HERO BLOCK -->.*?<!-- END HERO BLOCK -->', '', html, flags=re.DOTALL)
        
        # Inject main content
        html = html.replace('<!-- DYNAMIC_CONTENT -->', main_content)
        html = html.replace('<!-- LOCAL_SCHEMA -->', '') 
        
        with open(os.path.join(page_dir, 'index.html'), 'w') as f:
            f.write(html)
        count += 1

print(f"✅ Generated {count} Condition + Location pSEO intersection pages in /public/treatments/local/")
