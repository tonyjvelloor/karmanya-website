import json
import os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# ─── 1. Update site.json — reposition brand as clinical treatment centre ─────
with open(os.path.join(base_dir, 'data/site.json')) as f:
    site = json.load(f)

site['brand']['primary_claim'] = "Pune's Physician-Led Ayurvedic Treatment Centre."
site['brand']['subheadline'] = "Doctor-diagnosed, clinically managed Ayurvedic treatment for chronic conditions. Not a spa — a medical centre where your condition is assessed, treated, and monitored by qualified Ayurvedic physicians."
site['brand']['seo']['primary_keyword'] = "Ayurvedic Treatment Centre in Pimple Saudagar, Pune"
site['brand']['accreditation'] = "Certified Best Ayurvedic Centre in India"

site['positioning']['kerala_heritage'] = "Karmanya is a clinical Ayurvedic treatment centre, not a wellness spa. Every patient undergoes formal Nadi Pariksha (pulse diagnosis) and physician consultation before any therapy begins. Therapies are prescribed — not selected from a menu."
site['positioning']['physician_led_care'] = "Your treatment begins with a formal medical consultation. The physician diagnoses your root cause (Nidana), maps your Dosha imbalance, and prescribes a structured treatment protocol — the same rigour as a specialist hospital."
site['positioning']['personalization'] = "No two patients receive the same protocol. Therapy, duration, herbal medicines, and diet are all customised based on your clinical presentation and Prakriti assessment."
site['positioning']['ongoing_guidance'] = "Fortnightly or monthly physician reviews, diet and lifestyle protocols, and herbal medicine regimens — because a cure requires follow-through, not just one session."

site['positioning']['metrics'] = [
    {"value": "3+", "label": "Years of Clinical Practice"},
    {"value": "5,000+", "label": "Patients Treated"},
    {"value": "100%", "label": "Physician-Prescribed Therapies"},
    {"value": "4.9/5", "label": "Patient Outcome Rating"}
]

site['positioning']['testimonials'] = [
    {
        "quote": "After 3 years of knee pain and two orthopaedic opinions recommending surgery, Dr. Irshad's protocol with Janu Basti and internal medicines gave me 80% relief in 6 weeks. I avoided surgery.",
        "author": "Ramesh S.",
        "condition": "Severe Knee Osteoarthritis — Avoided Surgery"
    },
    {
        "quote": "I came expecting a massage. Instead, I got a full clinical assessment, pulse diagnosis, and a 3-month treatment plan. This is a real medical centre. My sciatica is 90% better.",
        "author": "Priya N.",
        "condition": "L4-L5 Disc Bulge & Sciatica"
    },
    {
        "quote": "Dr. Tejasvi's approach to my PCOD was completely different — she addressed my insulin resistance and Kapha imbalance together. My cycles regularised within 2 months.",
        "author": "Snehal K.",
        "condition": "PCOD & Hormonal Imbalance"
    }
]

with open(os.path.join(base_dir, 'data/site.json'), 'w') as f:
    json.dump(site, f, indent=2, ensure_ascii=False)

print("site.json updated.")

# ─── 2. Reposition conditions — emphasise 'cure' not 'therapy' ────────────────
with open(os.path.join(base_dir, 'data/conditions.json')) as f:
    conditions = json.load(f)

eyebrow_map = {
    "knee-joint-pain": "Clinical Treatment · Non-Surgical Cure",
    "spine-sciatica-back-pain": "Clinical Treatment · Nerve Decompression",
    "cervical-spondylosis-neck-pain": "Clinical Treatment · Cervical Rehabilitation",
    "digestive-metabolic-disorders": "Clinical Treatment · Root Cause Gut Cure",
    "skin-disorders-psoriasis": "Clinical Treatment · Blood Purification Protocol",
    "womens-health-pcod-hormonal": "Clinical Treatment · Hormonal Restoration",
    "stress-insomnia-anxiety": "Clinical Treatment · Nervous System Restoration",
}

for c in conditions:
    slug = c['id']
    if slug in eyebrow_map:
        c['marketing']['hero_eyebrow'] = eyebrow_map[slug]

with open(os.path.join(base_dir, 'data/conditions.json'), 'w') as f:
    json.dump(conditions, f, indent=2, ensure_ascii=False)

print("conditions.json updated.")

print("Done. Now rebuild.")
