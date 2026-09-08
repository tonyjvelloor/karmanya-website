"""
Generate /glossary/ page with:
- 24 core clinical Ayurvedic terms
- DefinedTermSet / DefinedTerm schema
- Internal links to conditions, treatments, and single clinic consultation
"""
import os, json, re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(f'{base_dir}/public/index.html') as f:
    idx = f.read()

nav_match = re.search(r'<header[^>]*>.*?</header>', idx, re.DOTALL)
nav_html = nav_match.group(0) if nav_match else ''
footer_match = re.search(r'<footer[^>]*>.*?</footer>', idx, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

terms = [
    {
        "term": "Nadi Pariksha",
        "transliteration": "Nāḍī Parīkṣā",
        "category": "Diagnostics",
        "definition": "Classical Ayurvedic pulse diagnosis technique performed at the radial artery using three fingers to assess the qualitative balance of Vata, Pitta, and Kapha doshas, evaluate metabolic fire (Agni), tissue health (Dhatus), and detect subclinical disease before symptoms manifest.",
        "related_link": "/doctors/",
        "link_text": "Experienced by our physicians"
    },
    {
        "term": "Janu Basti",
        "transliteration": "Jānu Basti",
        "category": "Therapies",
        "definition": "A specialised non-invasive Panchakarma upakarma where a reservoir of black gram flour dough is placed around the knee joint and filled with warm medicated oils (such as Mahanarayana Taila) to regenerate synovial lubrication, soothe cartilage wear, and treat osteoarthritis.",
        "related_link": "/treatments/janu-basti/",
        "link_text": "View Janu Basti Protocol"
    },
    {
        "term": "Kati Basti",
        "transliteration": "Kaṭī Basti",
        "category": "Therapies",
        "definition": "An intensive spinal therapy where a dough dam is constructed over the lumbosacral region (L4-L5/S1) and filled with warm medicated herbal oil for 45 minutes to relieve nerve root compression, disc herniation, and sciatica.",
        "related_link": "/treatments/kati-basti/",
        "link_text": "View Kati Basti Protocol"
    },
    {
        "term": "Griva Basti",
        "transliteration": "Grīvā Basti",
        "category": "Therapies",
        "definition": "Localised pooling of warm therapeutic herbal oil over the cervical vertebrae of the neck to nourish intervertebral discs, relieve muscle spasm, and resolve cervical spondylosis and cervicogenic headaches.",
        "related_link": "/conditions/cervical-spondylosis-neck-pain/",
        "link_text": "Cervical Spondylosis Care"
    },
    {
        "term": "Shirodhara",
        "transliteration": "Śirodhārā",
        "category": "Therapies",
        "definition": "The continuous, rhythmic pouring of a stream of warm herbal oil or medicated buttermilk (Takradhara) across the forehead over the Ajna Marma. Proven to activate parasympathetic nervous system response, lower cortisol, and relieve insomnia and anxiety.",
        "related_link": "/treatments/shirodhara/",
        "link_text": "View Shirodhara Protocol"
    },
    {
        "term": "Panchakarma",
        "transliteration": "Pañcakarma",
        "category": "Therapies",
        "definition": "The premier five-fold classical biological detoxification protocol in Ayurveda: Vamana (emesis), Virechana (purgation), Basti (medicated enema), Nasya (nasal therapy), and Raktamokshana (bloodletting), designed to purge deep cellular metabolic waste (Ama).",
        "related_link": "/treatments/panchakarma/",
        "link_text": "View Panchakarma Details"
    },
    {
        "term": "Virechana",
        "transliteration": "Virecana",
        "category": "Panchakarma",
        "definition": "Medically controlled therapeutic purgation using classical herbal decoctions and castor preparations to cleanse Pitta dosha and toxins from the liver, gallbladder, and small intestine. Highly effective for psoriasis, eczema, and PCOD.",
        "related_link": "/conditions/skin-disorders-psoriasis/",
        "link_text": "Psoriasis & Skin Care"
    },
    {
        "term": "Basti",
        "transliteration": "Basti",
        "category": "Panchakarma",
        "definition": "Administration of herbal decoctions (Kashaya Basti) or medicated oils (Sneha Basti) into the rectum. Recognized in classical texts as the 'half of all medical treatment' because it directly controls Vata dosha at its prime anatomical seat.",
        "related_link": "/conditions/spine-sciatica-back-pain/",
        "link_text": "Sciatica Spine Protocols"
    },
    {
        "term": "Nasya",
        "transliteration": "Nasya",
        "category": "Panchakarma",
        "definition": "Administration of therapeutic herbal oils or powders through the nasal passages. Described in classical Ayurveda as the direct channel to the brain and head, effective for cervical spondylosis, migraine, sinusitis, and sleep disorders.",
        "related_link": "/treatments/panchakarma/",
        "link_text": "Panchakarma Modalities"
    },
    {
        "term": "Patra Pinda Sweda (Kizhi)",
        "transliteration": "Patra Piṇḍa Sveda",
        "category": "Therapies",
        "definition": "A therapeutic fomentation procedure using boluses filled with medicinal herbal leaves fried in medicated oils, applied rhythmically over stiff joints and muscles to reduce swelling, spasm, and arthritic pain.",
        "related_link": "/treatments/kizhi/",
        "link_text": "View Kizhi Therapy"
    },
    {
        "term": "Njavara Kizhi",
        "transliteration": "Ñavarakkizhi",
        "category": "Therapies",
        "definition": "A unique Kerala Ashtavaidya rejuvenation therapy where special organic medicinal rice (Shashtika Shali) cooked in herbal milk decoction is tied in cloth boluses and applied across the body to restore wasted muscle and nourish nerve roots.",
        "related_link": "/treatments/kerala-chikitsa/",
        "link_text": "Kerala Chikitsa Tradition"
    },
    {
        "term": "Abhyangam",
        "transliteration": "Abhyaṅgam",
        "category": "Therapies",
        "definition": "Synchronised full-body medicinal oil application performed by trained therapists following specific lymphatic and nerve pathways, followed by herbal steam (Swedana) to loosen deep tissue toxins.",
        "related_link": "/treatments/abhyangam/",
        "link_text": "View Abhyangam Details"
    },
    {
        "term": "Ama",
        "transliteration": "Āma",
        "category": "Pathology",
        "definition": "Toxic, sticky, undigested metabolic byproduct that forms in the gastrointestinal tract due to weakened digestive fire (Mandaagni), circulating through micro-channels (Srotas) and triggering systemic inflammation and auto-immune reactions.",
        "related_link": "/conditions/digestive-metabolic-disorders/",
        "link_text": "Digestive Disorder Care"
    },
    {
        "term": "Agni",
        "transliteration": "Agni",
        "category": "Physiology",
        "definition": "The biological and digestive fire responsible for enzymatic digestion, cellular metabolism, nutrient absorption, and immune resistance. Healthy Agni prevents disease formation.",
        "related_link": "/conditions/digestive-metabolic-disorders/",
        "link_text": "Metabolic Protocols"
    },
    {
        "term": "Ojas",
        "transliteration": "Ojas",
        "category": "Physiology",
        "definition": "The supreme subtle essence of all seven bodily tissues (Dhatus), representing vital resilience, innate immunity, mental stability, and longevity in classical Ayurvedic medicine.",
        "related_link": "/conditions/stress-insomnia-anxiety/",
        "link_text": "Restoring Vital Resilience"
    },
    {
        "term": "Prakriti",
        "transliteration": "Prakṛti",
        "category": "Physiology",
        "definition": "An individual's unique genetic and constitutional bio-type determined at conception by the proportion of Vata, Pitta, and Kapha doshas, dictating metabolic traits and disease predispositions.",
        "related_link": "/doctors/",
        "link_text": "Consult on Your Prakriti"
    },
    {
        "term": "Vikriti",
        "transliteration": "Vikṛti",
        "category": "Pathology",
        "definition": "The current state of dosha imbalance or pathological deviation away from an individual's natural constitutional baseline (Prakriti), evaluated during clinical consultation to plan therapy.",
        "related_link": "/conditions/",
        "link_text": "Conditions We Treat"
    },
    {
        "term": "Vata Dosha",
        "transliteration": "Vāta Doṣa",
        "category": "Doshas",
        "definition": "The biological kinetic principle composed of Space and Air elements. Governs all neuro-muscular movement, breathing, nerve transmission, and joint articulation. When aggravated, causes dryness, joint pain, sciatica, and degeneration.",
        "related_link": "/conditions/knee-joint-pain/",
        "link_text": "Vata Joint Conditions"
    },
    {
        "term": "Pitta Dosha",
        "transliteration": "Pitta Doṣa",
        "category": "Doshas",
        "definition": "The biological thermal principle composed of Fire and Water elements. Governs enzymatic digestion, cellular thermogenesis, hepatic metabolism, and hormone synthesis. Imbalance causes inflammatory skin diseases, acidity, and burning sensations.",
        "related_link": "/conditions/skin-disorders-psoriasis/",
        "link_text": "Pitta Skin Conditions"
    },
    {
        "term": "Kapha Dosha",
        "transliteration": "Kapha Doṣa",
        "category": "Doshas",
        "definition": "The biological anabolic principle composed of Earth and Water elements. Governs physical structure, joint lubrication (Shleshaka Kapha), tissue cohesion, and weight stability. Excess causes fluid retention, cysts, and metabolic sluggishness.",
        "related_link": "/conditions/womens-health-pcod-hormonal/",
        "link_text": "Kapha & Hormonal Health"
    },
    {
        "term": "Rasayana",
        "transliteration": "Rasāyana",
        "category": "Therapies",
        "definition": "Rejuvenation and longevity therapeutics in classical Ayurveda that enhance cellular nutrition, prevent premature tissue degeneration, promote tissue regeneration, and boost immunity.",
        "related_link": "/treatments/",
        "link_text": "View All Therapies"
    },
    {
        "term": "Srotas",
        "transliteration": "Srotas",
        "category": "Physiology",
        "definition": "The macroscopic and microscopic bodily channel networks through which biological fluids, nutrients, and waste products flow. Clearing blocked channels (Sroto-shodhana) is a core aim of Panchakarma.",
        "related_link": "/treatments/panchakarma/",
        "link_text": "Channel Cleansing Therapy"
    },
    {
        "term": "Uttara Basti",
        "transliteration": "Uttara Basti",
        "category": "Panchakarma",
        "definition": "A gentle specialised Panchakarma procedure performed by female physicians where medicated oils are administered into the intrauterine tract to treat PCOD, thin endometrium, tubal blockage, and recurrent reproductive disorders.",
        "related_link": "/conditions/womens-health-pcod-hormonal/",
        "link_text": "Female Healthcare Protocols"
    },
    {
        "term": "Ashtavaidya",
        "transliteration": "Aṣṭavaidya",
        "category": "Tradition",
        "definition": "The revered Kerala Ayurvedic physician lineage that mastered all eight classical branches (Ashtanga) of Ayurveda, renowned worldwide for developing specialized oil procedures and curative chikitsa traditions.",
        "related_link": "/doctors/dr-irshad/",
        "link_text": "Dr. Irshad's Background"
    }
]

# Generate items HTML
terms_html = ""
defined_terms_schema = []

for t in sorted(terms, key=lambda x: x['term']):
    terms_html += f"""
    <div id="{t['term'].lower().replace(' ', '-')}" style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-6); box-shadow: var(--shadow-sm); margin-bottom: var(--space-6);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: var(--space-2);">
            <h3 style="font-size: 1.4rem; color: var(--color-primary); margin: 0;">{t['term']}</h3>
            <span style="font-size: 0.75rem; background: rgba(200,121,65,0.12); color: var(--color-accent); font-weight: 700; padding: 4px 10px; border-radius: 12px; text-transform: uppercase;">{t['category']}</span>
        </div>
        <div style="font-size: 0.9rem; color: #777; font-style: italic; margin-bottom: var(--space-3);">{t['transliteration']}</div>
        <p style="color: #444; font-size: 1rem; line-height: 1.7; margin-bottom: var(--space-4);">{t['definition']}</p>
        <div style="font-size: 0.88rem;">
            <a href="{t['related_link']}" style="color: var(--color-accent); font-weight: 600; text-decoration: none;">&rarr; {t['link_text']}</a>
        </div>
    </div>"""
    
    defined_terms_schema.append({
        "@type": "DefinedTerm",
        "name": t['term'],
        "description": t['definition'],
        "inDefinedTermSet": "https://karmanyaayurveda.com/glossary/"
    })

glossary_schema = {
    "@context": "https://schema.org",
    "@type": "DefinedTermSet",
    "name": "Karmanya Clinical Ayurveda Glossary",
    "description": "Authoritative glossary of classical Ayurvedic medicine terms, diagnostic concepts, and therapeutic protocols.",
    "url": "https://karmanyaayurveda.com/glossary/",
    "hasDefinedTerm": defined_terms_schema
}

bc_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
        {"@type": "ListItem", "position": 2, "name": "Ayurvedic Glossary", "item": "https://karmanyaayurveda.com/glossary/"}
    ]
}

page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="WkG1EsF3jpOenNE3qVR0DVexfFagjIofHbmUS-MM2I4">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayurvedic Medical Glossary | Key Concepts & Therapies | Karmanya Pune</title>
    <meta name="description" content="Understand classical Ayurvedic medical terms from Panchakarma and Nadi Pariksha to Janu Basti and Doshas. Clinical definitions from Karmanya Ayurveda Pune.">
    <link rel="canonical" href="https://karmanyaayurveda.com/glossary/">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pimple Saudagar, Pune">
    <meta property="og:title" content="Ayurvedic Medical Glossary | Karmanya Ayurveda Pune">
    <meta property="og:description" content="Authoritative clinical dictionary of classical Ayurvedic concepts and therapies.">
    <meta property="og:url" content="https://karmanyaayurveda.com/glossary/">
    <link rel="preload" href="/images/logo.png" as="image" type="image/png">
    <link rel="preload" href="/css/tokens.css" as="style">
    <link rel="preload" href="/css/base.css" as="style">
    <link rel="stylesheet" href="/css/tokens.css?v=7">
    <link rel="stylesheet" href="/css/base.css?v=7">
    <link rel="stylesheet" href="/css/components.css?v=7">
    <script type="application/ld+json">
{json.dumps(glossary_schema, indent=2)}
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

    <div style="background: var(--color-primary); color: white; padding: var(--space-16) 0 var(--space-12); text-align: center;">
        <div class="container container-editorial">
            <span style="color: var(--color-accent); font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">CLINICAL MEDICAL REFERENCE</span>
            <h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0; color: #ffffff;">Ayurvedic Medical Glossary</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 680px; margin: 0 auto;">Clear, medically accurate definitions of classical Ayurvedic terminology, diagnostic sciences, and treatment modalities practiced at Karmanya.</p>
        </div>
    </div>

    <main class="container container-editorial" style="padding-top: var(--space-12); padding-bottom: var(--space-16);">
        <div style="max-width: 820px; margin: 0 auto;">
            
            <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-sm); padding: var(--space-6); margin-bottom: var(--space-8);">
                <p style="margin: 0; color: #555; font-size: 0.95rem; line-height: 1.6;">
                    Ayurveda is not merely herbal remedies; it is a complete, codified medical system with its own anatomical, physiological, and pharmacological terminology. This glossary serves to demystify these terms for our patients. All treatments are conducted exclusively at our medical centre: <strong>27/11, Swaraj Garden Road, Pimple Saudagar, Pune</strong>.
                </p>
            </div>

            {terms_html}

            <div style="background: var(--color-primary); color: white; border-radius: var(--radius-lg); padding: var(--space-8); margin-top: var(--space-12); text-align: center;">
                <h3 style="color: white; font-size: 1.8rem; margin-bottom: var(--space-2);">Have Questions About Your Health?</h3>
                <p style="color: rgba(255,255,255,0.85); max-width: 600px; margin: 0 auto var(--space-6); line-height: 1.6;">Schedule a personal consultation with our senior Ayurvedic physicians for a comprehensive pulse diagnosis and custom protocol.</p>
                <a href="/book-consultation/" class="btn btn-primary" style="background: var(--color-accent); border-color: var(--color-accent); color: white; padding: 12px 26px;">Book Physician Consultation</a>
            </div>

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

os.makedirs(f"{base_dir}/public/glossary", exist_ok=True)
with open(f"{base_dir}/public/glossary/index.html", "w") as f:
    f.write(page_html)
print("  ✅ /glossary/ Generated with 24 clinical terms")
