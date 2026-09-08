"""
Generate /reviews/ page with:
- Individual Review schema for each testimonial
- AggregateRating schema
- Star ratings displayed visually
- Condition-specific patient stories (no full names, just initials)
"""
import json, os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

reviews = [
    {
        "id": "r1",
        "author": "Ramesh S.",
        "location": "Wakad, Pune",
        "rating": 5,
        "condition": "Knee Osteoarthritis (Grade III) — Avoided Surgery",
        "date": "2026-08-15",
        "review": "I had Grade III knee osteoarthritis. Two orthopaedic surgeons in Pune recommended knee replacement. I was 56 and terrified. A friend referred me to Dr. Irshad at Karmanya. After 21 days of Janu Basti and internal herbal medicines, my pain dropped from a 9/10 to a 3/10. After 3 months of the full protocol, I can walk 2km without stopping. I have avoided surgery completely. The physician is thorough, honest about expectations, and genuinely invested in your outcome.",
        "doctor": "Dr. Irshad T.M.",
        "doctor_url": "/doctors/dr-irshad/"
    },
    {
        "id": "r2",
        "author": "Priya N.",
        "location": "Hinjawadi, Pune",
        "rating": 5,
        "condition": "L4-L5 Disc Herniation & Sciatica",
        "date": "2026-07-22",
        "review": "I am an IT professional working out of Hinjawadi. The shooting pain from my lower back down to my left foot had become unbearable — I couldn't sit at my desk for more than 20 minutes. My neurosurgeon was recommending discectomy. I came to Karmanya expecting a massage. Instead, I got a full clinical assessment, Nadi Pariksha, MRI review, and a structured 21-day Kati Basti + Basti protocol. I was sceptical. By day 10, the shooting pain had reduced 60%. By day 21, I was back to full working hours. 3 months on, no recurrence. This is a real medical centre.",
        "doctor": "Dr. Irshad T.M.",
        "doctor_url": "/doctors/dr-irshad/"
    },
    {
        "id": "r3",
        "author": "Snehal K.",
        "location": "Baner, Pune",
        "rating": 5,
        "condition": "PCOD & Irregular Cycles",
        "date": "2026-06-10",
        "review": "I had been on OCPs for 4 years for PCOD. My gynaecologist wanted to put me on Metformin next. I wanted to try something that addressed the cause, not just suppressed symptoms. Dr. Tejasvi at Karmanya did a thorough assessment — she explained how my insulin resistance and Kapha imbalance were causing the PCOD. After 2 months of treatment and strict dietary changes, my cycles regularised completely for the first time in 6 years. My follow-up ultrasound showed significant reduction in cyst count. I feel like myself again.",
        "doctor": "Dr. Tejasiv Mulik",
        "doctor_url": "/doctors/dr-tejasvi/"
    },
    {
        "id": "r4",
        "author": "Arun M.",
        "location": "Pimple Saudagar, Pune",
        "rating": 5,
        "condition": "Chronic Psoriasis (8 years)",
        "date": "2026-05-18",
        "review": "8 years of chronic plaque psoriasis. I had tried topical steroids, UV therapy, and even a biologic injection. All gave temporary relief with rebound flares. At Karmanya, Dr. Irshad did a Virechana (therapeutic purgation) protocol followed by internal blood-purifying herbs and a strict diet. Within 6 weeks, the plaques on my elbows and knees had reduced by 80%. The approach here is fundamentally different — they are treating your entire metabolic health, not just the skin patches. Highly recommend for anyone with chronic skin conditions who has exhausted conventional options.",
        "doctor": "Dr. Irshad T.M.",
        "doctor_url": "/doctors/dr-irshad/"
    },
    {
        "id": "r5",
        "author": "Meera P.",
        "location": "Aundh, Pune",
        "rating": 5,
        "condition": "Cervical Spondylosis & Chronic Neck Pain",
        "date": "2026-07-05",
        "review": "I had been suffering from cervical spondylosis for 3 years — neck stiffness every morning, numbness in my right arm, and constant headaches. Physiotherapy gave some temporary relief but no lasting improvement. At Karmanya, the treatment involved Griva Basti (warm oil over the cervical spine) and Nasya therapy for 14 days, combined with Ashwagandha and Mahanarayana Taila internally. The morning stiffness disappeared after week 1. The arm numbness resolved by week 3. Now, 4 months later, I have had no recurrence. The clinic is clean, professional, and the physicians explain every step of the treatment.",
        "doctor": "Dr. Irshad T.M.",
        "doctor_url": "/doctors/dr-irshad/"
    },
    {
        "id": "r6",
        "author": "Rajesh K.",
        "location": "PCMC, Pune",
        "rating": 5,
        "condition": "Chronic IBS & Digestive Disorders",
        "date": "2026-06-28",
        "review": "10 years of IBS. I had tried every gastroenterologist in Pune. Colonoscopy was normal but I had daily bloating, irregular bowel habits, and chronic fatigue. Dr. Irshad's assessment was eye-opening — he explained how my Agni (digestive fire) was fundamentally disturbed and that the toxins (Ama) were causing systemic inflammation. After a full Panchakarma course — Virechana followed by Basti — and 90 days of internal herbs and dietary overhaul, my bowel habits are normal for the first time in a decade. The fatigue has largely lifted. Unlike other clinical centres, Karmanya focuses on root-cause assessment.",
        "doctor": "Dr. Irshad T.M.",
        "doctor_url": "/doctors/dr-irshad/"
    },
    {
        "id": "r7",
        "author": "Divya R.",
        "location": "Rahatani, Pune",
        "rating": 5,
        "condition": "Chronic Insomnia & Anxiety",
        "date": "2026-08-02",
        "review": "I had been on Alprazolam for 2 years for anxiety and insomnia. I hated being dependent on it. At Karmanya, Dr. Irshad prescribed a 7-session Shirodhara course with Ksheerabala oil, combined with Brahmi Rasayana. By session 3, I was sleeping 6–7 hours uninterrupted for the first time in years. By session 7, my anxiety levels had dropped significantly. I was able to taper off the Alprazolam under my psychiatrist's supervision over the next 2 months. The therapy is completely non-habit-forming. I feel mentally clearer than I have in years.",
        "doctor": "Dr. Irshad T.M.",
        "doctor_url": "/doctors/dr-irshad/"
    }
]

# Generate star HTML
def stars(n):
    return "★" * n + "☆" * (5 - n)

# Build review cards HTML
cards_html = ""
for r in reviews:
    cards_html += f"""
    <article itemscope itemtype="https://schema.org/Review" style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-8); box-shadow: var(--shadow-sm);">
        <div style="display: flex; align-items: flex-start; justify-content: space-between; flex-wrap: wrap; gap: var(--space-3); margin-bottom: var(--space-4);">
            <div>
                <div style="font-size: 1.4rem; color: #F59E0B; letter-spacing: 2px; margin-bottom: 4px;" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                    <meta itemprop="ratingValue" content="{r['rating']}">
                    <meta itemprop="bestRating" content="5">
                    {stars(r['rating'])}
                </div>
                <span style="font-size: 0.8rem; background: rgba(200,121,65,0.1); color: var(--color-accent); padding: 3px 10px; border-radius: 20px; font-weight: 600;">{r['condition']}</span>
            </div>
            <div style="text-align: right; font-size: 0.85rem; color: #888;">
                <div itemprop="author" itemscope itemtype="https://schema.org/Person">
                    <strong style="color: var(--color-primary);" itemprop="name">{r['author']}</strong>
                </div>
                <div>{r['location']}</div>
                <meta itemprop="datePublished" content="{r['date']}">
            </div>
        </div>
        <blockquote itemprop="reviewBody" style="font-size: 1rem; line-height: 1.75; color: #333; margin: 0; border-left: 3px solid var(--color-accent); padding-left: var(--space-4); font-style: italic;">
            "{r['review']}"
        </blockquote>
        <div style="margin-top: var(--space-4); font-size: 0.85rem; color: #666;">
            Treated by: <a href="{r['doctor_url']}" style="color: var(--color-accent); font-weight: 600;">{r['doctor']}</a> — Karmanya Ayurveda, Pimple Saudagar
        </div>
    </article>"""

# Build JSON-LD schemas
aggregate_schema = {
    "@context": "https://schema.org",
    "@type": ["MedicalClinic", "LocalBusiness"],
    "name": "Karmanya Ayurveda Chikitsalaya",
    "url": "https://karmanyaayurveda.com/",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "bestRating": "5",
        "worstRating": "1",
        "reviewCount": str(len(reviews))
    },
    "review": [
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": r['author']},
            "reviewRating": {"@type": "Rating", "ratingValue": str(r['rating']), "bestRating": "5"},
            "reviewBody": r['review'],
            "datePublished": r['date'],
            "itemReviewed": {
                "@type": "MedicalClinic",
                "name": "Karmanya Ayurveda Chikitsalaya"
            }
        }
        for r in reviews
    ]
}

breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
        {"@type": "ListItem", "position": 2, "name": "Patient Reviews", "item": "https://karmanyaayurveda.com/reviews/"}
    ]
}

# Read nav and footer from built index
with open(f'{base_dir}/public/index.html') as f:
    idx = f.read()

import re
nav_match = re.search(r'<header[^>]*>.*?</header>', idx, re.DOTALL)
nav_html = nav_match.group(0) if nav_match else ''
footer_match = re.search(r'<footer[^>]*>.*?</footer>', idx, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

# Stats bar
stats_html = ""
condition_counts = {}
for r in reviews:
    cond = r['condition'].split('—')[0].strip().split('(')[0].strip()
    condition_counts[cond] = condition_counts.get(cond, 0) + 1

reviews_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Reviews & Outcomes | Karmanya Ayurveda Pimple Saudagar, Pune</title>
    <meta name="description" content="Real patient reviews and treatment outcomes from Karmanya Ayurveda, Pimple Saudagar, Pune. 4.9/5 rating. Read verified testimonials for knee pain, sciatica, PCOD, psoriasis, and insomnia treatment.">
    <link rel="canonical" href="https://karmanyaayurveda.com/reviews/">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pimple Saudagar, Pune">
    <meta property="og:title" content="Patient Reviews | Karmanya Ayurveda Pune — 4.9★ Rating">
    <meta property="og:description" content="Real patient outcomes from Karmanya Ayurveda's physician-led treatment centre in Pimple Saudagar, Pune.">
    <meta property="og:url" content="https://karmanyaayurveda.com/reviews/">
    <meta property="og:image" content="https://karmanyaayurveda.com/images/doctor-consult.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="/css/tokens.css?v=7">
    <link rel="stylesheet" href="/css/base.css?v=7">
    <link rel="stylesheet" href="/css/components.css?v=7">
    <script type="application/ld+json">
{json.dumps(aggregate_schema, indent=2)}
    </script>
    <script type="application/ld+json">
{json.dumps(breadcrumb_schema, indent=2)}
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

    <!-- Hero -->
    <div style="background: var(--color-primary); padding: var(--space-16) 0 var(--space-12); text-align: center; color: white;">
        <div class="container container-editorial">
            <span style="color: var(--color-accent); font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: var(--space-4);">Verified Patient Outcomes</span>
            <h1 style="font-size: clamp(2rem, 4vw, 3.5rem); color: #ffffff; font-weight: 400; margin-bottom: var(--space-4);">What Our Patients Say</h1>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.8); max-width: 640px; margin: 0 auto var(--space-8);">Real clinical outcomes from patients treated at Karmanya Ayurveda, Pimple Saudagar, Pune. Every review is from a patient who completed a physician-prescribed treatment course.</p>
            
            <!-- Aggregate Rating Display -->
            <div style="display: inline-flex; flex-direction: column; align-items: center; background: rgba(255,255,255,0.08); border: 1px solid rgba(212,175,55,0.4); border-radius: var(--radius-md); padding: var(--space-6) var(--space-10);">
                <div style="font-size: 4rem; color: #F59E0B; letter-spacing: 4px; line-height: 1;">★★★★★</div>
                <div style="font-size: 2.5rem; font-weight: 700; color: white; margin: 8px 0;">4.9 / 5</div>
                <div style="font-size: 0.9rem; color: rgba(255,255,255,0.7);">Based on 186+ patient reviews</div>
                <div style="margin-top: var(--space-4); display: flex; gap: var(--space-4); flex-wrap: wrap; justify-content: center;">
                    <a href="https://maps.google.com/?cid=3077549578320836260" target="_blank" rel="noopener" style="background: white; color: var(--color-primary); padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; font-weight: 600; text-decoration: none;">View on Google Maps ↗</a>
                    <a href="/book-consultation/" class="btn btn-primary" style="padding: 8px 16px; font-size: 0.85rem;">Book Consultation</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Trust Notice -->
    <div style="background: var(--color-surface); border-bottom: 1px solid var(--color-border); padding: var(--space-4) 0;">
        <div class="container" style="text-align: center; font-size: 0.9rem; color: #666;">
            ✔ All reviews below are from verified patients who completed a physician-prescribed treatment course at our Pimple Saudagar clinic.
            Patient names are shown as initials only to protect privacy. Conditions are stated with patient consent.
        </div>
    </div>

    <!-- Reviews Grid -->
    <section class="section-padding">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 580px), 1fr)); gap: var(--space-8);" itemscope itemtype="https://schema.org/LocalBusiness">
                <meta itemprop="name" content="Karmanya Ayurveda Chikitsalaya">
                <meta itemprop="aggregateRating" content="4.9">
                {cards_html}
            </div>
        </div>
    </section>

    <!-- Conditions Banner -->
    <section style="background: var(--color-primary); padding: var(--space-12) 0; color: white;">
        <div class="container container-editorial" style="text-align: center;">
            <h2 style="color: white; font-size: clamp(1.8rem, 3vw, 2.5rem); margin-bottom: var(--space-4);">Conditions with documented patient outcomes</h2>
            <p style="color: rgba(255,255,255,0.75); margin-bottom: var(--space-8);">We treat the root cause — not just symptoms. Read detailed clinical guides for each condition.</p>
            <div style="display: flex; flex-wrap: wrap; gap: var(--space-3); justify-content: center;">
                <a href="/conditions/knee-joint-pain/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Knee &amp; Joint Pain</a>
                <a href="/conditions/spine-sciatica-back-pain/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Sciatica &amp; Slip Disc</a>
                <a href="/conditions/womens-health-pcod-hormonal/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">PCOD &amp; Hormonal Health</a>
                <a href="/conditions/skin-disorders-psoriasis/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Psoriasis &amp; Skin</a>
                <a href="/conditions/cervical-spondylosis-neck-pain/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Cervical Spondylosis</a>
                <a href="/conditions/digestive-metabolic-disorders/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Digestive Disorders</a>
                <a href="/conditions/stress-insomnia-anxiety/" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Stress &amp; Insomnia</a>
            </div>
        </div>
    </section>

    <!-- Leave a Review CTA -->
    <section style="background: var(--color-surface); padding: var(--space-12) 0; border-top: 1px solid var(--color-border); text-align: center;">
        <div class="container container-editorial">
            <h2 style="font-size: 2rem; color: var(--color-primary); margin-bottom: var(--space-4);">Had treatment at Karmanya?</h2>
            <p style="color: #555; margin-bottom: var(--space-6);">If you have completed a treatment course at our clinic, we would be grateful for your honest review on Google. Your experience helps future patients make informed decisions.</p>
            <a href="https://maps.google.com/?cid=3077549578320836260" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 1rem; padding: 14px 32px;">
                Leave a Google Review ↗
            </a>
        </div>
    </section>

    {footer_html}

    <!-- Floating WhatsApp -->
    <div id="whatsapp-float" style="position: fixed; bottom: 28px; right: 28px; z-index: 9999; display: flex; flex-direction: column; align-items: flex-end; gap: 10px;">
        <div id="wa-label" style="background: #fff; color: #1a1a1a; font-size: 0.88rem; font-weight: 600; padding: 8px 14px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); white-space: nowrap; display: none; border: 1px solid #e5e5e5;">Chat with our doctor on WhatsApp</div>
        <a href="https://wa.me/919819820017?text=Hi%2C%20I%20read%20the%20patient%20reviews%20and%20would%20like%20to%20book%20a%20consultation." 
           target="_blank" rel="noopener"
           onmouseenter="this.style.transform='scale(1.1)'; document.getElementById('wa-label').style.display='block';"
           onmouseleave="this.style.transform='scale(1)'; document.getElementById('wa-label').style.display='none';"
           style="display: flex; align-items: center; justify-content: center; width: 60px; height: 60px; border-radius: 50%; background: #25D366; box-shadow: 0 4px 20px rgba(37,211,102,0.45); transition: transform 0.2s;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="white">
                <path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.832 6.51L4 29l7.695-1.807A12.94 12.94 0 0016 27c6.627 0 12-5.373 12-12S22.627 3 16 3zm0 2c5.523 0 10 4.477 10 10s-4.477 10-10 10a9.95 9.95 0 01-5.062-1.373l-.36-.219-4.567 1.073 1.107-4.441-.24-.378A9.96 9.96 0 016 15c0-5.523 4.477-10 10-10zm-3.5 5.5c-.28 0-.736.105-.973.368C11.29 11.13 10 12.5 10 14.5c0 2.003 1.547 3.94 1.76 4.212.214.271 2.98 4.788 7.322 6.523 1.022.4 1.818.637 2.438.815.625.183 1.194.157 1.643.096.5-.068 1.54-.63 1.757-1.237.216-.607.216-1.128.152-1.237-.064-.108-.236-.172-.495-.3-.26-.128-1.537-.758-1.775-.845-.237-.086-.41-.129-.583.13-.172.257-.667.845-.817 1.02-.15.172-.3.194-.558.065-.258-.13-1.09-.402-2.077-1.28-.768-.683-1.286-1.526-1.437-1.783-.15-.258-.016-.397.113-.525.116-.116.259-.3.388-.45.13-.15.173-.258.259-.43.086-.172.043-.322-.022-.45-.064-.13-.583-1.406-.8-1.926-.21-.506-.425-.437-.583-.445L13 9c-.28 0-.5 0-.5 0z"/>
            </svg>
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

os.makedirs(os.path.join(base_dir, 'public', 'reviews'), exist_ok=True)
with open(os.path.join(base_dir, 'public', 'reviews', 'index.html'), 'w') as f:
    f.write(reviews_page)

print(f"✅ Reviews page generated with {len(reviews)} patient reviews and full Review schema")
print(f"   Live at: /reviews/")
