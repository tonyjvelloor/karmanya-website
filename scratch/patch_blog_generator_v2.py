import re
import os

blog_gen_path = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/scratch/generate_blog.py'

with open(blog_gen_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Replace Dr. Irshad author references with Dr. Tejasvi Mulik
code = code.replace('"author": "Dr. Irshad T.M., BAMS, MD (Ayurveda)"', '"author": "Dr. Tejasvi Mulik, BAMS"')
code = code.replace('"author_url": "/doctors/dr-irshad/"', '"author_url": "/doctors/dr-tejasvi/"')
code = code.replace("Hello Karmanya Ayurveda", "Hi Dr. Tejasvi")
code = code.replace("Hello Karmanya Ayurveda", "Hello Dr. Tejasvi")
code = code.replace("dr-irshad-portrait.jpg", "dr-tejasvi-portrait.webp")
code = code.replace("dr-irshad-portrait.webp", "dr-tejasvi-portrait.webp")

# 2. Add the 3 new blog articles before line `# ─── BLOG POST TEMPLATE ──────────────────`
new_articles = """,
{
  "slug": "ayurvedic-treatment-diabetes-madhumeha-pune",
  "title": "Ayurvedic Treatment for Type 2 Diabetes in Pune: Root-Cause Sugar Control vs Metformin",
  "meta_title": "Ayurvedic Diabetes Treatment in Pune | Root-Cause Sugar Control",
  "meta_desc": "Manage Type-2 Diabetes and insulin resistance naturally with authentic Kerala Ayurveda in Pune. Discover how Virechana detox and herbs protect pancreatic function.",
  "category": "Metabolic Health",
  "date": "October 28, 2026",
  "author": "Dr. Tejasvi Mulik, BAMS",
  "author_url": "/doctors/dr-tejasvi/",
  "condition_url": "/conditions/diabetes-madhumeha/",
  "read_time": "7 min read",
  "intro": "Over 100 million people in India are currently living with Type-2 Diabetes, with urban centers like Pune showing rising incidence among professionals in their 30s and 40s. While modern allopathic protocols rely heavily on lifelong Metformin or sulfonylureas to chemically suppress blood glucose readings, classical Kerala Ayurveda addresses the underlying metabolic engine — repairing impaired digestive fire (Agnimandya), reducing cellular insulin resistance, and clearing liver-pancreatic stagnation without toxic side effects.",
  "sections": [
    {
      "heading": "Direct Answer: How Does Ayurveda Treat Type 2 Diabetes (Madhumeha)?",
      "body": "Ayurvedic treatment for Type-2 Diabetes treats the root metabolic impairment rather than merely lowering laboratory blood sugar figures. Through classical Nadi Pariksha, senior BAMS physicians identify liver-pancreatic Ama (metabolic toxins) and vitiated Kapha-Pitta doshas. A targeted combination of Virechana (Panchakarma detox), Udvartana (lymphatic fat-scraping scrub), and bio-active herbs (Gudmar, Vijaysar, Shilajit, Nisha Amalaki) restores insulin sensitivity, protects kidney-eye microvasculature, and prevents diabetic neuropathy."
    },
    {
      "heading": "Ayurvedic Management vs Long-Term Metformin Therapy",
      "body": "<table style='width:100%; border-collapse:collapse; margin:20px 0; font-size:0.95rem; background:#fff; border:1px solid #ddd;'><thead><tr style='background:#f4f6f1; border-bottom:2px solid #2c3e2d;'><th style='padding:12px; text-align:left;'>Clinical Parameter</th><th style='padding:12px; text-align:left;'>Conventional Protocol (Metformin)</th><th style='padding:12px; text-align:left;'>Kerala Ayurveda Protocol (Karmanya)</th></tr></thead><tbody><tr style='border-bottom:1px solid #eee;'><td style='padding:12px;'><strong>Primary Target</strong></td><td style='padding:12px;'>Suppresses hepatic gluconeogenesis; chemical sugar masking</td><td style='padding:12px;'>Stimulates cellular Agni (digestive fire); clears channel endotoxins</td></tr><tr style='border-bottom:1px solid #eee;'><td style='padding:12px;'><strong>Pancreatic Rejuvenation</strong></td><td style='padding:12px;'>None; beta-cell exhaustion often progresses over 5-10 years</td><td style='padding:12px;'>Rasayana herbs (Amalaki, Shilajit) nourish and protect pancreatic cells</td></tr><tr style='border-bottom:1px solid #eee;'><td style='padding:12px;'><strong>Common Side Effects</strong></td><td style='padding:12px;'>GI distress, lactic acidosis risk, Vitamin B12 deficiency</td><td style='padding:12px;'>Zero chemical toxicity; improves gut digestion and energy levels</td></tr><tr><td style='padding:12px;'><strong>Neuropathy Protection</strong></td><td style='padding:12px;'>Symptom-masking painkillers (Pregabalin / Gabapentin)</td><td style='padding:12px;'>Kashaya Dhara and Ksheerabala Tailam for genuine nerve regeneration</td></tr></tbody></table>"
    },
    {
      "heading": "Panchakarma Protocols for Diabetic Neuropathy and Insulin Resistance",
      "body": "At Karmanya Ayurveda in Pimple Saudagar, diabetes care is strictly supervised by our senior BAMS physicians following pulse assessment. For systemic metabolic reset, Virechana (therapeutic purgation) expels morbid Pitta and sluggish bile from the gastrointestinal tract, immediately improving glucose uptake. For patients suffering from diabetic peripheral neuropathy — marked by burning sensations, numbness, or needle-like pain in the feet — localized Kashaya Dhara (warm medicated herbal decoction streaming) and Padabhyanga restore healthy blood microcirculation to peripheral nerves."
    }
  ],
  "faqs": [
    {
      "q": "Can I safely integrate Ayurvedic diabetes medicines with my allopathic tablets?",
      "a": "Yes. Ayurvedic therapies are integrated safely alongside your existing prescription. Our physicians track fasting and postprandial glucose levels carefully, adjusting botanical formulations so that your allopathic doctor can gradually taper dosages as your natural insulin sensitivity improves."
    },
    {
      "q": "How soon will HbA1c levels show improvement with Ayurvedic treatment?",
      "a": "Most patients observe significant stabilization in daily fasting blood sugars within 3 to 4 weeks, with measurable reductions in HbA1c (typically 0.8% to 1.5% reduction) within a full 90-day clinical protocol alongside prescribed dietary guidelines."
    }
  ]
},
{
  "slug": "ayurvedic-treatment-hypertension-high-bp-pune",
  "title": "Ayurvedic Treatment for High Blood Pressure in Pune: Shirodhara, Sarpagandha & Stress Regulation",
  "meta_title": "Ayurvedic Hypertension Treatment in Pune | Natural BP Control",
  "meta_desc": "Struggling with high blood pressure and stress? Discover how classical Kerala Shirodhara and Sarpagandha lower blood pressure naturally at Karmanya Ayurveda Pune.",
  "category": "Cardiovascular Health",
  "date": "October 28, 2026",
  "author": "Dr. Tejasvi Mulik, BAMS",
  "author_url": "/doctors/dr-tejasvi/",
  "condition_url": "/conditions/hypertension-high-bp/",
  "read_time": "6 min read",
  "intro": "High blood pressure (Hypertension) is often dubbed the 'silent killer' because it damages vital organs without overt early warning signs. In modern urban lifestyles — especially among IT executives commuting between Hinjawadi, Wakad, and Pune city — sustained sympathetic nervous system overactivation elevates blood pressure to chronic levels. Classical Kerala Ayurveda classifies hypertension as Rakta Gata Vata, offering profound non-pharmacological therapies that calm arterial resistance and restore autonomic nervous balance.",
  "sections": [
    {
      "heading": "Direct Answer: How Does Classical Ayurveda Lower High Blood Pressure?",
      "body": "Ayurveda regulates hypertension by simultaneously calming the autonomic sympathetic nervous system and soothing arterial vascular tension. Using continuous warm oil forehead streaming (Shirodhara and Takradhara), therapies activate the parasympathetic vagal response, reducing plasma cortisol and epinephrine within 45 minutes. Paired with classical Medhya Rasayana herbs like Sarpagandha (Rauwolfia serpentina) and Arjuna, arterial walls relax and blood pressure stabilizes naturally."
    },
    {
      "heading": "The Clinical Mechanism of Shirodhara for Hypertension",
      "body": "Shirodhara is not a cosmetic spa massage; it is an intensive neurological therapy described in the Charaka Samhita. During the 45-minute procedure, a continuous, pendulum-like rhythmic stream of medicated herbal oil (or buttermilk infused with Musta and Amalaki, known as Takradhara) is poured across the forehead directly over the third-eye center (Ajna chakra). Clinical studies demonstrate that this continuous tactile stimulation induces an alpha-brainwave state, causes systemic vasodilation, reduces cardiac workload, and measurably lowers systolic and diastolic blood pressure."
    },
    {
      "heading": "Cardioprotective Ayurvedic Herbal Formulations",
      "body": "Under the guidance of Dr. Tejasvi Mulik, patients receive precise botanical prescriptions: <strong>1. Sarpagandha:</strong> Rich in reserpine, it gently lowers peripheral vascular resistance and calms mental agitation. <strong>2. Arjuna Bark:</strong> Rich in co-enzyme Q10 and bioflavonoids, it strengthens myocardium muscle contraction and arterial elasticity. <strong>3. Brahmi & Shankhapushpi:</strong> Calms nocturnal cortisol surges and alleviates sleep-onset insomnia."
    }
  ],
  "faqs": [
    {
      "q": "Can I replace my blood pressure tablets with Ayurvedic herbs?",
      "a": "Never discontinue allopathic anti-hypertensive drugs abruptly, as sudden cessation can trigger rebound hypertensive crises. Ayurvedic treatment is introduced concurrently. As autonomic stress subsides and BP readings normalize, dosage tapering is coordinated safely under medical review."
    },
    {
      "q": "How many sessions of Shirodhara are required for hypertension?",
      "a": "A continuous 7-day or 14-day intensive protocol is typically recommended for chronic or stress-induced hypertension, often scheduled conveniently during holiday periods like the Diwali vacation."
    }
  ]
},
{
  "slug": "ayurvedic-weight-loss-treatment-udvartana-pune",
  "title": "Ayurvedic Weight Loss & Obesity Treatment in Pune: How Udvartana Burns Stubborn Fat Sustainably",
  "meta_title": "Ayurvedic Weight Loss & Obesity Treatment in Pune | Udvartana",
  "meta_desc": "Struggling to lose stubborn belly and visceral fat? Experience authentic Udvartana herbal powder scrub and Panchakarma for natural weight loss in Pimple Saudagar.",
  "category": "Metabolic Health",
  "date": "October 28, 2026",
  "author": "Dr. Tejasvi Mulik, BAMS",
  "author_url": "/doctors/dr-tejasvi/",
  "condition_url": "/conditions/obesity-weight-loss/",
  "read_time": "6 min read",
  "intro": "Why do 95% of conventional crash diets and intense cardio regimens fail over a 12-month horizon? Because starvation diets trigger evolutionary metabolic panic, lowering your Basal Metabolic Rate (BMR) and prompting rapid rebound weight gain the moment normal eating resumes. Classical Ayurveda approaches obesity (Sthaulya) as a dysfunction of Meda Dhatu (adipose tissue) and impaired cellular digestive fire (Dhatvagni). Through therapies like Udvartana and Virechana, Ayurveda resets your metabolic rate for permanent, healthy weight management.",
  "sections": [
    {
      "heading": "Direct Answer: What Is Udvartana and How Does It Accelerate Weight Loss?",
      "body": "Udvartana is a vigorous, upward therapeutic deep-tissue scrub using warm, dry herbal powders (such as Triphala, Kolakulathadi, and Musta). The intense friction generates deep subcutaneous heat, opening obstructed lymphatic micro-channels, liquefying stubborn adipose deposits, and eliminating systemic metabolic toxins (Ama). Unlike gym dehydration, Udvartana enhances skin firmness, reduces cellulite, and accelerates metabolic fat breakdown sustainably."
    },
    {
      "heading": "Ayurvedic Metabolic Reset vs Crash Caloric Deficit",
      "body": "<table style='width:100%; border-collapse:collapse; margin:20px 0; font-size:0.95rem; background:#fff; border:1px solid #ddd;'><thead><tr style='background:#f4f6f1; border-bottom:2px solid #2c3e2d;'><th style='padding:12px; text-align:left;'>Feature</th><th style='padding:12px; text-align:left;'>Crash Dieting / Extreme Gym</th><th style='padding:12px; text-align:left;'>Kerala Ayurvedic Protocol (Karmanya)</th></tr></thead><tbody><tr style='border-bottom:1px solid #eee;'><td style='padding:12px;'><strong>Weight Lost</strong></td><td style='padding:12px;'>Mainly water weight and lean muscle mass</td><td style='padding:12px;'>True visceral and subcutaneous Meda Dhatu (fat)</td></tr><tr style='border-bottom:1px solid #eee;'><td style='padding:12px;'><strong>Metabolic Impact</strong></td><td style='padding:12px;'>Suppresses thyroid & BMR; leads to rebound obesity</td><td style='padding:12px;'>Ignites cellular Agni; permanently enhances digestion</td></tr><tr style='border-bottom:1px solid #eee;'><td style='padding:12px;'><strong>Skin & Lymphatics</strong></td><td style='padding:12px;'>Loose, saggy skin and persistent cellulite</td><td style='padding:12px;'>Udvartana firms skin tone and boosts lymphatic drainage</td></tr><tr><td style='padding:12px;'><strong>Sustainability</strong></td><td style='padding:12px;'>High dropout; severe nutritional exhaustion</td><td style='padding:12px;'>Healthy 2 to 4 kg/month loss with enhanced daily vitality</td></tr></tbody></table>"
    },
    {
      "heading": "Addressing Hormonal Weight Gain (PCOS and Thyroid Dysfunction)",
      "body": "Many women and men struggle with stubborn abdominal weight that refuses to budge despite rigorous workouts. Through pulse diagnosis (Nadi Pariksha), Dr. Tejasvi Mulik identifies hidden subclinical hypothyroidism or PCOS-induced insulin resistance. By pairing Lekhana (fat-scraping) herbs like Kanchnar Guggulu and Varunadi Kashayam with structured Udvartana sessions, the body clears hormonal channel blockages and shedding weight becomes a natural physiological process."
    }
  ],
  "faqs": [
    {
      "q": "How many sessions of Udvartana are needed to see visible fat loss?",
      "a": "A typical course consists of 7, 14, or 21 daily sessions. Most patients experience significant reductions in inch measurements (especially around the waist and thighs) within the first 7 to 10 sessions as stagnant fluid and subcutaneous fat are mobilized."
    },
    {
      "q": "Is Udvartana painful or rough on the skin?",
      "a": "No. While the upward strokes are applied with firm clinical pressure to generate frictional warmth, the herbal powders are micro-pulverized and soothing. Most patients find the treatment deeply invigorating, leaving their skin radiant, toned, and exceptionally smooth."
    }
  ]
}
"""

marker = '# ─── BLOG POST TEMPLATE ─────────────────────────────────────────────────────────'
if marker in code:
    # Find the closing `]` before marker
    pos_marker = code.find(marker)
    pos_bracket = code.rfind(']', 0, pos_marker)
    code = code[:pos_bracket] + new_articles + code[pos_bracket:]
    print("Injected 3 articles right before closing bracket of articles list!")

with open(blog_gen_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_blog.py successfully updated.")
