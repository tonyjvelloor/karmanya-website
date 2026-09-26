import json

with open('data/locations.json', 'r') as f:
    locations = json.load(f)

new_locations = [
  {
    "id": "aundh",
    "slug": "aundh",
    "name": "Aundh",
    "full_name": "Aundh, Pune",
    "seo": {
      "meta_title": "Ayurvedic Doctor near Aundh (Clinic in Pimple Saudagar) | Karmanya",
      "meta_description": "Looking for an Ayurvedic doctor near Aundh, Pune? Karmanya Ayurveda is located just 10 mins away in Pimple Saudagar. Expert Panchakarma & pain management."
    },
    "hero": {
      "eyebrow": "10 MINS FROM AUNDH \u2022 CLINIC IN PIMPLE SAUDAGAR",
      "h1": "Ayurvedic Care for Aundh Residents \u2014 Clinic in Pimple Saudagar",
      "lead": "Patients from Aundh visit Karmanya Ayurveda for physician-led pain management and clinical Panchakarma. Located just 5.5 km away at Swaraj Garden Road."
    },
    "transit": {
      "distance": "5.5 km from Aundh",
      "drive_time": "10\u201315 minutes drive to our Pimple Saudagar clinic",
      "landmarks": "Drive via Aundh-Ravet BRTS Road or Sangvi-Kiwale Road directly to Swaraj Garden Road."
    },
    "clinical_focus": {
      "overview": "Residents of Aundh frequently consult our physicians for lifestyle and metabolic disorders, as well as specialized Kerala therapies for joint and spine pain.",
      "top_conditions": [
        "spine-sciatica-back-pain",
        "cervical-spondylosis-neck-pain",
        "digestive-metabolic-disorders",
        "stress-insomnia-anxiety"
      ]
    },
    "faqs": [
      {
        "question": "Do you have a branch in Aundh?",
        "answer": "No, our only clinic is located at 27/11 Swaraj Garden Road, Pimple Saudagar, just a short 10-15 minute drive from Aundh."
      }
    ],
    "geo": {
      "latitude": 18.5626,
      "longitude": 73.8087,
      "postal_code": "411007"
    }
  },
  {
    "id": "rahatani",
    "slug": "rahatani",
    "name": "Rahatani",
    "full_name": "Rahatani, Pune",
    "seo": {
      "meta_title": "Ayurvedic Doctor in Rahatani | Clinic near Rahatani",
      "meta_description": "Authentic Ayurvedic doctor near Rahatani. Karmanya Ayurveda is located just 5 mins away in Pimple Saudagar, offering specialized joint & spine care."
    },
    "hero": {
      "eyebrow": "5 MINS FROM RAHATANI \u2022 CLINIC IN PIMPLE SAUDAGAR",
      "h1": "Ayurvedic Clinic near Rahatani \u2014 Karmanya Ayurveda",
      "lead": "Looking for genuine Ayurveda near Rahatani? Karmanya Ayurveda is located just 1.5 km away in Pimple Saudagar, offering non-surgical treatments for chronic pain."
    },
    "transit": {
      "distance": "1.5 km from Rahatani",
      "drive_time": "5 minutes drive to our Pimple Saudagar clinic",
      "landmarks": "Drive via Rahatani Road directly onto Swaraj Garden Road."
    },
    "clinical_focus": {
      "overview": "Rahatani is practically our neighborhood. Patients from Rahatani find it extremely convenient to attend daily Panchakarma and pain management therapies at our Swaraj Garden Road facility.",
      "top_conditions": [
        "knee-joint-pain",
        "spine-sciatica-back-pain",
        "womens-health-pcod-hormonal",
        "digestive-metabolic-disorders"
      ]
    },
    "faqs": [
      {
        "question": "Where is the clinic relative to Rahatani?",
        "answer": "We are located at 27/11 Swaraj Garden Road, Pimple Saudagar, which is only about 1.5 km (a 5-minute drive) from Rahatani."
      }
    ],
    "geo": {
      "latitude": 18.6015,
      "longitude": 73.7846,
      "postal_code": "411017"
    }
  }
]

locations.extend(new_locations)

with open('data/locations.json', 'w') as f:
    json.dump(locations, f, indent=2)

