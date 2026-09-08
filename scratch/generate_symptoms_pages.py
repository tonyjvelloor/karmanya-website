"""
Generate /symptoms/ symptom-level pages:
1. knee-clicking-popping-sound
2. lower-back-pain-when-sitting
3. stiff-neck-computer-work
Linked to related conditions and single clinic location.
"""
import os, json, re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(f'{base_dir}/public/index.html') as f:
    idx = f.read()

nav_match = re.search(r'<header[^>]*>.*?</header>', idx, re.DOTALL)
nav_html = nav_match.group(0) if nav_match else ''
footer_match = re.search(r'<footer[^>]*>.*?</footer>', idx, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

symptoms = [
    {
        "slug": "knee-clicking-popping-sound",
        "title": "Why Does Your Knee Click, Pop, or Grind? Ayurvedic Diagnosis of Joint Crepitus",
        "meta_title": "Knee Clicking & Popping Sound Causes & Treatment | Karmanya Pune",
        "meta_desc": "Experiencing popping, cracking, or grinding in your knees? Learn why knee crepitus indicates early synovial depletion in Ayurveda and how Janu Basti restores joint cushion.",
        "symptom_name": "Knee Crepitus & Popping",
        "target_condition": "Knee Osteoarthritis",
        "condition_url": "/conditions/knee-joint-pain/",
        "read_time": "6 min read",
        "summary": "A clicking or grinding sound in your knee when squatting, climbing stairs, or standing up is known medically as crepitus. In Ayurveda, this sound is the hallmark earliest warning sign of dry Vata accumulation and synovial fluid depletion.",
        "sections": [
            {
                "heading": "What That Clicking Sound Actually Means in Ayurveda",
                "content": "In Ayurvedic pathology, healthy joints are lubricated by <em>Shleshaka Kapha</em> — an unctuous, protective bio-fluid comparable to synovial fluid. When aggravated <em>Vata dosha</em> (dry, rough, cold, mobile) enters the knee joint, it literally dries out this natural cushion.<br><br>The audible cracking and grinding (<em>Sandhi Sphutana</em>) is caused by bone surfaces rubbing with insufficient lubrication or gas bubbles popping within depleted synovial spaces. If left ignored, clicking progresses to stiffness, cartilage breakdown, and full-blown degenerative osteoarthritis (<em>Janu Sandhigata Vata</em>)."
            },
            {
                "heading": "How Karmanya Restores Knee Lubrication Before Cartilage Wears Down",
                "content": "The standard allopathic approach is often to tell patients: 'Come back when it hurts more or when you need surgery.' Ayurveda intervenes early.<br><br>At Karmanya in Pimple Saudagar, our physicians utilise <strong>Janu Basti</strong> — building a reservoir around the knee and infusing heated classical lipid formulations (<em>Mahanarayana Taila</em>, <em>Ksheerabala Taila</em>) deep into the joint capsule. This lubricates the subchondral layers, stops progressive friction, and halts the clicking sound."
            }
        ],
        "faqs": [
            {"q": "Is a clicking knee always a sign of arthritis?", "a": "Painless clicking occasionally occurs from benign tendon snapping. However, clicking accompanied by stiffness after sitting, aching after climbing stairs, or joint warmth is a definitive indicator of early degenerative change that warrants clinical pulse diagnosis."},
            {"q": "Can diet help restore knee joint lubrication?", "a": "Yes. A diet rich in pure A2 cow ghee, warm sesame preparations, soaked almonds, and boiled milk with ginger and turmeric nourishes joint Kapha. Cold refrigerated beverages and dry foods (salads, crackers) further aggravate Vata and must be discontinued."}
        ]
    },
    {
        "slug": "lower-back-pain-when-sitting",
        "title": "Lower Back Pain When Sitting at a Desk: Causes, Ergonomics, and Ayurvedic Relief",
        "meta_title": "Lower Back Pain When Sitting at Desk | Ayurvedic Spine Care Pune",
        "meta_desc": "Experiencing lower back ache after sitting for work in Pune? Discover how prolonged desk hours dehydrate spinal discs and how Kati Basti relieves lumbar strain.",
        "symptom_name": "Sitting Lower Back Strain",
        "target_condition": "Sciatica & Spinal Disc Disorders",
        "condition_url": "/conditions/spine-sciatica-back-pain/",
        "read_time": "6 min read",
        "summary": "For software engineers in Hinjawadi and corporate professionals across Pune, sitting for 8 to 10 hours a day causes continuous intradiscal pressure on the lumbar vertebrae, leading to chronic lower back ache and early disc prolapse.",
        "sections": [
            {
                "heading": "The Biomechanics of Sitting: Why Your L4-L5 Discs Suffer",
                "content": "Sitting unsupported actually exerts <strong>40% to 90% higher pressure</strong> on your lower lumbar discs (L4-L5 and L5-S1) than standing upright. In Ayurveda, the pelvic region and lumbar spine are the primary anatomical seat of <em>Apana Vata</em>.<br><br>Prolonged immobility disrupts downward Vata circulation, creating stagnant muscle spasm (<em>Stambha</em>) in the quadratus lumborum and psoas muscles. Over months, this constant pressure squeezes hydration out of the intervertebral discs, predisposing you to painful disc bulges and sciatica."
            },
            {
                "heading": "Targeted Ayurvedic Protocol for Desk-Bound Back Strain",
                "content": "Rather than relying on painkillers that irritate your stomach, our physicians at Karmanya prescribe <strong>Kati Basti</strong> — targeted warm oil retention over the lumbar spine. This relieves chronic paraspinal tension, increases deep arterial perfusion to the dehydrated disc, and calms irritated nerve roots.<br><br>Our team also reviews your workstation ergonomics and teaches micro-movement routines to protect your spine during work hours."
            }
        ],
        "faqs": [
            {"q": "How can I tell if my back ache is just muscular or a disc bulge?", "a": "Muscular strain is typically local and eases with gentle stretching. If pain radiates into the buttock or down the leg, causes numbness in toes, or worsens sharply when coughing or sneezing, it indicates nerve root compression from a disc bulge. Bring recent MRI scans to our clinic for assessment."},
            {"q": "How many sessions of Kati Basti do IT professionals typically need?", "a": "For chronic postural back strain without full disc herniation, a focused 7 to 10-day course of Kati Basti and Patra Pinda Sweda provides immense, long-lasting structural relief."}
        ]
    },
    {
        "slug": "stiff-neck-computer-work",
        "title": "Stiff Neck and Shoulder Pain from Laptop Work: Ayurvedic Solutions for Tech Neck",
        "meta_title": "Stiff Neck & Shoulder Pain from Screen Time Pune | Karmanya Ayurveda",
        "meta_desc": "Struggling with 'Tech Neck' and upper back tension in Pune? Discover how classical Griva Basti and Nasya therapy relieve cervical nerve compression and muscle rigidity.",
        "symptom_name": "Cervical Stiffness & Tech Neck",
        "target_condition": "Cervical Spondylosis",
        "condition_url": "/conditions/cervical-spondylosis-neck-pain/",
        "read_time": "6 min read",
        "summary": "Leaning forward toward laptop screens and smartphones puts immense stress on the cervical vertebrae. In Ayurveda, this chronic posture produces Manyastambha (cervical stiffness) and early disc degeneration.",
        "sections": [
            {
                "heading": "Understanding 'Tech Neck' as Manyastambha in Ayurveda",
                "content": "For every inch your head tilts forward, the effective load on your cervical spine doubles. In classical Ayurvedic texts, this severe rigidity and stiffness of the neck muscles is documented as <em>Manyastambha</em>, arising when aggravated Vata and Kapha block the cervical micro-channels (<em>Srotas</em>).<br><br>Symptoms start as morning stiffness and trap tightness, progressing to radiating arm numbness, finger tingling, and tension headaches."
            },
            {
                "heading": "Clinical Relief via Griva Basti and Nasya",
                "content": "Karmanya Ayurveda treats cervical strain through two synergistic classical therapies:<br><br>1. <strong>Griva Basti:</strong> Continuous retention of warm medicinal herbal oil over the cervical vertebrae (C4-C7) to relax deep spasm and nourish compressed discs.<br>2. <strong>Nasya Therapy:</strong> Administering medicated drops (such as <em>Ksheerabala Taila</em>) through the nasal corridor — which classical texts describe as the direct gateway to the head, brain, and cervical nerve roots."
            }
        ],
        "faqs": [
            {"q": "Can neck stiffness cause headaches and dizziness?", "a": "Yes. Cervicogenic headaches and vertigo occur when tight suboccipital muscles and compressed cervical joints disrupt blood flow and irritate upper cervical nerves. Griva Basti and Shirodhara are exceptionally effective for this."},
            {"q": "Is neck popping or cracking during stretching safe?", "a": "Habitual forceful cracking of the neck stretches ligaments and can worsen cervical instability. Instead, gentle isometric neck exercises and Ayurvedic herbal oil fomentation provide safe, lasting mobility."}
        ]
    }
]

for s in symptoms:
    slug = s['slug']
    out_dir = f"{base_dir}/public/symptoms/{slug}"
    os.makedirs(out_dir, exist_ok=True)
    
    sec_html = ""
    for sec in s['sections']:
        sec_html += f'<h2 style="font-size: 1.8rem; color: var(--color-primary); margin: var(--space-8) 0 var(--space-3);">{sec["heading"]}</h2>'
        sec_html += f'<div style="font-size: 1.05rem; line-height: 1.8; color: #333; margin-bottom: var(--space-6);">{sec["content"]}</div>'
        
    faqs_html = '<div style="margin-top: var(--space-10); border-top: 2px solid var(--color-accent); padding-top: var(--space-6);">'
    faqs_html += '<h2 style="font-size: 1.8rem; color: var(--color-primary); margin-bottom: var(--space-4);">Frequently Asked Questions</h2>'
    schema_faqs = []
    for f in s['faqs']:
        faqs_html += f'''<div style="border-bottom: 1px solid var(--color-border); padding: var(--space-4) 0;">
            <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-bottom: 6px;">{f["q"]}</h3>
            <p style="color: #555; line-height: 1.7; margin: 0;">{f["a"]}</p>
        </div>'''
        schema_faqs.append({"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}})
    faqs_html += '</div>'
    
    art_schema = {
        "@context": "https://schema.org",
        "@type": ["Article", "MedicalWebPage"],
        "headline": s['title'],
        "description": s['meta_desc'],
        "url": f"https://karmanyaayurveda.com/symptoms/{slug}/",
        "publisher": {
            "@type": "MedicalClinic",
            "name": "Karmanya Ayurveda Chikitsalaya",
            "url": "https://karmanyaayurveda.com/"
        },
        "about": {
            "@type": "MedicalSignOrSymptom",
            "name": s['symptom_name']
        }
    }
    
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": schema_faqs
    }
    
    bc_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Symptom Guides", "item": "https://karmanyaayurveda.com/symptoms/"},
            {"@type": "ListItem", "position": 3, "name": s['symptom_name'], "item": f"https://karmanyaayurveda.com/symptoms/{slug}/"}
        ]
    }
    
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="WkG1EsF3jpOenNE3qVR0DVexfFagjIofHbmUS-MM2I4">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{s['meta_title']}</title>
    <meta name="description" content="{s['meta_desc']}">
    <link rel="canonical" href="https://karmanyaayurveda.com/symptoms/{slug}/">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pimple Saudagar, Pune">
    <meta property="og:title" content="{s['meta_title']}">
    <meta property="og:description" content="{s['meta_desc']}">
    <meta property="og:url" content="https://karmanyaayurveda.com/symptoms/{slug}/">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://karmanyaayurveda.com/images/doctor-consult.webp">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preload" href="/images/logo.png" as="image" type="image/png">
    <link rel="preload" href="/css/tokens.css" as="style">
    <link rel="preload" href="/css/base.css" as="style">
    <link rel="stylesheet" href="/css/tokens.css?v=7">
    <link rel="stylesheet" href="/css/base.css?v=7">
    <link rel="stylesheet" href="/css/components.css?v=7">
    <script type="application/ld+json">
{json.dumps(art_schema, indent=2)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, indent=2)}
    </script>
    <script type="application/ld+json">
{json.dumps(bc_schema, indent=2)}
    </script>
</head>
<body>
        <!-- Top Announcement & Direct Contact Bar -->
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

    {nav_html}

    <div style="background: var(--color-primary); color: white; padding: var(--space-16) 0 var(--space-12);">
        <div class="container container-editorial">
            <nav style="font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-bottom: var(--space-4);">
                <a href="/" style="color: rgba(255,255,255,0.6); text-decoration: none;">Home</a> &rsaquo; 
                <a href="/symptoms/" style="color: rgba(255,255,255,0.6); text-decoration: none;">Symptom Guides</a> &rsaquo; 
                <span style="color: white;">{s['symptom_name']}</span>
            </nav>
            <span style="display: inline-block; background: rgba(212,175,55,0.2); border: 1px solid var(--color-accent); color: var(--color-accent); padding: 4px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: var(--space-3);">AYURVEDIC SYMPTOM GUIDE</span>
            <h1 style="font-size: clamp(1.9rem, 4vw, 3rem); font-weight: 400; line-height: 1.25; margin-bottom: var(--space-4); color: #ffffff;">{s['title']}</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); line-height: 1.6; max-width: 760px; margin-bottom: var(--space-4);">{s['summary']}</p>
            <div style="font-size: 0.85rem; color: rgba(255,255,255,0.7);">
                <span>&#128337; {s['read_time']}</span> &bull; 
                <span>Associated Condition: <a href="{s['condition_url']}" style="color: var(--color-accent); font-weight: 600;">{s['target_condition']}</a></span>
            </div>
        </div>
    </div>

    <main class="container container-editorial" style="padding-top: var(--space-10); padding-bottom: var(--space-16);">
        <div style="max-width: 820px;">
            
            <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-left: 4px solid var(--color-accent); border-radius: var(--radius-sm); padding: var(--space-6); margin-bottom: var(--space-8);">
                <strong style="color: var(--color-primary); font-size: 1.05rem; display: block; margin-bottom: 6px;">Single Clinic Location Notice</strong>
                <p style="margin: 0; color: #555; font-size: 0.95rem; line-height: 1.6;">All consultations and treatments are conducted exclusively at our single medical centre at <strong>27/11, Swaraj Garden Road, Pimple Saudagar, Pune</strong>. We do not operate secondary clinics or franchises. Convenient access with parking for patients from Wakad, Hinjawadi, Baner, Aundh, and PCMC.</p>
            </div>

            {sec_html}

            <!-- CTA Card -->
            <div style="background: var(--color-primary); color: white; border-radius: var(--radius-lg); padding: var(--space-8); margin: var(--space-10) 0; text-align: center;">
                <h3 style="color: white; font-size: 1.8rem; margin-bottom: var(--space-2);">Stop Early Symptoms from Becoming Chronic Disease</h3>
                <p style="color: rgba(255,255,255,0.85); max-width: 600px; margin: 0 auto var(--space-6); line-height: 1.6;">Consult Dr. Irshad T.M. or Dr. Tejasvi Mulik at our Pimple Saudagar clinic for an in-depth pulse assessment and personalised protocol.</p>
                <div style="display: flex; gap: var(--space-4); justify-content: center; flex-wrap: wrap;">
                    <a href="/book-consultation/" class="btn btn-primary" style="background: var(--color-accent); border-color: var(--color-accent); color: white; padding: 12px 26px;">Book Physician Consultation</a>
                    <a href="https://wa.me/919819820017?text=Hi%2C%20I%20am%20experiencing%20{s['symptom_name']}%20and%20would%20like%20to%20consult%20a%20physician." class="btn btn-secondary" style="border-color: rgba(255,255,255,0.4); color: white; padding: 12px 26px;">Ask on WhatsApp</a>
                </div>
            </div>

            {faqs_html}

        </div>
    </main>

    {footer_html}

    <!-- Floating WhatsApp CTA -->
    <div id="whatsapp-float" style="position: fixed; bottom: 28px; right: 28px; z-index: 9999;">
        <a href="https://wa.me/919819820017" target="_blank" rel="noopener"
           style="display: flex; align-items: center; justify-content: center; width: 60px; height: 60px; border-radius: 50%; background: #25D366; box-shadow: 0 4px 20px rgba(37,211,102,0.45);">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="white"><path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.832 6.51L4 29l7.695-1.807A12.94 12.94 0 0016 27c6.627 0 12-5.373 12-12S22.627 3 16 3zm0 2c5.523 0 10 4.477 10 10s-4.477 10-10 10a9.95 9.95 0 01-5.062-1.373l-.36-.219-4.567 1.073 1.107-4.441-.24-.378A9.96 9.96 0 016 15c0-5.523 4.477-10 10-10zm-3.5 5.5c-.28 0-.736.105-.973.368C11.29 11.13 10 12.5 10 14.5c0 2.003 1.547 3.94 1.76 4.212.214.271 2.98 4.788 7.322 6.523 1.022.4 1.818.637 2.438.815.625.183 1.194.157 1.643.096.5-.068 1.54-.63 1.757-1.237.216-.607.216-1.128.152-1.237-.064-.108-.236-.172-.495-.3-.26-.128-1.537-.758-1.775-.845-.237-.086-.41-.129-.583.13-.172.257-.667.845-.817 1.02-.15.172-.3.194-.558.065-.258-.13-1.09-.402-2.077-1.28-.768-.683-1.286-1.526-1.437-1.783-.15-.258-.016-.397.113-.525.116-.116.259-.3.388-.45.13-.15.173-.258.259-.43.086-.172.043-.322-.022-.45-.064-.13-.583-1.406-.8-1.926-.21-.506-.425-.437-.583-.445L13 9c-.28 0-.5 0-.5 0z"/></svg>
        </a>
    </div>
    <!-- Mobile Sticky Action Bar -->
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

</body>
</html>"""
    
    with open(f"{out_dir}/index.html", "w") as f:
        f.write(page_html)
    print(f"  ✅ /symptoms/{slug}/")

# Generate /symptoms/ hub
hub_cards = ""
for s in symptoms:
    hub_cards += f"""
    <div style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-8); box-shadow: var(--shadow-sm); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
            <span style="font-size: 0.75rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: var(--space-2);">{s['target_condition']}</span>
            <h2 style="font-size: 1.4rem; margin-bottom: var(--space-3);"><a href="/symptoms/{s['slug']}/" style="color: var(--color-primary); text-decoration: none; line-height: 1.3;">{s['title']}</a></h2>
            <p style="color: #555; font-size: 0.95rem; line-height: 1.6; margin-bottom: var(--space-4);">{s['meta_desc']}</p>
        </div>
        <div>
            <a href="/symptoms/{s['slug']}/" class="btn btn-secondary" style="font-size: 0.9rem; padding: 8px 18px;">Read Symptom Guide &rarr;</a>
        </div>
    </div>"""

hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="WkG1EsF3jpOenNE3qVR0DVexfFagjIofHbmUS-MM2I4">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayurvedic Symptom Guides | Early Diagnosis & Care | Karmanya Pune</title>
    <meta name="description" content="Understand early warning symptoms from clicking knees to desk backache and stiff neck through classical Ayurveda. Clinical guidance from Karmanya, Pimple Saudagar.">
    <link rel="canonical" href="https://karmanyaayurveda.com/symptoms/">
    <link rel="stylesheet" href="/css/tokens.css?v=7">
    <link rel="stylesheet" href="/css/base.css?v=7">
    <link rel="stylesheet" href="/css/components.css?v=7">
</head>
<body>
        <!-- Top Announcement & Direct Contact Bar -->
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

    {nav_html}
    <div style="background: var(--color-primary); padding: var(--space-16) 0 var(--space-12); text-align: center; color: white;">
        <div class="container container-editorial">
            <span style="color: var(--color-accent); font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">PREVENTATIVE CLINICAL DIAGNOSIS</span>
            <h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0; color: #ffffff;">Ayurvedic Symptom Guides</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 680px; margin: 0 auto;">Don't wait for mild symptoms to evolve into advanced degeneration. Understand what your body is signalling through classical Ayurvedic pathology.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container">
            <div class="grid-2" style="gap: var(--space-8);">
                {hub_cards}
            </div>
        </div>
    </section>
    {footer_html}
    <!-- Mobile Sticky Action Bar -->
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

</body>
</html>"""

os.makedirs(f"{base_dir}/public/symptoms", exist_ok=True)
with open(f"{base_dir}/public/symptoms/index.html", "w") as f:
    f.write(hub_html)
print("  ✅ /symptoms/ Hub")
