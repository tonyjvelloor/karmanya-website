import json

with open('data/conditions.json', 'r') as f:
    conditions = json.load(f)

new_conditions = [
    {
        "id": "diabetes-madhumeha",
        "title": "Ayurvedic Diabetes Treatment",
        "slug": "diabetes-madhumeha",
        "seo": {
          "meta_title": "Ayurvedic Diabetes Treatment in Pune | Non-Surgical Sugar Control",
          "meta_description": "Manage Type-2 Diabetes naturally with authentic Kerala Ayurveda in Pimple Saudagar. Consult our BAMS doctors for metabolic correction and Panchakarma detox."
        },
        "marketing": {
          "hero_eyebrow": "Metabolic Correction \u00b7 Madhumeha",
          "hero_title": "Ayurvedic Treatment for Diabetes",
          "hero_description": "A holistic, natural approach to managing blood sugar levels, insulin resistance, and diabetic neuropathy using classical Kerala Panchakarma and herbal formulations.",
          "image_url": "/images/protocols/protocol-metabolic.webp"
        },
        "clinical": {
          "ayurvedic_perspective": "In Ayurveda, Diabetes Mellitus (specifically Type-2) correlates with 'Madhumeha', a metabolic disease resulting from Agnimandya (impaired digestion) and Kapha-Pitta dosha imbalance. Poor diet and sedentary lifestyle lead to the accumulation of Ama (toxins) which impairs the function of the pancreas and cellular insulin sensitivity.",
          "assessment_process": "Our BAMS physicians conduct a detailed Nadi Pariksha, assess your Prakriti, review your HbA1c and fasting sugar levels, and evaluate peripheral nerve function (for neuropathy).",
          "related_treatments": ["panchakarma", "udvartana", "abhyangam"],
          "approach": "We focus on Deepana-Pachana (correcting digestion), Shodhana (Panchakarma detoxification like Virechana to expel morbid doshas), and Rasayana (rejuvenating tissues to prevent diabetic complications)."
        },
        "safety": {
          "disclaimer": "Ayurvedic treatment aims at metabolic correction and should be integrated safely under medical supervision, alongside routine blood sugar monitoring.",
          "emergency_rule": "Severe hyperglycemic episodes require immediate emergency allopathic care."
        }
    },
    {
        "id": "hypertension-high-bp",
        "title": "Ayurvedic Hypertension Treatment",
        "slug": "hypertension-high-bp",
        "seo": {
          "meta_title": "Ayurvedic Treatment for High Blood Pressure in Pune",
          "meta_description": "Naturally lower high blood pressure (Hypertension) with Shirodhara and classical Ayurvedic medicine in Pune. Consult our expert physicians today."
        },
        "marketing": {
          "hero_eyebrow": "Cardiovascular Health \u00b7 Stress Management",
          "hero_title": "Ayurvedic Treatment for Hypertension",
          "hero_description": "Manage high blood pressure naturally through stress-relieving therapies like Shirodhara, dietary correction, and potent Ayurvedic cardiac tonics.",
          "image_url": "/images/protocols/protocol-shirodhara.webp"
        },
        "clinical": {
          "ayurvedic_perspective": "Hypertension (Rakta Gata Vata) is viewed as a systemic imbalance where aggravated Vata and Pitta doshas affect the Rakta Dhatu (blood) and cardiovascular channels (Srotas). Chronic stress, excess sodium, and a sedentary lifestyle cause arterial stiffness and nervous system overactivation.",
          "assessment_process": "Diagnosis includes pulse reading (Nadi Pariksha) to identify the specific doshic imbalance driving the blood pressure spikes, along with a review of your current medication.",
          "related_treatments": ["shirodhara", "panchakarma", "nadi-pariksha"],
          "approach": "Our protocol involves Medhya Rasayanas (nervine tonics) to calm the nervous system, Shirodhara to rapidly lower cortisol and stress, and Virechana to cleanse the Pitta dosha from the blood."
        },
        "safety": {
          "disclaimer": "Do not stop your prescribed anti-hypertensive medications abruptly without consulting your primary cardiologist.",
          "emergency_rule": "Hypertensive crises with chest pain or vision changes require immediate emergency medical attention."
        }
    },
    {
        "id": "obesity-weight-loss",
        "title": "Ayurvedic Obesity & Weight Loss",
        "slug": "obesity-weight-loss",
        "seo": {
          "meta_title": "Ayurvedic Weight Loss & Obesity Treatment in Pune",
          "meta_description": "Struggling with obesity? Discover Udvartana (dry powder massage) and Panchakarma detox for natural, sustainable weight loss at Karmanya Ayurveda Pune."
        },
        "marketing": {
          "hero_eyebrow": "Sthaulya \u00b7 Sustainable Weight Management",
          "hero_title": "Ayurvedic Treatment for Obesity",
          "hero_description": "Sustainably burn stubborn fat and correct your metabolism with authentic Udvartana therapies and physician-led Ayurvedic dietary planning.",
          "image_url": "/images/protocols/protocol-udvartana.webp"
        },
        "clinical": {
          "ayurvedic_perspective": "Obesity (Sthaulya) is a condition of excess Kapha dosha and Meda Dhatu (fat tissue). It is fundamentally a metabolic disorder caused by low digestive fire (Jatharagni) at the tissue level, converting nutrients into Ama (toxins) and excess fat rather than energy.",
          "assessment_process": "We evaluate your BMI, visceral fat patterns, metabolic rate, and underlying hormonal issues (like hypothyroidism or PCOS) through comprehensive Nadi Pariksha.",
          "related_treatments": ["udvartana", "panchakarma", "kerala-chikitsa"],
          "approach": "The core therapy is Udvartana—a vigorous deep-tissue massage using medicated herbal powders that creates friction, breaks down subcutaneous fat, and stimulates lymphatic drainage. This is paired with internal fat-scraping (Lekhana) herbs and Virechana detox."
        },
        "safety": {
          "disclaimer": "Ayurvedic weight loss is gradual and sustainable, focusing on metabolic health rather than rapid, unhealthy fat depletion.",
          "emergency_rule": "Seek standard medical care for acute complications related to severe morbid obesity."
        }
    }
]

# Avoid duplicates
existing_ids = [c['id'] for c in conditions]
for nc in new_conditions:
    if nc['id'] not in existing_ids:
        conditions.append(nc)

with open('data/conditions.json', 'w') as f:
    json.dump(conditions, f, indent=2)

print("Added Diabetes, Hypertension, and Obesity conditions!")
