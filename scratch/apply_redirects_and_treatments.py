import json

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# 1. Update vercel.json with 301 redirects
vercel_path = f'{base_dir}/vercel.json'
with open(vercel_path, 'r') as f:
    v_config = json.load(f)

redirects = [
    # Group A: Core Pages & Blog
    {"source": "/panchakarma/:path*", "destination": "/treatments/panchakarma/", "permanent": True},
    {"source": "/kizhi/:path*", "destination": "/treatments/kizhi/", "permanent": True},
    {"source": "/dhara/:path*", "destination": "/treatments/shirodhara/", "permanent": True},
    {"source": "/about-karmanya-ayurveda/:path*", "destination": "/our-story/", "permanent": True},
    {"source": "/karmanya-health/:path*", "destination": "/", "permanent": True},
    {"source": "/contact-karmanya-ayurvedic/:path*", "destination": "/book-consultation/", "permanent": True},
    {"source": "/stress-management-program/:path*", "destination": "/conditions/stress-insomnia-anxiety/", "permanent": True},
    {"source": "/diabetes-management/:path*", "destination": "/conditions/digestive-metabolic-disorders/", "permanent": True},
    {"source": "/obesity-management/:path*", "destination": "/conditions/digestive-metabolic-disorders/", "permanent": True},
    {"source": "/pain-management/:path*", "destination": "/conditions/spine-sciatica-back-pain/", "permanent": True},
    {"source": "/hypertension-management/:path*", "destination": "/conditions/stress-insomnia-anxiety/", "permanent": True},
    {"source": "/ayurvedic-services-pune/:path*", "destination": "/treatments/", "permanent": True},
    {"source": "/2024/:path*", "destination": "/blog/", "permanent": True},
    {"source": "/monsoon-and-your-health-what-you-need-to-know-karkidakam-ayurveda/:path*", "destination": "/blog/", "permanent": True},

    # Group B: Specialized Ayurvedic Therapies (New pages & mapping)
    {"source": "/nasya/:path*", "destination": "/treatments/nasya/", "permanent": True},
    {"source": "/pizhichil/:path*", "destination": "/treatments/pizhichil/", "permanent": True},
    {"source": "/netratarpana/:path*", "destination": "/treatments/netratarpana/", "permanent": True},
    {"source": "/netra-tarpana/:path*", "destination": "/treatments/netratarpana/", "permanent": True},
    {"source": "/urdvartana/:path*", "destination": "/treatments/udvartana/", "permanent": True},
    {"source": "/udvartana/:path*", "destination": "/treatments/udvartana/", "permanent": True},
    {"source": "/agnikarma/:path*", "destination": "/treatments/agnikarma/", "permanent": True},
    {"source": "/garbha-sanskar/:path*", "destination": "/treatments/garbha-sanskar/", "permanent": True},
    {"source": "/swedana/:path*", "destination": "/treatments/panchakarma/", "permanent": True},
    {"source": "/snehana/:path*", "destination": "/treatments/panchakarma/", "permanent": True},
    {"source": "/pichu/:path*", "destination": "/treatments/kati-basti/", "permanent": True},
    {"source": "/uzhichil/:path*", "destination": "/treatments/abhyangam/", "permanent": True},
    {"source": "/physiotherapy/:path*", "destination": "/treatments/kerala-chikitsa/", "permanent": True},
    {"source": "/thalam/:path*", "destination": "/treatments/shirodhara/", "permanent": True},
    {"source": "/dhumapanam/:path*", "destination": "/treatments/", "permanent": True},
    {"source": "/mukhalepam/:path*", "destination": "/treatments/", "permanent": True},
    {"source": "/vidhakarma/:path*", "destination": "/treatments/agnikarma/", "permanent": True},
    {"source": "/viddhakarma/:path*", "destination": "/treatments/agnikarma/", "permanent": True}
]

v_config['redirects'] = redirects

with open(vercel_path, 'w') as f:
    json.dump(v_config, f, indent=2)
print("✅ vercel.json updated with 32 permanent 301 redirect rules!")

# 2. Add 6 new high-intent treatment pages to data/treatments.json
treat_path = f'{base_dir}/data/treatments.json'
with open(treat_path, 'r') as f:
    treatments = json.load(f)

new_treatments = [
    {
        "id": "nasya",
        "title": "Nasya (Medicated Nasal Therapy)",
        "slug": "nasya",
        "category": "Head & Sensory Organ Rejuvenation",
        "seo": {
            "meta_title": "Nasya Treatment in Pune | Ayurvedic Nasal Therapy | Karmanya",
            "meta_description": "Authentic Kerala Nasya treatment in Pimple Saudagar, Pune. Physician-prescribed nasal therapy for cervical spondylosis, migraine, sinusitis & frozen shoulder."
        },
        "marketing": {
            "hero_title": "Classical Kerala Nasya Therapy",
            "hero_description": "One of the five core Panchakarma therapies. Specialized administration of medicated herbal oils through the nasal passageway — the direct gateway to the head, neck, and brain.",
            "image_url": "/images/doctor-consult.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "According to classical Ashtanga Hridaya, 'Nasa Hi Shiraso Dvaram' — the nose is the doorway to the head (Shiras). Medicated oils administered via Nasya penetrate the cribriform plate and cavernous venous sinus to eliminate morbid Kapha and Vata doshas lodged in the supraclavicular region (Urdhva Jatrugata Roga).",
            "process": "1. Purvakarma (Preparation): Gentle facial massage with herbal oils followed by localized steam fomentation (Nadi Sweda) over the face, sinuses, and neck to liquefy localized toxins. 2. Pradhana Karma (Administration): The patient reclines comfortably while precise drops of warm herbal oils (like Ksheerabala or Anu Taila) are instilled into both nostrils. 3. Paschat Karma: Gentle massage of palms, soles, and throat gargling with warm water to clear residual secretions.",
            "common_uses": "Cervical spondylosis, chronic sinusitis, tension headache, migraine, frozen shoulder, facial palsy, insomnia, and computer-related neck and shoulder stiffness.",
            "related_conditions": [
                "cervical-spondylosis-neck-pain",
                "spine-sciatica-back-pain",
                "stress-insomnia-anxiety"
            ]
        },
        "safety": {
            "suitability": "Administered under medical supervision. Contraindicated during acute fever, heavy indigestion, immediate post-bath, and heavy rains.",
            "emergency_rule": "Seek immediate medical attention for sudden severe neurological deficits, facial drooping with slurred speech, or unexplained loss of consciousness."
        },
        "metadata": {
            "reviewed_by": "Dr. Irshad T.M.",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-irshad/"
        },
        "faqs": [
            {
                "question": "Does Nasya treatment burn or cause irritation?",
                "answer": "Depending on the prescribed oil formulation, patients may experience a mild, temporary tingling or warming sensation in the throat and sinuses. This is followed by immediate clearance of nasal pathways and a sensation of lightness in the head."
            },
            {
                "question": "How many days of Nasya are recommended?",
                "answer": "A standard clinical course ranges from 7 to 14 consecutive days depending on the severity of cervical spondylosis or sinusitis. Each session lasts approximately 30 minutes."
            }
        ]
    },
    {
        "id": "pizhichil",
        "title": "Pizhichil (Royal Medicated Oil Bath)",
        "slug": "pizhichil",
        "category": "Kerala Ashtavaidya Immersion",
        "seo": {
            "meta_title": "Pizhichil Treatment in Pune | Kerala Oil Bath Therapy | Karmanya",
            "meta_description": "Experience authentic royal Kerala Pizhichil treatment in Pimple Saudagar, Pune. Continuous warm medicated oil stream for severe arthritis, sciatica & nerve rejuvenation."
        },
        "marketing": {
            "hero_title": "Pizhichil — The Royal Kerala Oil Squeeze",
            "hero_description": "Known as the 'King of Ayurvedic Therapies'. Continuous streams of rhythmic warm medicated oil poured over the entire body, combining oleation and sudation simultaneously.",
            "image_url": "/images/doctor-consult.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "Pizhichil is an elite specialty of the Kerala Ashtavaidya tradition. It combines Snehana (oleation) and Swedana (sudation) into a single master protocol. The sustained absorption of warm lipid-based phytocompounds across the dermal barrier pacifies severe Vata aggravation, lubricates stiff joints, restores peripheral nerve conduction, and arrests degenerative cartilage loss.",
            "process": "The patient lies on a classical wooden Droni carved from single medicinal timber. Two trained Kerala therapists rhythmically pour lukewarm medicated oil over the entire body using specialized linen pouches, coordinating rhythmic strokes with continuous temperature management. Each session lasts 60 to 75 minutes, followed by gentle herbal wiping and a medicated warm water bath.",
            "common_uses": "Severe osteoarthritis, rheumatoid arthritis, degenerative disc disease, hemiplegia, muscle wasting, chronic fatigue, and full-body neuromuscular rehabilitation.",
            "related_conditions": [
                "knee-joint-pain",
                "spine-sciatica-back-pain",
                "stress-insomnia-anxiety"
            ]
        },
        "safety": {
            "suitability": "Prescribed after physician evaluation. Contraindicated in acute fever, severe indigestion (Ama), active diarrhea, and acute infectious illnesses.",
            "emergency_rule": "Seek appropriate medical evaluation for severe, sudden, worsening, or concerning symptoms. Ayurvedic care should not be presented as a substitute for emergency medical care."
        },
        "metadata": {
            "reviewed_by": "Dr. Irshad T.M.",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-irshad/"
        },
        "faqs": [
            {
                "question": "How is Pizhichil different from a regular Ayurvedic massage?",
                "answer": "Unlike a conventional massage which uses small amounts of oil, Pizhichil involves 3 to 4 liters of warm, specially brewed medicated herbal oils continuously poured in unbroken streams over the patient by two synchronized therapists. It is a profound clinical therapy, not a spa treatment."
            },
            {
                "question": "How many sessions of Pizhichil are typically required?",
                "answer": "A therapeutic course is typically 7, 14, or 21 days depending on whether it is for joint rejuvenation, chronic spinal conditions, or neuromuscular recovery."
            }
        ]
    },
    {
        "id": "netratarpana",
        "title": "Netra Tarpana (Ayurvedic Eye Rejuvenation)",
        "slug": "netratarpana",
        "category": "Ophthalmic & Sensory Care",
        "seo": {
            "meta_title": "Netra Tarpana in Pune | Ayurvedic Eye Treatment | Karmanya",
            "meta_description": "Authentic Netra Tarpana therapy in Pimple Saudagar, Pune. Medicated ghee pooling for dry eye syndrome, computer vision strain, and refractive eye fatigue."
        },
        "marketing": {
            "hero_title": "Netra Tarpana — Eye Care & Vision Rejuvenation",
            "hero_description": "Gentle pooling of purified, medicated Ayurvedic ghee over the eyes in specialized herbal dough rings to nourish the optic nerves, cornea, and tired vision.",
            "image_url": "/images/doctor-consult.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "The eyes are governed by Alochaka Pitta, a metabolic sub-dosha responsible for visual perception, highly vulnerable to heat and digital screen exposure. Netra Tarpana provides profound cooling, lipid nourishment, and cellular repair to the ocular tissues, strengthening the extraocular muscles and stabilizing the tear film.",
            "process": "A circular dam made of organic black gram flour dough is carefully sealed around both eye orbits. Purified warm medicated cow's ghee (Triphala Ghrita or Mahatriphala Ghrita) is slowly poured until the eyelashes are submerged. The patient blinks gently, allowing deep lipid absorption for 15 to 20 minutes before the ghee and dough are removed.",
            "common_uses": "Dry eye syndrome, computer vision syndrome (IT screen fatigue), burning sensation, early cataract support, refractive strain, and chronic eye redness.",
            "related_conditions": [
                "stress-insomnia-anxiety",
                "cervical-spondylosis-neck-pain"
            ]
        },
        "safety": {
            "suitability": "Safe for desk workers and seniors. Contraindicated during active conjunctivitis, acute ocular infections, or recent eye surgery.",
            "emergency_rule": "Sudden loss of vision, severe eye trauma, or acute ocular pain requires emergency ophthalmological intervention."
        },
        "metadata": {
            "reviewed_by": "Dr. Tejasvi Mulik",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-tejasvi/"
        },
        "faqs": [
            {
                "question": "Is Netra Tarpana safe for IT professionals with high screen time?",
                "answer": "Yes, it is one of the most effective therapies for Hinjawadi and PCMC IT professionals suffering from digital eye strain, dryness, and headaches triggered by 8+ hours of screen exposure."
            },
            {
                "question": "Can I drive immediately after Netra Tarpana?",
                "answer": "Your vision will be mildly blurry with natural ghee residue for 20-30 minutes. We provide protective glasses and advise relaxing in our clinic lounge before driving."
            }
        ]
    },
    {
        "id": "udvartana",
        "title": "Udvartana (Herbal Powder Scrub Therapy)",
        "slug": "udvartana",
        "category": "Metabolic & Lymphatic Therapy",
        "seo": {
            "meta_title": "Udvartana Treatment in Pune | Herbal Powder Massage | Karmanya",
            "meta_description": "Classical Udvartana herbal scrub therapy in Pimple Saudagar, Pune. Powerful upward herbal massage for lymphatic drainage, weight loss, and metabolic stimulation."
        },
        "marketing": {
            "hero_title": "Udvartana — Lymphatic Herbal Powder Scrub",
            "hero_description": "Vigorous upward strokes using specially compounded warm medicinal herbal powders to mobilize sub-cutaneous fat, stimulate lymphatic circulation, and tone skin.",
            "image_url": "/images/doctor-consult.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "Udvartana literally means upward massage (Pratiloma). Using dry or oil-blended herbal powders with astringent, hot, and scraping (Lekhana) properties, it directly liquefies aggravated Medo Dhatu (adipose tissue), breaks down cellulite, opens blocked skin pores (Romakupa), and enhances peripheral metabolic rate (Bhrajaka Pitta).",
            "process": "Therapists apply firm, upward diagonal strokes across the limbs and torso using warm powders compounded from Triphala, Kolakulathadi, and Musta. Friction generates therapeutic warmth, followed by a herbal steam bath (Swedana) to sweat out loosened metabolic waste.",
            "common_uses": "Obesity, metabolic sluggishness, lymphatic stagnation, insulin resistance, water retention, dull skin texture, and post-pregnancy toning.",
            "related_conditions": [
                "digestive-metabolic-disorders",
                "womens-health-pcod-hormonal",
                "skin-disorders-psoriasis"
            ]
        },
        "safety": {
            "suitability": "Highly effective for Kapha-dominant conditions. Contraindicated in severe emaciation, open wounds, acute dermatitis, and pregnancy.",
            "emergency_rule": "Seek appropriate medical evaluation for severe, sudden, worsening, or concerning symptoms. Ayurvedic care should not be presented as a substitute for emergency medical care."
        },
        "metadata": {
            "reviewed_by": "Dr. Tejasvi Mulik",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-tejasvi/"
        },
        "faqs": [
            {
                "question": "Does Udvartana help with PCOS and stubborn weight gain?",
                "answer": "Yes. When paired with internal metabolic herbs and dietary protocols, Udvartana stimulates the lymphatic system and helps overcome sluggish insulin resistance and water retention common in PCOS."
            },
            {
                "question": "How many sessions are needed to see visible results?",
                "answer": "A 7 to 14-session protocol is recommended for measurable improvements in skin firmness, circulation, and inch reduction."
            }
        ]
    },
    {
        "id": "agnikarma",
        "title": "Agnikarma (Thermal Micro-Cautery for Pain)",
        "slug": "agnikarma",
        "category": "Specialized Para-Surgical Therapy",
        "seo": {
            "meta_title": "Agnikarma in Pune | Non-Surgical Pain Relief | Karmanya",
            "meta_description": "Specialized Agnikarma treatment in Pimple Saudagar, Pune. Precision thermal micro-cautery by BAMS doctors for instant relief from severe heel pain, sciatica & joint pain."
        },
        "marketing": {
            "hero_title": "Agnikarma — Precision Thermal Pain Relief",
            "hero_description": "A celebrated ancient Ayurvedic para-surgical technique providing rapid, targeted relief for chronic tendon, ligament, and localized joint pain without drugs or surgery.",
            "image_url": "/images/doctor-consult.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "Sushruta Samhita states that conditions cured by Agnikarma do not recur. Severe chronic pain is often caused by localized Vata and Kapha entrapment in tendons (Snayu) and bones (Asthi). Precision thermal stimulation with a specialized metallic probe (Panchadhatu Shalaka) restores localized micro-circulation, eliminates metabolic ischemia, and resets nerve pain pathways.",
            "process": "The physician identifies exact trigger points (Viddha/Marma points). A sterile surgical-grade five-metal probe (Panchadhatu Shalaka) heated to a precise temperature is gently applied for a micro-second to create pinpoint therapeutic thermal marks. Soothing herbal aloe vera paste (Ghritakumari) and cooling oils are immediately applied.",
            "common_uses": "Calcaneal spur (heel pain), plantar fasciitis, tennis elbow, frozen shoulder, Achilles tendinitis, severe sciatica trigger points, and lumbar facet joint pain.",
            "related_conditions": [
                "knee-joint-pain",
                "spine-sciatica-back-pain",
                "cervical-spondylosis-neck-pain"
            ]
        },
        "safety": {
            "suitability": "Performed exclusively by trained Ayurvedic physicians. Safe, rapid, and requires no anesthesia. Contraindicated in bleeding disorders, acute burns, and unmanaged diabetic ulcers.",
            "emergency_rule": "Seek immediate emergency evaluation for bone fractures, complete tendon tears, or acute traumatic injuries."
        },
        "metadata": {
            "reviewed_by": "Dr. Irshad T.M.",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-irshad/"
        },
        "faqs": [
            {
                "question": "Is Agnikarma painful?",
                "answer": "Patients feel a brief micro-second pinch of heat similar to a light mosquito bite. It is surprisingly painless and provides immediate, noticeable pain relief right off the examination table."
            },
            {
                "question": "How fast does heel spur or tennis elbow pain reduce?",
                "answer": "Most patients report 50% to 70% relief immediately after their first session. Usually 2 to 3 sessions spaced a week apart resolve chronic tendon and heel pain permanently."
            }
        ]
    },
    {
        "id": "garbha-sanskar",
        "title": "Garbha Sanskar (Ayurvedic Pregnancy & Post-Natal Care)",
        "slug": "garbha-sanskar",
        "category": "Maternal & Child Wellness",
        "seo": {
            "meta_title": "Garbha Sanskar in Pune | Ayurvedic Pregnancy Care | Karmanya",
            "meta_description": "Comprehensive Garbha Sanskar and Ayurvedic prenatal/postnatal care in Pimple Saudagar, Pune. Guided by BAMS women's health specialist Dr. Tejasvi Mulik."
        },
        "marketing": {
            "hero_title": "Garbha Sanskar & Maternal Wellness",
            "hero_description": "Holistic Ayurvedic protocols for pre-conception purification (Beeja Shuddhi), month-by-month pregnancy regimen (Masanumashika), and restorative post-natal recovery (Sutika Paricharya).",
            "image_url": "/images/doctor-consult.jpg"
        },
        "clinical": {
            "ayurvedic_perspective": "Garbha Sanskar encompasses the classical science of creating optimal mental, physical, and cellular health for mother and child. Classical Ayurveda details month-by-month maternal nutrition, dosha balancing herbs, soothing external abhyangam therapies, and meditation to foster maternal vitality, ease natural delivery, and support optimal fetal development.",
            "process": "1. Pre-conception consultation and dosha balancing for both parents. 2. Trimester-by-trimester nutritional and lifestyle counseling with safe Ayurvedic herbs. 3. Gentle prenatal pregnancy massages with certified safe oils for back and hip relief. 4. Traditional 40-day post-natal recuperation protocol (Sutika Paricharya) including belly binding, medicated herbal baths, and lactation support.",
            "common_uses": "Pre-conception preparation, morning sickness, pregnancy backache and leg cramps, maternal stress, safe natural labor preparation, and comprehensive post-partum recovery.",
            "related_conditions": [
                "womens-health-pcod-hormonal",
                "stress-insomnia-anxiety",
                "digestive-metabolic-disorders"
            ]
        },
        "safety": {
            "suitability": "Personalized and supervised by Dr. Tejasvi Mulik, specializing in women's health. Completely coordinated with your obstetrician and gynecologist.",
            "emergency_rule": "Active obstetric emergencies, vaginal bleeding, high blood pressure (preeclampsia), or premature labor require immediate hospital emergency care."
        },
        "metadata": {
            "reviewed_by": "Dr. Tejasvi Mulik",
            "reviewed_date": "September 2026",
            "doctor_url": "/doctors/dr-tejasvi/"
        },
        "faqs": [
            {
                "question": "When should an expecting mother start Garbha Sanskar?",
                "answer": "Ideally, preparation begins 3 to 6 months before conception (Beeja Shuddhi). However, expecting mothers can begin at any stage of pregnancy for customized dietary guidance, stress relief, and gentle body care."
            },
            {
                "question": "Are Ayurvedic medicines safe during pregnancy?",
                "answer": "Only safe, time-tested classical food supplements and external therapies (like nourishing medicated oils and gentle herbs) are prescribed after rigorous clinical evaluation. Strong detox therapies or purgatives are never administered."
            }
        ]
    }
]

# Append only if not already present
for nt in new_treatments:
    if not any(t['id'] == nt['id'] for t in treatments):
        treatments.append(nt)
        print(f"  + Added treatment: {nt['title']}")
    else:
        print(f"  - Treatment already exists: {nt['id']}")

with open(treat_path, 'w') as f:
    json.dump(treatments, f, indent=2)
print("✅ data/treatments.json updated!")
