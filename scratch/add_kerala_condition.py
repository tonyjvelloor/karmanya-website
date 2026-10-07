import json

with open('data/conditions.json', 'r') as f:
    conditions = json.load(f)

# Check if it already exists
if any(c['id'] == 'kerala-ayurveda' for c in conditions):
    print("Already exists")
else:
    kerala_condition = {
        "id": "kerala-ayurveda",
        "title": "Authentic Kerala Ayurveda",
        "slug": "kerala-ayurveda",
        "seo": {
          "meta_title": "Best Kerala Ayurveda in Pune | Authentic Panchakarma Clinic",
          "meta_description": "Looking for the best Kerala Ayurveda in Pune? Experience authentic Panchakarma, Nadi Pariksha, and classical herbal treatments at Karmanya Ayurveda."
        },
        "marketing": {
          "hero_eyebrow": "Classical Kerala Tradition",
          "hero_title": "Authentic Kerala Ayurveda & Panchakarma",
          "hero_description": "We bring the unadulterated healing traditions of Kerala to Pune, offering physician-prescribed treatments using authentic medicinal oils and classical protocols.",
          "image_url": "/images/protocols/protocol-back-kati-basti.webp"
        },
        "clinical": {
          "ayurvedic_perspective": "Kerala is globally renowned as the cradle of authentic Ayurveda, preserving the Ashtavaidya tradition unbroken for centuries. Unlike commercial spas, true Kerala Ayurveda is deeply clinical, relying on precise botanical formulations, rigorous Panchakarma purification, and strict adherence to classical texts like the Sahasrayogam and Ashtanga Hrudayam.",
          "assessment_process": "Every patient undergoes a thorough Nadi Pariksha (Pulse Diagnosis) by our senior BAMS physicians, following the pure Kerala diagnostic methodology to uncover root doshic imbalances.",
          "related_treatments": [
            "panchakarma",
            "kerala-chikitsa",
            "shirodhara",
            "abhyangam"
          ],
          "approach": "Our Kerala approach guarantees: 1) 100% genuine GMP-certified medicines sourced directly from Arya Vaidya Sala Kottakkal. 2) Traditional therapies performed on authentic medicinal wood Dronis. 3) Strict medical supervision for all Panchakarma and specialized pain management therapies."
        },
        "safety": {
          "disclaimer": "All therapies are prescribed purely on clinical necessity following a consultation.",
          "emergency_rule": "Kerala Ayurveda is excellent for chronic conditions, but acute medical emergencies require allopathic intervention."
        }
    }
    conditions.append(kerala_condition)
    
    with open('data/conditions.json', 'w') as f:
        json.dump(conditions, f, indent=2)
    print("Added Kerala Ayurveda condition!")
