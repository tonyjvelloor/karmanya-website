"""
Generate /compare/ comparison pages:
1. ayurveda-vs-knee-replacement-surgery
2. ayurveda-vs-surgery-painkillers-sciatica
3. ayurveda-vs-hormonal-pills-pcod
With full structured data (Article, MedicalWebPage, FAQPage, BreadcrumbList), 
comparison tables, clinical criteria, and transparent boundaries.
"""
import os, json, re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(f'{base_dir}/public/index.html') as f:
    idx = f.read()

nav_match = re.search(r'<header[^>]*>.*?</header>', idx, re.DOTALL)
nav_html = nav_match.group(0) if nav_match else ''
footer_match = re.search(r'<footer[^>]*>.*?</footer>', idx, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

comparisons = [
    {
        "slug": "ayurveda-vs-knee-replacement-surgery",
        "title": "Ayurvedic Treatment vs Knee Replacement Surgery: A Clinical Decision Guide",
        "meta_title": "Ayurveda vs Knee Replacement Surgery in Pune | Karmanya Ayurveda",
        "meta_desc": "Debating between knee replacement surgery (TKR) and Ayurvedic treatment (Janu Basti)? Clinical comparison of recovery times, risks, costs, and eligibility in Pune.",
        "condition_name": "Knee Osteoarthritis",
        "condition_url": "/conditions/knee-joint-pain/",
        "read_time": "7 min read",
        "summary": "When knee cartilage wears down, surgery is frequently recommended as the definitive answer. But is knee replacement necessary for every grade of osteoarthritis? This guide compares classical Kerala Ayurvedic management with Total Knee Arthroplasty (TKA/TKR), outlining when surgery is mandatory and when non-surgical Ayurvedic protocols can preserve your natural joint.",
        "table": [
            ("Parameter", "Ayurvedic Protocol (Janu Basti + Chikitsa)", "Total Knee Replacement (TKR)"),
            ("Goal", "Preserve natural joint, regenerate synovial lubrication, stop degeneration", "Amputate damaged joint surfaces and implant metal/plastic prosthesis"),
            ("Invasiveness", "100% Non-invasive (External medicated oils + internal herbs)", "Major surgical procedure under spinal/general anaesthesia"),
            ("Recovery Period", "No hospitalisation; walk immediately after daily 45-min therapy", "3–7 days hospital stay; 3–6 months intensive physical rehab"),
            ("Clinical Suitability", "Grade I, Grade II, and moderate Grade III osteoarthritis", "End-stage Grade IV (bone-on-bone complete joint collapse)"),
            ("Complication Risks", "Virtually zero surgical risk; completely natural herbal oils", "Infection, blood clots (DVT), implant loosening, revision surgery in 15–20 yrs"),
            ("Cost in Pune", "₹14,000 – ₹25,000 for complete multi-week protocol & medicines", "₹2,50,000 – ₹4,50,000 per knee (plus post-op physio & meds)")
        ],
        "sections": [
            {
                "heading": "The Core Medical Difference: Joint Preservation vs Joint Replacement",
                "content": "Modern orthopaedics views cartilage wear as purely mechanical friction. Once space narrows, the standard recommendation moves quickly toward joint replacement. In classical Ayurveda, knee osteoarthritis is diagnosed as <em>Janu Sandhigata Vata</em>. The root cause is systemic Vata aggravation causing depletion of <em>Shleshaka Kapha</em> (synovial fluid) and tissue drying.<br><br>At Karmanya Ayurveda, our priority is <strong>natural joint preservation</strong>. Through sustained warm medicated oil pooling (<em>Janu Basti</em>), herbal leaf fomentation (<em>Patra Pinda Sweda</em>), and cartilage-nourishing Rasayanas, we restore lubrication and soothe peri-articular inflammation before permanent structural collapse occurs."
            },
            {
                "heading": "When Should You NOT Choose Ayurveda? (Honest Clinical Boundaries)",
                "content": "We never make false promises. If an MRI or weight-bearing X-ray demonstrates <strong>Grade IV complete joint ankylosis (complete loss of joint space with severe bone erosion and mechanical deformity)</strong>, non-surgical therapy cannot reconstruct destroyed bone architecture. In such end-stage cases, surgical replacement is appropriate.<br><br>However, over 70% of patients seeking second opinions at our Pimple Saudagar clinic are in Grade II or Grade III. For these patients, surgery can often be safely deferred or avoided entirely through timely, disciplined Ayurvedic intervention."
            }
        ],
        "faqs": [
            {
                "q": "Can Ayurveda help if my orthopaedic surgeon already gave a surgery date?",
                "a": "Unless you are in acute emergency trauma or have active septic arthritis, elective knee replacement is scheduled for chronic degeneration. Many patients consult our physicians for an independent clinical assessment and trial a 3-week Janu Basti protocol before making a permanent surgical decision."
            },
            {
                "q": "What happens if Ayurvedic treatment does not relieve my pain?",
                "a": "Ayurvedic treatment does not compromise your ability to have surgery later if ever required. Unlike steroid injections which can weaken tendons and increase infection risk for future implants, Ayurvedic herbal therapies protect surrounding soft tissue and muscle tone."
            }
        ]
    },
    {
        "slug": "ayurveda-vs-surgery-painkillers-sciatica",
        "title": "Ayurveda vs Painkillers & Surgery for Sciatica and Disc Prolapse",
        "meta_title": "Ayurveda vs Surgery & Painkillers for Sciatica in Pune | Karmanya",
        "meta_desc": "Comparing Ayurvedic Kati Basti and Panchakarma against microdiscectomy and long-term NSAIDs for lumbar slip disc and sciatica in Pimple Saudagar, Pune.",
        "condition_name": "Sciatica & Spinal Disc Herniation",
        "condition_url": "/conditions/spine-sciatica-back-pain/",
        "read_time": "8 min read",
        "summary": "Sciatica caused by L4-L5 or L5-S1 disc herniation leaves patients trapped between daily painkiller dependence and daunting spinal surgery. This clinical guide compares standard modern medical pathways against authentic Ayurvedic spine care at Karmanya Ayurveda.",
        "table": [
            ("Parameter", "Ayurvedic Spine Protocol (Kati Basti + Basti)", "Allopathic Medications (NSAIDs / Gabapentin)", "Spine Surgery (Microdiscectomy / Fusion)"),
            ("Mechanism", "Relieves nerve root oedema, rehydrates disc, corrects Apana Vata", "Chemical suppression of nerve pain and prostaglandin production", "Physical excision of protruding disc fragment to decompress nerve"),
            ("Root Cause Addressed?", "Yes — halts disc dehydration and strengthens paraspinal muscles", "No — masks symptoms while underlying disc bulge persists", "Partially — relieves pressure mechanically, but adjacent segment disease risk remains"),
            ("Side Effect Profile", "Zero organ toxicity; rejuvenates digestive and metabolic health", "Gastric ulcers, kidney stress, liver burden with chronic NSAID use", "Failed Back Surgery Syndrome (FBSS), spinal instability, nerve scar tissue"),
            ("Timeline", "Noticeable relief in 7–14 days; stable recovery in 21–28 days", "Temporary relief within 2–4 hours; pain returns when dose wears off", "Immediate mechanical decompression; 6–12 weeks surgical wound healing")
        ],
        "sections": [
            {
                "heading": "Why Masking Nerve Pain With Painkillers Accelerates Disc Damage",
                "content": "Pain is your body's protective biofeedback mechanism. When heavy NSAIDs, muscle relaxants, or pregabalin mute pain signals, patients continue lifting, sitting in poor postures, and stressing the damaged disc. Over months, this turns a minor disc bulge into an extruded disc or permanent nerve root impingement.<br><br>At Karmanya Ayurveda, our goal is not temporary sedation of symptoms. By pooling warm classical herbal oils (<em>Ksheerabala Taila</em>, <em>Murivenna</em>) directly over the affected lumbar vertebrae in <em>Kati Basti</em>, we induce deep vascular perfusion, reduce perineural swelling, and relieve the severe muscular spasms immobilising the lower spine."
            },
            {
                "heading": "Red Flags: When Is Spinal Surgery Immediately Necessary?",
                "content": "Patient safety is paramount. If a patient experiences <strong>Cauda Equina Syndrome</strong> (sudden loss of bladder or bowel control, saddle anaesthesia, or sudden progressive foot drop/paralysis), this constitutes a medical emergency requiring immediate surgical decompression within 24–48 hours. Our physicians screen every back pain patient during physical assessment to rule out these emergency criteria."
            }
        ],
        "faqs": [
            {
                "q": "Can an extruded or herniated disc shrink back with Ayurvedic therapy?",
                "a": "Yes. Clinical follow-up MRIs consistently show that resolving perineural inflammation and rehydrating disc tissue allows the body's natural macrophage system to resorb herniated disc fragments (spontaneous disc regression) without surgical cutting."
            },
            {
                "q": "How many days of Kati Basti are recommended for L4-L5 sciatica?",
                "a": "Most patients at Karmanya undergo a 14 to 21-day consecutive protocol of Kati Basti combined with Njavara Kizhi and internal herbal decoctions, followed by structured ergonomics and rehabilitation guidance."
            }
        ]
    },
    {
        "slug": "ayurveda-vs-hormonal-pills-pcod",
        "title": "Ayurveda vs Oral Contraceptive Pills (OCPs) for PCOD & PCOS",
        "meta_title": "Ayurveda vs Birth Control Pills for PCOD in Pune | Karmanya Ayurveda",
        "meta_desc": "Comparing Ayurvedic root-cause cycle regularisation with birth control pills for PCOD and hormonal imbalance. Female physician-led care in Pimple Saudagar.",
        "condition_name": "PCOD & Hormonal Health",
        "condition_url": "/conditions/womens-health-pcod-hormonal/",
        "read_time": "7 min read",
        "summary": "For millions of women diagnosed with PCOD/PCOS, oral contraceptive pills (OCPs) are prescribed to force a monthly withdrawal bleed. But what happens when you stop taking the pill? This clinical guide explores why Ayurvedic medicine treats the underlying metabolic and ovulatory root cause rather than creating synthetic hormonal dependency.",
        "table": [
            ("Parameter", "Ayurvedic Clinical Care (Dr. Tejasvi Mulik)", "Oral Contraceptive Pills (OCPs)"),
            ("Primary Action", "Stimulates natural spontaneous ovulation and corrects metabolic Agni", "Suppresses natural ovulation entirely and triggers artificial withdrawal bleed"),
            ("Long-term Effect", "Sustained regular menstrual cycles after completing treatment course", "Post-pill amenorrhea and rebound symptom flare once pills are discontinued"),
            ("Weight & Metabolism", "Corrects insulin resistance, clears Kapha stagnation, aids sustainable fat loss", "Can exacerbate insulin sensitivity issues, water retention, and mood volatility"),
            ("Fertility Support", "Directly prepares the endometrial bed (Garbhashaya) for natural conception", "Contraindicated if actively planning pregnancy; does not improve egg quality"),
            ("Treatment Modality", "Virechana detoxification, Uttara Basti, custom herbal Rasayanas & diet", "Synthetic ethinylestradiol and progestin daily tablets")
        ],
        "sections": [
            {
                "heading": "The Illusion of 'Regular Periods' on Birth Control Pills",
                "content": "A crucial biological fact that many women are not told is that the bleeding experienced while on contraceptive pills is not a true menstrual period; it is a pharmaceutical <em>withdrawal bleed</em> caused by dropping hormone levels during the placebo pill week. No egg is released, and the ovarian cysts remain untouched.<br><br>In Ayurveda, under the clinical leadership of <strong>Dr. Tejasvi Mulik (BAMS)</strong> at Karmanya, PCOD is evaluated as a dual imbalance of <em>Kapha</em> (cellular stagnation, follicular cyst formation, insulin resistance) and <em>Apana Vata</em> (impaired ovulatory rhythm). Treatment focuses on restoring the ovary's innate ability to mature and release follicles naturally."
            },
            {
                "heading": "Comprehensive Ayurvedic Protocol for Natural Hormonal Balance",
                "content": "Our protocol combines specialised <em>Virechana</em> (therapeutic metabolic purgation to clear liver stagnation and hormonal metabolites), <em>Uttara Basti</em> for direct uterine and ovarian nourishment, and classical classical botanicals including Shatavari, Kanchanar Guggulu, and Lodhra. Coupled with an anti-inflammatory dietary chart, this multi-step approach resolves root insulin resistance."
            }
        ],
        "faqs": [
            {
                "q": "Will my PCOD symptoms return once I finish the Ayurvedic course?",
                "a": "Unlike pills which only work while you swallow them daily, Ayurvedic treatment re-establishes your metabolic baseline. Provided you maintain healthy nutrition and circadian sleep habits as guided by Dr. Tejasvi, natural regular cycles remain stable."
            },
            {
                "q": "Can I safely transition off birth control pills to Ayurveda?",
                "a": "Yes. Dr. Tejasvi coordinates an overlap protocol where Ayurvedic metabolic herbs are introduced before tapering off synthetic hormones under clinical observation to prevent severe withdrawal acne and amenorrhea."
            }
        ]
    }
]

# Generate each comparison page
for item in comparisons:
    slug = item['slug']
    out_dir = f"{base_dir}/public/compare/{slug}"
    os.makedirs(out_dir, exist_ok=True)
    
    # Build Table HTML
    headers = item['table'][0]
    rows = item['table'][1:]
    
    table_html = '<div style="overflow-x: auto; margin: var(--space-8) 0; border: 1px solid var(--color-border); border-radius: var(--radius-md); box-shadow: var(--shadow-sm);">'
    table_html += '<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; background: white;">'
    table_html += '<thead style="background: var(--color-primary); color: white;"><tr>'
    for h in headers:
        table_html += f'<th style="padding: 14px 18px; border-bottom: 1px solid var(--color-border); font-weight: 600;">{h}</th>'
    table_html += '</tr></thead><tbody>'
    for r in rows:
        table_html += '<tr style="border-bottom: 1px solid var(--color-border);">'
        table_html += f'<td style="padding: 12px 18px; font-weight: 600; color: var(--color-primary); background: rgba(0,0,0,0.02);">{r[0]}</td>'
        for val in r[1:]:
            table_html += f'<td style="padding: 12px 18px; line-height: 1.5; color: #444;">{val}</td>'
        table_html += '</tr>'
    table_html += '</tbody></table></div>'
    
    # Sections HTML
    sec_html = ""
    for s in item['sections']:
        sec_html += f'<h2 style="font-size: 1.8rem; color: var(--color-primary); margin: var(--space-8) 0 var(--space-3);">{s["heading"]}</h2>'
        sec_html += f'<div style="font-size: 1.05rem; line-height: 1.8; color: #333; margin-bottom: var(--space-6);">{s["content"]}</div>'
        
    # FAQs HTML & Schema
    faqs_html = '<div style="margin-top: var(--space-10); border-top: 2px solid var(--color-accent); padding-top: var(--space-6);">'
    faqs_html += '<h2 style="font-size: 1.8rem; color: var(--color-primary); margin-bottom: var(--space-4);">Frequently Asked Questions</h2>'
    schema_faqs = []
    for f in item['faqs']:
        faqs_html += f'''<div style="border-bottom: 1px solid var(--color-border); padding: var(--space-4) 0;">
            <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-bottom: 6px;">{f["q"]}</h3>
            <p style="color: #555; line-height: 1.7; margin: 0;">{f["a"]}</p>
        </div>'''
        schema_faqs.append({"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}})
    faqs_html += '</div>'
    
    # Schemas
    art_schema = {
        "@context": "https://schema.org",
        "@type": ["Article", "MedicalWebPage"],
        "headline": item['title'],
        "description": item['meta_desc'],
        "url": f"https://karmanyaayurveda.com/compare/{slug}/",
        "publisher": {
            "@type": "MedicalClinic",
            "name": "Karmanya Ayurveda Chikitsalaya",
            "url": "https://karmanyaayurveda.com/"
        },
        "about": {
            "@type": "MedicalCondition",
            "name": item['condition_name']
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
            {"@type": "ListItem", "position": 2, "name": "Treatment Comparisons", "item": "https://karmanyaayurveda.com/compare/"},
            {"@type": "ListItem", "position": 3, "name": item['title'], "item": f"https://karmanyaayurveda.com/compare/{slug}/"}
        ]
    }
    
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="WkG1EsF3jpOenNE3qVR0DVexfFagjIofHbmUS-MM2I4">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{item['meta_title']}</title>
    <meta name="description" content="{item['meta_desc']}">
    <link rel="canonical" href="https://karmanyaayurveda.com/compare/{slug}/">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pimple Saudagar, Pune">
    <meta property="og:title" content="{item['meta_title']}">
    <meta property="og:description" content="{item['meta_desc']}">
    <meta property="og:url" content="https://karmanyaayurveda.com/compare/{slug}/">
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
                <a href="/compare/" style="color: rgba(255,255,255,0.6); text-decoration: none;">Clinical Comparisons</a> &rsaquo; 
                <span style="color: white;">{item['condition_name']}</span>
            </nav>
            <span style="display: inline-block; background: rgba(212,175,55,0.2); border: 1px solid var(--color-accent); color: var(--color-accent); padding: 4px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: var(--space-3);">CLINICAL DECISION GUIDE</span>
            <h1 style="font-size: clamp(1.9rem, 4vw, 3rem); font-weight: 400; line-height: 1.25; margin-bottom: var(--space-4); color: #ffffff;">{item['title']}</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); line-height: 1.6; max-width: 760px; margin-bottom: var(--space-4);">{item['summary']}</p>
            <div style="font-size: 0.85rem; color: rgba(255,255,255,0.7);">
                <span>&#128337; {item['read_time']}</span> &bull; 
                <span>Reviewed by Senior Ayurvedic Physicians at Karmanya</span> &bull; 
                <a href="{item['condition_url']}" style="color: var(--color-accent); text-decoration: underline;">View Full Condition Protocol &rarr;</a>
            </div>
        </div>
    </div>

    <main class="container container-editorial" style="padding-top: var(--space-10); padding-bottom: var(--space-16);">
        <div style="max-width: 820px;">
            
            <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-left: 4px solid var(--color-accent); border-radius: var(--radius-sm); padding: var(--space-6); margin-bottom: var(--space-8);">
                <strong style="color: var(--color-primary); font-size: 1.05rem; display: block; margin-bottom: 6px;">Single Clinic Location Notice</strong>
                <p style="margin: 0; color: #555; font-size: 0.95rem; line-height: 1.6;">All consultations and treatments are conducted exclusively at our single medical centre at <strong>27/11, Swaraj Garden Road, Pimple Saudagar, Pune</strong>. We do not operate remote or franchise branches. Patients travel from across Wakad, Hinjawadi, Baner, Aundh, and PCMC for clinical consultations.</p>
            </div>

            <h2 style="font-size: 1.8rem; color: var(--color-primary); margin-bottom: var(--space-3);">At a Glance: Clinical Comparison Table</h2>
            <p style="color: #666; font-size: 0.95rem; margin-bottom: var(--space-4);">Review the medical objectives, risks, recovery times, and cost structures side by side:</p>
            
            {table_html}

            {sec_html}

            <!-- Consultation CTA Card -->
            <div style="background: var(--color-primary); color: white; border-radius: var(--radius-lg); padding: var(--space-8); margin: var(--space-10) 0; text-align: center;">
                <h3 style="color: white; font-size: 1.8rem; margin-bottom: var(--space-2);">Need an Honest Physician Assessment?</h3>
                <p style="color: rgba(255,255,255,0.85); max-width: 600px; margin: 0 auto var(--space-6); line-height: 1.6;">Bring your MRI, X-rays, or diagnostic reports to our Pimple Saudagar clinic for a dedicated 45-minute pulse diagnosis and orthopaedic evaluation before committing to surgery or long-term medication.</p>
                <div style="display: flex; gap: var(--space-4); justify-content: center; flex-wrap: wrap;">
                    <a href="/book-consultation/" class="btn btn-primary" style="background: var(--color-accent); border-color: var(--color-accent); color: white; padding: 12px 26px;">Book Physician Consultation</a>
                    <a href="https://wa.me/919819820017?text=Hi%2C%20I%20read%20the%20comparison%20guide%20for%20{slug}%20and%20would%20like%20to%20discuss%20my%20case." class="btn btn-secondary" style="border-color: rgba(255,255,255,0.4); color: white; padding: 12px 26px;">Ask on WhatsApp</a>
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
    print(f"  ✅ /compare/{slug}/")

# Generate /compare/ hub
hub_cards = ""
for item in comparisons:
    hub_cards += f"""
    <div style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-8); box-shadow: var(--shadow-sm); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
            <span style="font-size: 0.75rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: var(--space-2);">{item['condition_name']}</span>
            <h2 style="font-size: 1.4rem; margin-bottom: var(--space-3);"><a href="/compare/{item['slug']}/" style="color: var(--color-primary); text-decoration: none; line-height: 1.3;">{item['title']}</a></h2>
            <p style="color: #555; font-size: 0.95rem; line-height: 1.6; margin-bottom: var(--space-4);">{item['meta_desc']}</p>
        </div>
        <div>
            <a href="/compare/{item['slug']}/" class="btn btn-secondary" style="font-size: 0.9rem; padding: 8px 18px;">Read Full Comparison &rarr;</a>
        </div>
    </div>"""

hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="google-site-verification" content="WkG1EsF3jpOenNE3qVR0DVexfFagjIofHbmUS-MM2I4">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayurvedic vs Modern Medical Treatment Comparisons | Karmanya Pune</title>
    <meta name="description" content="Objective clinical comparisons between Ayurvedic protocols and surgery/long-term medications for knee pain, sciatica, and PCOD. Karmanya Ayurveda, Pimple Saudagar.">
    <link rel="canonical" href="https://karmanyaayurveda.com/compare/">
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
            <span style="color: var(--color-accent); font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">EVIDENCE &amp; ALTERNATIVES</span>
            <h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0; color: #ffffff;">Clinical Treatment Comparisons</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 680px; margin: 0 auto;">Make informed decisions about your healthcare. Read evidence-based, transparent comparisons between classical Ayurvedic care and invasive surgical or long-term medication routes.</p>
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

os.makedirs(f"{base_dir}/public/compare", exist_ok=True)
with open(f"{base_dir}/public/compare/index.html", "w") as f:
    f.write(hub_html)
print("  ✅ /compare/ Hub")
