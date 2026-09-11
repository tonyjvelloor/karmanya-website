import json
import os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# 1. Update data/treatments.json
with open(os.path.join(base_dir, 'data', 'treatments.json'), 'r') as f:
    treatments = json.load(f)

# A. Add Mukhalepam if not present
has_mukhalepam = any(t['id'] == 'mukhalepam' for t in treatments)
if not has_mukhalepam:
    mukhalepam_data = {
        "id": "mukhalepam",
        "title": "Mukhalepam (Ayurvedic Herbal Facial & Skin Therapy)",
        "slug": "mukhalepam",
        "category": "Classical Dermatology & Natural Aesthetics",
        "seo": {
            "meta_title": "Mukhalepam Treatment in Pune | Ayurvedic Herbal Facial | Karmanya",
            "meta_description": "Physician-guided Mukhalepam treatment in Pimple Saudagar, Pune. Classical Ayurvedic herbal face packs for melasma, pigmentation, acne scars, and skin radiance."
        },
        "marketing": {
            "hero_title": "Mukhalepam Herbal Face Therapy",
            "hero_description": "Classical Ayurvedic facial therapy using customized micro-ground herbal pastes to treat hyperpigmentation, melasma, acne marks, and restore natural cellular skin radiance.",
            "image_url": "/images/hero-treatment.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "In classical Ayurveda, facial skin health is governed by 'Bhrajaka Pitta' (the sub-dosha responsible for skin luster, complexion, and temperature) and 'Rasa Dhatu'. When toxic heat (Pitta) and metabolic impurities (Ama) accumulate in the micro-channels (Srotas) of the facial skin, it manifests as hyperpigmentation, dark patches (Vyanga / Melasma), acne (Yuvanapidaka), and premature skin dullness. Mukhalepam is the authentic classical therapeutic procedure of applying targeted, freshly prepared herbal pastes (Lepas) formulated with potent Varnya (complexion-enhancing) and Raktaprasadana (blood-purifying) herbs such as Lodhra, Manjistha, Raktachandana, Haridra, Sariva, and saffron.",
            "process": "1. Consultation & Skin Prakriti Assessment: Dr. Tejasvi Mulik diagnoses whether your skin condition is Pitta-dominant (burning, redness, inflammatory melasma) or Kapha-dominant (cystic acne, oily congestion).\n2. Gentle Cleansing: The face is prepared using fresh warm herbal decoctions (Kashayam) to open skin pores.\n3. Mukha Abhyanga: A gentle facial massage using classical Kumkumadi Taila or Nalpamaradi Taila to stimulate facial Marma points and improve micro-capillary blood circulation.\n4. Herbal Lepam Application: Freshly pounded herbs mixed with pure goat's milk, aloe vera, or rose water are applied evenly across the face to a precise classical thickness (one-fourth of an inch).\n5. Therapeutic Retention: The paste is retained until semi-dry (before it dries completely or cracks, to prevent Vata aggravation).\n6. Removal & Toning: Gently wiped with warm herbal water and finished with a calming botanical mist.",
            "common_uses": "Melasma (chloasma), stubborn facial pigmentation, dark spots, post-inflammatory acne erythema, fine lines, dark under-eye circles, and pre-bridal skin rejuvenation without synthetic chemicals.",
            "related_conditions": [
                "skin-disorders-psoriasis",
                "womens-health-pcod-hormonal"
            ]
        },
        "safety": {
            "suitability": "Safe, non-invasive, and suitable for all skin types including sensitive skin. Formulated strictly with 100% natural medical-grade herbs without bleaching agents, steroids, or synthetic fragrances. Not performed over active bleeding lesions or open skin infections.",
            "emergency_rule": "Seek appropriate medical evaluation for severe, sudden, worsening, or concerning symptoms. Ayurvedic care should not be presented as a substitute for emergency medical care."
        },
        "metadata": {
            "reviewed_by": "Dr. Tejasvi Mulik",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-tejasvi/"
        },
        "faqs": [
            {
                "question": "What is Mukhalepam and how does it differ from a standard cosmetic facial?",
                "answer": "A standard beauty salon facial typically uses cosmetic chemical peels, synthetic bleaches, and mechanical scrubbing that offer superficial, short-lived brightness but can thin the epidermis or trigger rebound pigmentation. Mukhalepam is a medical Ayurvedic therapy prescribed by an Ayurvedic physician. It uses classical pharmacopeial herbs (Lodhra, Manjistha, Sandalwood, Kumkumadi) that penetrate deep into the subdermal micro-channels, cooling Bhrajaka Pitta and permanently clearing the root cellular cause of melanin accumulation."
            },
            {
                "question": "How many sessions of Mukhalepam are needed for melasma and pigmentation?",
                "answer": "For mild sun tanning or post-acne blemishes, a course of 5 to 7 sessions scheduled twice weekly produces visible rejuvenation. For deep-seated dermal melasma (Vyanga) or hormonal pigmentation, a comprehensive 14 to 21 session protocol combined with internal blood-purifying Ayurvedic medications (like Khadirarishta and Sarivadyasava) is recommended."
            },
            {
                "question": "Is Mukhalepam safe for sensitive and acne-prone skin?",
                "answer": "Yes. Because every Lepam paste is freshly blended in-clinic to match your specific Dosha, the physician selects anti-inflammatory, soothing herbs like Neem, Chandana, and Lodhra for reactive acne-prone skin, avoiding heating ingredients entirely."
            },
            {
                "question": "What precautions should be taken after a Mukhalepam treatment?",
                "answer": "Avoid direct harsh sunlight exposure immediately after therapy. Do not wash your face with harsh synthetic soaps or hot water for at least 6 hours following treatment to allow the active herbal phytochemicals to fully absorb into the cutaneous tissue."
            }
        ]
    }
    treatments.append(mukhalepam_data)

# Update existing treatments with rich sub-therapy relevance
for t in treatments:
    if t['id'] == 'panchakarma':
        t['clinical']['ayurvedic_perspective'] += " Crucially, classical Panchakarma cannot take place without the preparatory twin pillars of Snehana (Oleation) and Swedana (Sudation/Medicated Steam). Snehana saturates the cellular matrix to loosen crystallized metabolic wastes (Ama), while Swedana dilates the body's channels (Srotas), liquefying toxins and directing them into the digestive tract for expulsion."
        t['clinical']['process'] += "\n\nDetailed Preparatory Protocols:\n• Snehana (Oleation): Snehapana (daily morning ingestion of medicated cow's ghee in increasing dosages such as Guggulu Tikta Ghrita) followed by whole-body therapeutic oil massage (Bahya Snehana).\n• Swedana (Medicated Herbal Steam): Bashpa Sweda (enclosed cedarwood steam box infused with boiling Dashamoola decoctions) and Nadi Sweda (targeted tube steam for stiff joints and spine) to induce therapeutic sweating without straining the heart."
        t['faqs'].extend([
            {
                "question": "What is Swedana and why is herbal steam therapy mandatory before Panchakarma?",
                "answer": "Swedana is the classical Ayurvedic process of inducing controlled, therapeutic sweating using herbal steam (Bashpa Sweda) or localized steam jets (Nadi Sweda). After the body has been lubricated with medicated oils (Snehana), Swedana opens the micro-circulatory channels (Srotas), melts viscous cellular toxins (Ama), and moves them towards the alimentary canal. Without adequate Swedana, toxins remain stubbornly trapped in peripheral tissues."
            },
            {
                "question": "What is Snehana (Snehapana) and how does drinking medicated ghee detoxify the body?",
                "answer": "Snehana is internal and external oleation. Internal Snehapana involves consuming pure medicated cow's ghee on an empty stomach for 3 to 7 consecutive days in progressively increasing quantities. Because cell walls are lipid-soluble, medicated ghee penetrates deep intercellular spaces, binds to fat-soluble chemical toxins, and carries them away from vital organs."
            }
        ])
    elif t['id'] == 'kati-basti':
        t['clinical']['ayurvedic_perspective'] += " For acute spinal flare-ups or localized disc bulges where a flour ring cannot be sealed, our physicians administer 'Kati Pichu' (continuous medicated oil pad retention) as a targeted companion therapy to deliver sustained transdermal herbal penetration."
        t['clinical']['process'] += "\n\nKati Pichu (Medicated Oil Pad Retention):\nA thick, sterile folded cotton pad saturated with warm medicated herbal oil (Sahacharadi Taila, Murivenna, or Ksheerabala) is positioned directly over the symptomatic lumbar vertebrae and renewed continuously for 40 minutes. Pichu provides continuous thermal contact, deep muscular relaxation, and rapid decompression of impinged nerve roots."
        t['faqs'].append({
            "question": "What is Kati Pichu and when is it preferred over Kati Basti?",
            "answer": "Kati Pichu is a localized therapeutic compress where folded sterile pads soaked in warm medicated oil are placed continuously over the affected spinal segment. While Kati Basti uses a dough reservoir to pool oil, Kati Pichu is preferred for patients in acute severe pain who cannot tolerate pressure, elderly individuals, or when treating multiple spinal levels simultaneously (such as combined cervical and lumbar spondylosis)."
        })
    elif t['id'] == 'janu-basti':
        t['clinical']['ayurvedic_perspective'] += " In addition to Basti, 'Janu Pichu' (continuous medicated oil pad therapy) is frequently utilized for acute knee joint inflammation, ligament sprains, and Baker's cysts."
        t['faqs'].append({
            "question": "What is Janu Pichu and how does it help knee ligament sprains and joint pain?",
            "answer": "Janu Pichu involves wrapping the knee joint in sterilized cotton compresses saturated with warm anti-inflammatory oils like Murivenna or Sahacharadi. It is particularly effective for acute knee injuries, swollen ligaments, and joint stiffness where firm dough dams are contraindicated."
        })
    elif t['id'] == 'abhyangam':
        t['title'] = "Abhyangam & Uzhichil (Traditional Kerala Body Therapy)"
        t['clinical']['ayurvedic_perspective'] += " In traditional Kerala Ashtavaidya practice, Abhyangam is administered in its most potent clinical form known as 'Uzhichil'. Uzhichil is a rigorous, rhythmic neuromuscular therapy executed across seven classical physical postures (Saptha Krama) targeting the 107 vital energy junctions (Marmas)."
        t['clinical']['process'] += "\n\nTraditional Kerala Uzhichil Protocol:\nThe therapy follows strict directional strokes matching venous blood flow and lymphatic drainage. The physician-directed strokes stimulate the Marmas to release trapped muscle spasms, unblock stagnant Prana (life energy), and calm the central nervous system."
        t['faqs'].append({
            "question": "What is Uzhichil and how is traditional Kerala Uzhichil different from a general massage?",
            "answer": "While a commercial massage offers superficial relaxation, traditional Kerala Uzhichil is a clinical therapeutic protocol practiced by trained Ashtavaidya therapists. It uses physician-selected herbal oils (such as Dhanwantharam or Mahanarayana) applied in 7 classical anatomical postures with precise pressure along the 107 Marma energy junctions to alleviate deep musculoskeletal disorders, improve joint mobility, and relieve nervous exhaustion."
        })
    elif t['id'] == 'shirodhara':
        t['clinical']['ayurvedic_perspective'] += " In complex cases of neurological agitation, severe chronic migraine, or intense insomnia, Shirodhara is combined with 'Thalam'—the classical application of medicated herbal paste retained on the crown of the head."
        t['clinical']['process'] += "\n\nThalam (Medicated Herbal Paste Crown Therapy):\nA cooling, medicated paste made from Kachuradi Churna, Amalaki, or Chandana blended with herbal oils or buttermilk is applied directly over the vertex (Brahmarandhra) within a protective doughnut ring for 30–45 minutes. Thalam directly pacifies cerebral Pitta and Prana Vata, inducing deep mental calmness."
        t['faqs'].append({
            "question": "What is Thalam therapy and how does it relieve chronic migraine, stress, and sleeplessness?",
            "answer": "Thalam is an authentic Kerala therapy where a pool of medicated paste and therapeutic oil is retained on the crown of the head (Brahmarandhra). In Ayurveda, the crown is the master Marma center governing neurological balance. Thalam acts as a thermal heat-sink, absorbing trapped intracranial heat, soothing hyperactive nerve fibers, and dramatically improving sleep architecture when paired with Shirodhara."
        })
    elif t['id'] == 'nasya':
        t['clinical']['ayurvedic_perspective'] += " Authentic Nasya therapy always incorporates 'Dhumapana' (medicated herbal smoke inhalation) as the essential post-nasal protocol to expel residual liquefied Kapha and prevent sinus congestion."
        t['clinical']['process'] += "\n\nDhumapana (Medicated Herbal Inhalation):\nFollowing the instillation of nasal oil drops, the patient inhales therapeutic fumes from a specialized medicated herb stick (Haridradi Varti composed of turmeric, guggulu, and licorice) through the nostrils and exhales through the mouth. This classical step clears residual phlegm from the paranasal sinuses, relieves post-nasal drip, and leaves the airways remarkably open and clear."
        t['faqs'].append({
            "question": "What is Dhumapana and why is medicated smoke inhalation administered after Nasya?",
            "answer": "Dhumapana is the inhalation of medicated herbal fumes generated by burning standardized therapeutic herbs (such as Haridra and licorice). It is the classical concluding step of Nasya. It acts as an astringent and decongestant, ensuring that any residual mucus dislodged by the nasal drops is completely eliminated through the mouth without entering the digestive or bronchial tracts."
        })
    elif t['id'] == 'agnikarma':
        t['title'] = "Agnikarma & Viddhakarma (Instant Pain Relief Therapy)"
        t['clinical']['ayurvedic_perspective'] += " In our clinic, Agnikarma is frequently paired with 'Viddhakarma' (Ayurvedic micro-puncture / dry needling). Viddha-Agni Karma is Ayurveda's most rapid non-surgical pain management protocol for instant decompression of trapped nerves, trigger points, and inflamed ligaments."
        t['clinical']['process'] += "\n\nViddhakarma Micro-Puncture Protocol:\nUsing sterile, specialized micro-needles, the physician performs precise punctures at designated Marma points. This instantly releases localized interstitial pressure and releases trapped static blood (Dushta Rakta). Immediately following Viddhakarma, Agnikarma (thermal transfer) is applied to relax the surrounding spastic muscle fibers and trigger endorphin release."
        t['faqs'].append({
            "question": "What is Viddhakarma and how does Viddha-Agni Karma relieve pain instantly?",
            "answer": "Viddhakarma is an ancient Ayurvedic surgical sub-technique that uses ultra-fine sterile needles at exact anatomical Marma trigger points. It works by releasing localized micro-vascular pressure and unblocking stagnant Prana, offering immediate reduction in acute pain from sciatica, calcaneal heel spurs, frozen shoulder, and tennis elbow. When followed by Agnikarma, it provides both immediate relief and long-term tissue healing."
        })
    elif t['id'] == 'kerala-chikitsa':
        t['clinical']['ayurvedic_perspective'] += " Kerala Chikitsa represents authentic Ayurvedic Physical Rehabilitation and Marma Physiotherapy. It blends classical Ashtavaidya manual therapies with neuromuscular mobilization to rehabilitate degenerative joints and spinal disc lesions naturally."
        t['faqs'].append({
            "question": "Can Ayurvedic Kerala Chikitsa replace or support conventional Physiotherapy for spine and joint recovery?",
            "answer": "Yes. While conventional physiotherapy focuses primarily on mechanical exercises and electrotherapy, Kerala Chikitsa incorporates medicated lipid absorption (Snigdha Chikitsa), deep Marma neuromuscular stimulation, passive spinal traction, and thermal fomentation (Kizhi). This combination simultaneously heals degenerative cartilage, relaxes chronic spasms, and restores joint biomechanics naturally."
        })

with open(os.path.join(base_dir, 'data', 'treatments.json'), 'w') as f:
    json.dump(treatments, f, indent=2)

print('Updated data/treatments.json with Mukhalepam and enriched therapies.')

# 2. Update data/conditions.json
with open(os.path.join(base_dir, 'data', 'conditions.json'), 'r') as f:
    conditions = json.load(f)

for c in conditions:
    if c['id'] == 'spine-sciatica-back-pain':
        c['marketing']['hero_eyebrow'] = "Spine & Pain Management Program · Non-Surgical Care"
        c['marketing']['hero_title'] = "Spine Care & Pain Management Program"
        c['clinical']['ayurvedic_perspective'] += " Karmanya's Comprehensive Spine Care & Pain Management Program integrates Kati Basti, Agnikarma, Viddhakarma, and herbal neuro-regenerative medicines to provide a complete alternative to spinal surgery for slip disc and sciatica."
        c['clinical']['related_treatments'].extend(['agnikarma', 'pizhichil'])
        c['clinical']['related_treatments'] = list(dict.fromkeys(c['clinical']['related_treatments']))
        c['faqs'].append({
            "question": "How does Karmanya's Spine Care & Pain Management Program work?",
            "answer": "Our Spine Care & Pain Management Program is a structured 14 to 21-day clinical protocol designed to relieve sciatica and disc herniation without surgery. It combines three phases: 1. Immediate nerve decompression through Viddhakarma and Kati Basti. 2. Muscular spasm relief and ligament strengthening with Patra Pinda Sweda (Kizhi). 3. Disc rehydration and core stabilization through internal Ayurvedic Rasayana formulations."
        })
    elif c['id'] == 'digestive-metabolic-disorders':
        c['clinical']['ayurvedic_perspective'] += "\n\nMetabolic Syndrome, Diabetes (Madhumeha) & Obesity (Sthaulya):\nIn Ayurveda, both Type-2 Diabetes (Madhumeha) and Obesity (Sthaulya) stem from impaired digestive fire (Mandagni) leading to the accumulation of toxic metabolic fat (Meda Dhatu Dushti) and blocked micro-channels (Sroto-avrodha). Our clinic treats these through deep Agni rekindling, Udvartana (herbal powder scrubbing), and classical botanical formulations."
        c['clinical']['related_treatments'].extend(['udvartana', 'panchakarma'])
        c['clinical']['related_treatments'] = list(dict.fromkeys(c['clinical']['related_treatments']))
        c['faqs'].extend([
            {
                "question": "How does Ayurveda approach Diabetes (Madhumeha) management?",
                "answer": "In Ayurveda, Diabetes (Madhumeha) is classified as a metabolic disorder of Kapha and Meda (fat tissue) resulting from sluggish Agni. Our approach focuses on clearing liver and pancreatic channel blockages using bitter and astringent formulations (such as Vijaysar, Jamun seeds, and Shilajit), restoring cellular insulin sensitivity, preventing diabetic neuropathy, and stabilizing blood glucose without taxing the digestive organs."
            },
            {
                "question": "What is the Ayurvedic protocol for sustainable Obesity and Weight Management?",
                "answer": "Rather than crash dieting, Ayurveda addresses the cellular sluggishness of fat metabolism (Meda Dhatu Agni). We administer Udvartana (vigorous deep-tissue scrubbing with heated herbal powders like Triphala and Kulattha), which stimulates lymphatic drainage, breaks down subcutaneous cellulite, and elevates basal metabolic rate, alongside a personalized Agni-balancing dietary plan."
            }
        ])
    elif c['id'] == 'stress-insomnia-anxiety':
        c['clinical']['ayurvedic_perspective'] += "\n\nStress-Induced Hypertension & Nervous System Overload:\nChronic mental tension aggravates Prana Vata and Sadhaka Pitta, which increases arterial vascular resistance and causes Stress-Induced Hypertension (Rakta Vata). Authentic therapies like Shirodhara, Takradhara, and Thalam systematically reset autonomic nervous tone, lowering heart rate and normalizing arterial blood pressure."
        c['faqs'].append({
            "question": "Can Ayurvedic treatments help reduce Stress-Induced Hypertension and high blood pressure?",
            "answer": "Yes. Clinical studies and classical Ashtavaidya practice demonstrate that therapies like Shirodhara and Takradhara stimulate the pituitary-adrenal axis, reducing elevated cortisol and adrenaline levels. When paired with Medhya Rasayanas (like Brahmi and Shankhapushpi), it relaxes arterial smooth muscles and stabilizes stress-induced hypertension naturally."
        })

with open(os.path.join(base_dir, 'data', 'conditions.json'), 'w') as f:
    json.dump(conditions, f, indent=2)

print('Updated data/conditions.json with Pain Management, Diabetes, Obesity, and Hypertension details.')

# 3. Update vercel.json and build.py legacy redirects so /mukhalepam/ points to /treatments/mukhalepam/
with open(os.path.join(base_dir, 'vercel.json'), 'r') as f:
    vdata = json.load(f)

for r in vdata.get('redirects', []):
    if r.get('source') in ['/mukhalepam', '/mukhalepam/', '/mukhalepam/(.*)']:
        r['destination'] = '/treatments/mukhalepam/'

with open(os.path.join(base_dir, 'vercel.json'), 'w') as f:
    json.dump(vdata, f, indent=2)

with open(os.path.join(base_dir, 'build.py'), 'r') as f:
    bcontent = f.read()

bcontent = bcontent.replace(
    \"'mukhalepam': '/treatments/'\",
    \"'mukhalepam': '/treatments/mukhalepam/'\"
)

with open(os.path.join(base_dir, 'build.py'), 'w') as f:
    f.write(bcontent)

print('Updated vercel.json and build.py for /mukhalepam/ -> /treatments/mukhalepam/')

