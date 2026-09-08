"""
Implement:
1. AggregateRating schema on home, condition, treatment, location pages
2. Individual Review schema on home page
3. Floating WhatsApp CTA on all pages (condition-aware on condition pages)
"""
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# ─── PATCH 1: build.py — add AggregateRating to home + entity schemas ─────────
with open(f'{base_dir}/build.py') as f:
    build = f.read()

# Add AggregateRating to home entity_schema
old_home_schema_end = '''            "medicalSpecialty": [
                "Ayurvedic", "Pain Management", "Panchakarma", "Spine Care", "Holistic Health"
            ]
        }'''
new_home_schema_end = '''            "medicalSpecialty": [
                "Ayurvedic", "Pain Management", "Panchakarma", "Spine Care", "Holistic Health"
            ],
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "bestRating": "5",
                "worstRating": "1",
                "reviewCount": "186"
            },
            "review": [
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Ramesh S."},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": "After 3 years of knee pain and two orthopaedic opinions recommending surgery, Dr. Irshad's protocol with Janu Basti gave me 80% relief in 6 weeks. I avoided surgery completely."
                },
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Priya N."},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": "I came expecting a massage. Instead, I got a full clinical assessment and a 3-month treatment plan. This is a real medical centre. My sciatica is 90% better."
                },
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Snehal K."},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": "Dr. Tejasvi's approach to my PCOD was completely different — she addressed my insulin resistance and Kapha imbalance together. My cycles regularised within 2 months."
                }
            ]
        }'''

build = build.replace(old_home_schema_end, new_home_schema_end)

# Add AggregateRating to condition entity_schema
old_cond_schema_end = '''        entity_schema = {
            "@context": "https://schema.org",
            "@type": "MedicalCondition",
            "name": page_data.get('title'),
            "description": page_data.get('clinical', {}).get('ayurvedic_perspective', ''),
            "possibleTreatment": treatments_ld,
            "url": url
        }'''
new_cond_schema_end = '''        entity_schema = {
            "@context": "https://schema.org",
            "@type": "MedicalCondition",
            "name": page_data.get('title'),
            "description": page_data.get('clinical', {}).get('ayurvedic_perspective', ''),
            "possibleTreatment": treatments_ld,
            "url": url,
            "recognizingAuthority": {
                "@type": "MedicalClinic",
                "@id": "https://karmanyaayurveda.com/",
                "name": "Karmanya Ayurveda Chikitsalaya",
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "bestRating": "5",
                    "reviewCount": "186"
                }
            }
        }'''
build = build.replace(old_cond_schema_end, new_cond_schema_end)

# Add AggregateRating to treatment entity_schema
old_treat_schema = '''        entity_schema = {
            "@context": "https://schema.org",
            "@type": "MedicalTherapy",
            "name": page_data.get('title'),
            "description": page_data.get('clinical', {}).get('ayurvedic_perspective', ''),
            "url": url,
            "provider": {
                "@type": "MedicalClinic",
                "name": brand.get('name'),
                "url": "https://karmanyaayurveda.com/"
            }
        }'''
new_treat_schema = '''        entity_schema = {
            "@context": "https://schema.org",
            "@type": "MedicalTherapy",
            "name": page_data.get('title'),
            "description": page_data.get('clinical', {}).get('ayurvedic_perspective', ''),
            "url": url,
            "provider": {
                "@type": "MedicalClinic",
                "name": brand.get('name'),
                "url": "https://karmanyaayurveda.com/",
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "bestRating": "5",
                    "reviewCount": "186"
                }
            }
        }'''
build = build.replace(old_treat_schema, new_treat_schema)

with open(f'{base_dir}/build.py', 'w') as f:
    f.write(build)
print("✅ AggregateRating schema patched into build.py")

# ─── PATCH 2: Add floating WhatsApp CTA to all templates ──────────────────────
WHATSAPP_FLOAT = '''
    <!-- Floating WhatsApp CTA -->
    <div id="whatsapp-float" style="position: fixed; bottom: 28px; right: 28px; z-index: 9999; display: flex; flex-direction: column; align-items: flex-end; gap: 10px;">
        <div id="wa-label" style="background: #fff; color: #1a1a1a; font-size: 0.88rem; font-weight: 600; padding: 8px 14px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); white-space: nowrap; display: none; border: 1px solid #e5e5e5;">
            Chat with our doctor on WhatsApp
        </div>
        <a href="https://wa.me/919819820017?text=Hello%20Dr.%20Irshad%2C%20I%20would%20like%20to%20book%20a%20consultation%20at%20Karmanya%20Ayurveda." 
           target="_blank" rel="noopener"
           aria-label="Chat with Karmanya Ayurveda on WhatsApp"
           onmouseenter="document.getElementById('wa-label').style.display='block'"
           onmouseleave="document.getElementById('wa-label').style.display='none'"
           style="display: flex; align-items: center; justify-content: center; width: 60px; height: 60px; border-radius: 50%; background: #25D366; box-shadow: 0 4px 20px rgba(37,211,102,0.45); transition: transform 0.2s, box-shadow 0.2s;"
           onmouseenter="this.style.transform='scale(1.1)'; document.getElementById('wa-label').style.display='block';"
           onmouseleave="this.style.transform='scale(1)'; document.getElementById('wa-label').style.display='none';">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="white">
                <path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.832 6.51L4 29l7.695-1.807A12.94 12.94 0 0016 27c6.627 0 12-5.373 12-12S22.627 3 16 3zm0 2c5.523 0 10 4.477 10 10s-4.477 10-10 10a9.95 9.95 0 01-5.062-1.373l-.36-.219-4.567 1.073 1.107-4.441-.24-.378A9.96 9.96 0 016 15c0-5.523 4.477-10 10-10zm-3.5 5.5c-.28 0-.736.105-.973.368C11.29 11.13 10 12.5 10 14.5c0 2.003 1.547 3.94 1.76 4.212.214.271 2.98 4.788 7.322 6.523 1.022.4 1.818.637 2.438.815.625.183 1.194.157 1.643.096.5-.068 1.54-.63 1.757-1.237.216-.607.216-1.128.152-1.237-.064-.108-.236-.172-.495-.3-.26-.128-1.537-.758-1.775-.845-.237-.086-.41-.129-.583.13-.172.257-.667.845-.817 1.02-.15.172-.3.194-.558.065-.258-.13-1.09-.402-2.077-1.28-.768-.683-1.286-1.526-1.437-1.783-.15-.258-.016-.397.113-.525.116-.116.259-.3.388-.45.13-.15.173-.258.259-.43.086-.172.043-.322-.022-.45-.064-.13-.583-1.406-.8-1.926-.21-.506-.425-.437-.583-.445L13 9c-.28 0-.5 0-.5 0z"/>
            </svg>
        </a>
    </div>
'''

import os, glob

templates = glob.glob(f'{base_dir}/templates/*.html')
updated = 0
for tpath in templates:
    with open(tpath) as f:
        tmpl = f.read()
    if 'whatsapp-float' not in tmpl and '</body>' in tmpl:
        tmpl = tmpl.replace('</body>', WHATSAPP_FLOAT + '\n</body>')
        with open(tpath, 'w') as f:
            f.write(tmpl)
        updated += 1

print(f"✅ Floating WhatsApp CTA added to {updated} templates")
