import json
import os
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(os.path.join(base_dir, 'templates', 'index.html'), 'r') as f:
    base_html = f.read()

professions = [
    {
        "id": "it-professionals",
        "name": "IT Professionals & Software Engineers",
        "slug": "it-professionals",
        "conditions": [
            {"id": "spine-sciatica-back-pain", "name": "Lower Back Pain & Sciatica", "cause": "Prolonged sitting in ergonomically poor chairs and long hours of coding lead to severe lumbar compression and L4-L5 disc herniation."},
            {"id": "cervical-spondylosis-neck-pain", "name": "Cervical Spondylosis & Neck Stiffness", "cause": "Forward head posture ('Tech Neck') while looking at monitors causes severe cervical spine degeneration and radiating pain into the arms."},
            {"id": "stress-insomnia-anxiety", "name": "Insomnia, Stress & Burnout", "cause": "High-pressure release cycles, screen-induced blue light exposure, and irregular sleep schedules severely aggravate Vata dosha, leading to chronic insomnia."}
        ]
    },
    {
        "id": "dentists",
        "name": "Dentists & Surgeons",
        "slug": "dentists",
        "conditions": [
            {"id": "cervical-spondylosis-neck-pain", "name": "Cervical Spondylosis", "cause": "Constantly bending over patients at unnatural angles puts immense strain on the cervical spine, leading to early spondylosis."},
            {"id": "spine-sciatica-back-pain", "name": "Lower Back Pain", "cause": "Twisting the torso while seated for clinical procedures causes asymmetric wear on the lumbar discs."}
        ]
    },
    {
        "id": "teachers",
        "name": "Teachers & Professors",
        "slug": "teachers",
        "conditions": [
            {"id": "knee-joint-pain", "name": "Knee Osteoarthritis", "cause": "Standing for 6-8 hours a day in classrooms accelerates cartilage wear and tear in the weight-bearing knee joints."},
            {"id": "stress-insomnia-anxiety", "name": "Vocal Cord Strain & Stress", "cause": "Constant speaking and managing large classrooms leads to systemic exhaustion and aggravated Vata."}
        ]
    }
]

template_html = """
<div style="background: var(--color-bg); border-bottom: 1px solid var(--color-border); padding: var(--space-8) 0;">
    <div class="container">
        <div style="max-width: 800px;">
            <p style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: var(--space-2);">OCCUPATIONAL HEALTH \u2022 AYURVEDIC CARE</p>
            <h1 style="font-size: clamp(2rem, 4vw, 3rem); line-height: 1.1; margin-bottom: var(--space-4); font-family: var(--font-serif); color: var(--color-primary);">Ayurvedic Treatment for {prof_name} in Pune</h1>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #555; margin-bottom: var(--space-6);">Every profession carries its own physical toll. At Karmanya Ayurveda, we provide targeted, non-surgical clinical protocols specifically designed to reverse the chronic occupational hazards faced by {prof_name}.</p>
            <a href="https://wa.me/919819820017?text=Hello%20Karmanya%20Ayurveda,%20I%20am%20looking%20for%20a%20consultation%20regarding%20occupational%20pain." class="btn btn-primary" style="background: var(--color-accent); color: var(--color-primary); padding: 12px 24px;">Consult Our Physicians</a>
        </div>
    </div>
</div>

<div class="container" style="padding: var(--space-12) 0;">
    <div class="grid-2" style="gap: var(--space-12);">
        <div>
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); margin-bottom: var(--space-4);">Common Conditions We Treat for {prof_name}</h2>
            
            {conditions_html}
            
        </div>
        
        <div>
            <div style="background: white; border: 1px solid var(--color-border); padding: var(--space-8); border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
                <h3 style="font-family: var(--font-serif); color: var(--color-primary); margin-bottom: var(--space-4); font-size: 1.5rem;">Why Clinical Ayurveda?</h3>
                <p style="color: #555; line-height: 1.6; margin-bottom: var(--space-4);">
                    Occupational hazards cannot be permanently fixed with temporary painkillers. If your job requires you to sit for 9 hours or stand all day, the structural wear and tear will continue.
                </p>
                <p style="color: #555; line-height: 1.6; margin-bottom: var(--space-4);">
                    Our authentic Kerala Ayurvedic approach (including therapies like <strong>Kati Basti</strong> for the spine and <strong>Janu Basti</strong> for the knees) focuses on:
                </p>
                <ul style="color: #555; line-height: 1.6; margin-bottom: var(--space-6); padding-left: 20px;">
                    <li>Decompressing nerve roots trapped by bad posture.</li>
                    <li>Rehydrating dried-out spinal discs and knee cartilage.</li>
                    <li>Strengthening the surrounding musculature to prevent future injury.</li>
                </ul>
                <div style="text-align: center; background: rgba(26,61,43,0.03); padding: 15px; border-radius: 8px;">
                    <p style="margin: 0; font-weight: 600; color: var(--color-primary);">Located conveniently near Hinjawadi & Wakad</p>
                    <p style="margin: 5px 0 0 0; font-size: 0.9rem; color: #666;">27/11, Swaraj Garden Road, Pimple Saudagar</p>
                </div>
            </div>
        </div>
    </div>
</div>
"""

count = 0
for prof in professions:
    slug = f"ayurvedic-treatment-for-{prof['slug']}"
    page_dir = os.path.join(base_dir, 'public', 'occupational', slug)
    os.makedirs(page_dir, exist_ok=True)
    
    cond_html = ""
    for cond in prof['conditions']:
        cond_html += f"""
        <div style="margin-bottom: var(--space-6); padding-bottom: var(--space-6); border-bottom: 1px solid var(--color-border);">
            <h3 style="color: var(--color-accent); font-size: 1.3rem; margin-bottom: var(--space-2);">{cond['name']}</h3>
            <p style="color: #444; line-height: 1.6; margin-bottom: var(--space-2);"><strong>The Occupational Cause:</strong> {cond['cause']}</p>
            <a href="/conditions/{cond['id']}/" style="color: var(--color-primary); font-weight: 600; font-size: 0.9rem; text-decoration: underline;">Read our clinical protocol for {cond['name']} &rarr;</a>
        </div>
        """
    
    main_content = template_html.format(
        prof_name=prof['name'],
        conditions_html=cond_html
    )
    
    meta_title = f"Ayurvedic Treatment for {prof['name']} in Pune | Karmanya"
    meta_desc = f"Specialized Ayurvedic care for occupational hazards faced by {prof['name']}. Non-surgical treatment for back pain, neck strain, and stress in Pune."
    
    html = base_html
    seo_block = f'''
    <title>{meta_title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://karmanyaayurveda.com/occupational/{slug}/">
    <meta property="og:title" content="{meta_title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://karmanyaayurveda.com/occupational/{slug}/">
    <meta property="og:type" content="article">
    '''
    html = html.replace('{{seo_head_tags}}', seo_block)
    
    html = re.sub(r'<!-- HERO BLOCK -->.*?<!-- END HERO BLOCK -->', '', html, flags=re.DOTALL)
    
    html = html.replace('<!-- DYNAMIC_CONTENT -->', main_content)
    html = html.replace('<!-- LOCAL_SCHEMA -->', '') 
    
    with open(os.path.join(page_dir, 'index.html'), 'w') as f:
        f.write(html)
    count += 1

print(f"✅ Generated {count} Occupational pSEO pages in /public/occupational/")
