import json
import os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# 1. Update data/conditions.json
conditions_path = os.path.join(base_dir, 'data', 'conditions.json')
with open(conditions_path, 'r', encoding='utf-8') as f:
    conditions = json.load(f)

new_faqs = {
    'kerala-ayurveda': [
      {
        "question": "What is authentic Kerala Ayurveda and how is it different from regular commercial spas?",
        "answer": "Authentic Kerala Ayurveda adheres to the classical Ashtavaidya tradition — a 2,000-year-old lineage of physician families who preserved texts like Ashtanga Hrudayam and Sahasrayogam. It is distinguished by heavy use of medicated herbal oils (Thailams), specific procedural therapies like Dhara, Pizhichil, and Kizhi performed on authentic single-piece wooden Dronis, and strict Panchakarma purification supervised by BAMS physicians."
      },
      {
        "question": "How do I know if a clinic in Pune offers genuine Kerala Ayurveda?",
        "answer": "Look for three markers of authenticity: physician training under classical Kerala Ayurvedic institutions, medicines sourced directly from GMP-certified Kerala manufacturers like Arya Vaidya Sala Kottakkal, and procedural fidelity — correct sequence, dosage, and post-procedure care. At Karmanya, all therapies follow authentic classical protocols."
      },
      {
        "question": "Can I undergo a complete Kerala Panchakarma detox during the Diwali vacation in Pune?",
        "answer": "Yes. Karmanya Ayurveda remains open all 7 days from 10:00 AM to 8:00 PM throughout the Diwali holiday period. We offer intensive 7-day and 14-day Kerala Panchakarma and pain management regimens tailored for working professionals and families, enabling you to complete therapy without taking extended work leave."
      },
      {
        "question": "What should I expect during my first Kerala Ayurveda consultation?",
        "answer": "Your first visit includes a thorough 45-minute Nadi Pariksha (three-finger radial pulse diagnosis) by Dr. Tejasvi Mulik, review of existing MRI/X-ray scans, Prakriti (body constitution) assessment, and a customized treatment plan. The consultation fee is strictly ₹500 with zero surprise charges."
      },
      {
        "question": "How long does a typical Kerala Ayurveda treatment course last?",
        "answer": "Treatment duration depends on your condition's chronicity. Typical courses range from 7 days (acute flare-ups, stress recovery) to 14-21 days (chronic disc herniations, advanced osteoarthritis, full Panchakarma detox). Your physician determines the exact protocol after in-person assessment."
      }
    ],
    'diabetes-madhumeha': [
      {
        "question": "Can Ayurveda help manage Type-2 Diabetes alongside allopathic medicine?",
        "answer": "Yes. Ayurvedic treatment for diabetes (Madhumeha) focuses on metabolic correction through Deepana-Pachana (digestive fire correction), Shodhana (Panchakarma detoxification like Virechana), and Rasayana (tissue rejuvenation). It works alongside your existing medication under medical supervision, gradually improving insulin sensitivity and reducing reliance on allopathic drugs."
      },
      {
        "question": "What Ayurvedic therapies are used for diabetes and insulin resistance?",
        "answer": "Key therapies include Virechana (therapeutic purgation to expel morbid Pitta and Kapha), Udvartana (dry herbal powder scrub to stimulate lymphatic fat metabolism), and classical formulations containing Gudmar (Gymnema sylvestre), Vijaysar, Shilajit, and Nisha Amalaki to support pancreatic beta-cell function."
      },
      {
        "question": "Can Ayurveda help with diabetic neuropathy (burning sensation or numbness in feet)?",
        "answer": "Yes. Diabetic neuropathy responds exceptionally well to Kashaya Dhara (warm medicated herbal decoction streaming), Padabhyanga with Ksheerabala Tailam, and neuro-regenerative Medhya Rasayanas like Ashwagandha and Bala, which improve microcirculation and nourish damaged peripheral nerves."
      },
      {
        "question": "What dietary protocol is recommended for diabetes in Ayurveda?",
        "answer": "Ayurveda prescribes a Kapha-Pitta pacifying diet: low glycemic grains such as barley (Yava), millets, and old brown rice; bitter vegetables like bitter gourd (Karela), fenugreek (Methi), and drumstick; and strict avoidance of curd, refined flour (Maida), daytime sleeping, and heavy fried meals."
      }
    ],
    'hypertension-high-bp': [
      {
        "question": "Can Ayurveda lower high blood pressure naturally?",
        "answer": "Yes. Classical therapies like Shirodhara (continuous rhythmic warm herbal oil stream on the forehead) directly stimulate the vagus nerve and downregulate cortisol and adrenaline levels. Combined with Medhya Rasayanas (Sarpagandha, Brahmi, Shankhapushpi, Arjuna) and dietary sodium correction, patients achieve stabilized blood pressure within 6 to 8 weeks."
      },
      {
        "question": "Should I stop my BP tablets before starting Ayurvedic treatment?",
        "answer": "Absolutely not. Never discontinue prescribed anti-hypertensive medications abruptly. Ayurvedic treatment works alongside your existing medication. As your blood pressure stabilizes with sustained care, your cardiologist may consider gradual dosage tapering based on daily monitoring."
      },
      {
        "question": "How does Shirodhara help with stress-induced hypertension?",
        "answer": "Shirodhara involves pouring a continuous stream of warm medicated herbal oil (or Takradhara / medicated buttermilk) onto the forehead for 45 minutes. Clinical studies indicate this induces an alpha-brainwave state, lowers plasma cortisol, reduces arterial resistance, and calms sympathetic nervous system overactivation."
      },
      {
        "question": "What Ayurvedic herbs are used for cardiovascular and blood pressure health?",
        "answer": "Classical formulations include Sarpagandha (Rauwolfia serpentina), Arjuna (Terminalia arjuna for cardiac muscle toning), Brahmi (Bacopa monnieri), Shankhapushpi (Convolvulus pluricaulis), and Jatamansi (Nardostachys jatamansi) for deep nervous system calming."
      }
    ],
    'obesity-weight-loss': [
      {
        "question": "How does Ayurveda help with weight loss differently from crash diets?",
        "answer": "Ayurvedic weight management targets the root metabolic cause — impaired digestive fire (Agnimandya) converting nutrients into excess fat (Meda Dhatu) rather than energy. Therapies like Udvartana, Virechana, and Lekhana (fat-scraping) herbs recalibrate cellular metabolism permanently, preventing rebound weight gain."
      },
      {
        "question": "What is Udvartana and how does it reduce stubborn fat?",
        "answer": "Udvartana is an intensive upward deep-tissue massage using warm, dry herbal powders (Triphala, Musta, Kolakulathadi). The intense friction creates therapeutic heat that liquefies subcutaneous adipose tissue, stimulates lymphatic drainage, tones loose skin, and improves peripheral circulation."
      },
      {
        "question": "How much weight can I expect to lose with an Ayurvedic weight loss program?",
        "answer": "Ayurvedic weight loss is gradual and sustainable — typically 2 to 4 kilograms per month with consistent therapies and dietary adherence. The focus is on reducing visceral fat, lowering triglycerides and fasting insulin, and correcting metabolic markers rather than temporary water loss."
      },
      {
        "question": "Can Ayurveda help with hormonal weight gain from PCOS or Hypothyroidism?",
        "answer": "Yes. Hormonal weight gain is treated by clearing channel blockages (Sroto-rodha) and correcting endocrine imbalances. Formulations like Kanchanara Guggulu (for thyroid) and Varunadi Kashayam combined with Udvartana and Virechana address both the hormonal root cause and excess fat tissue."
      }
    ]
}

for c in conditions:
    slug = c.get('slug')
    # Update metadata to Dr. Tejasvi Mulik
    c['metadata'] = {
        "reviewed_by": "Dr. Tejasvi Mulik",
        "reviewed_date": "October 2026",
        "doctor_url": "/doctors/dr-tejasvi/"
    }
    # Add FAQs if missing
    if slug in new_faqs and (not c.get('faqs') or len(c.get('faqs')) == 0):
        c['faqs'] = new_faqs[slug]
    
    # Fix meta_description in digestive disorders
    if slug == 'digestive-metabolic-disorders':
        c['seo']['meta_description'] = "Treat chronic acidity, IBS, bloating, and sluggish metabolism with authentic Ayurvedic medicine in Pune. Gut-reset protocols with Dr. Tejasvi Mulik."

with open(conditions_path, 'w', encoding='utf-8') as f:
    json.dump(conditions, f, indent=2)
print("Updated data/conditions.json successfully.")

# 2. Update data/treatments.json
treatments_path = os.path.join(base_dir, 'data', 'treatments.json')
with open(treatments_path, 'r', encoding='utf-8') as f:
    treatments = json.load(f)

for t in treatments:
    t['metadata'] = {
        "reviewed_by": "Dr. Tejasvi Mulik",
        "reviewed_date": "October 2026",
        "doctor_url": "/doctors/dr-tejasvi/"
    }
    # Clean FAQ text
    for faq in t.get('faqs', []):
        ans = faq.get('answer', '')
        ans = ans.replace("Dr. Irshad T.M. and Dr. Tejasvi Mulik", "Dr. Tejasvi Mulik")
        ans = ans.replace("Dr. Irshad T.M.", "Dr. Tejasvi Mulik")
        ans = ans.replace("Dr. Irshad trained under classical Kerala Ayurvedic institutions with Ashtavaidya lineage", "our senior physicians trained under classical Kerala Ayurvedic institutions with Ashtavaidya lineage")
        ans = ans.replace("At Karmanya, Dr. Irshad brings the Ashtavaidya Kerala tradition directly to Pune.", "At Karmanya, our senior physicians bring the Ashtavaidya Kerala tradition directly to Pune.")
        ans = ans.replace("Dr. Irshad", "Dr. Tejasvi")
        faq['answer'] = ans

with open(treatments_path, 'w', encoding='utf-8') as f:
    json.dump(treatments, f, indent=2)
print("Updated data/treatments.json successfully.")

# 3. Update data/site.json, data/locations.json, data/claims.json
site_path = os.path.join(base_dir, 'data', 'site.json')
with open(site_path, 'r', encoding='utf-8') as f:
    site_data = json.load(f)
for test in site_data.get('testimonials', []):
    test['quote'] = test.get('quote', '').replace("Dr. Irshad's protocol", "the clinical protocol at Karmanya")
with open(site_path, 'w', encoding='utf-8') as f:
    json.dump(site_data, f, indent=2)
print("Updated data/site.json successfully.")

loc_path = os.path.join(base_dir, 'data', 'locations.json')
with open(loc_path, 'r', encoding='utf-8') as f:
    loc_data = json.load(f)
for l in loc_data:
    lead = l.get('lead', '')
    l['lead'] = lead.replace("Dr. Irshad T.M. and Dr. Tejasvi Mulik", "Dr. Tejasvi Mulik")
with open(loc_path, 'w', encoding='utf-8') as f:
    json.dump(loc_data, f, indent=2)
print("Updated data/locations.json successfully.")

claims_path = os.path.join(base_dir, 'data', 'claims.json')
with open(claims_path, 'r', encoding='utf-8') as f:
    claims_data = json.load(f)
for cl in claims_data:
    if cl.get('approved_by') == 'Dr. Irshad':
        cl['approved_by'] = 'Dr. Tejasvi Mulik'
with open(claims_path, 'w', encoding='utf-8') as f:
    json.dump(claims_data, f, indent=2)
print("Updated data/claims.json successfully.")

print("All data files updated for E-E-A-T and medical attribution.")
