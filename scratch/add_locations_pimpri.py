import json

with open('data/locations.json', 'r') as f:
    locations = json.load(f)

new_locations = [
  {
    "id": "pimpri",
    "slug": "pimpri",
    "name": "Pimpri",
    "full_name": "Pimpri, Pune",
    "seo": {
      "meta_title": "Ayurvedic Doctor in Pimpri (Clinic in Pimple Saudagar)",
      "meta_description": "Looking for an Ayurvedic doctor in Pimpri? Karmanya Ayurveda is located just 10 mins away in Pimple Saudagar. Expert Panchakarma & pain management."
    },
    "hero": {
      "eyebrow": "10 MINS FROM PIMPRI \u2022 CLINIC IN PIMPLE SAUDAGAR",
      "h1": "Ayurvedic Clinic near Pimpri \u2014 Karmanya Ayurveda",
      "lead": "Patients from Pimpri visit Karmanya Ayurveda for physician-led pain management and clinical Panchakarma. Located just a short drive away at Swaraj Garden Road."
    },
    "transit": {
      "distance": "5.0 km from Pimpri",
      "drive_time": "10\u201312 minutes drive to our Pimple Saudagar clinic",
      "landmarks": "Drive via Kalewadi Phata directly to Swaraj Garden Road."
    },
    "clinical_focus": {
      "overview": "We specialize in non-surgical treatments for joint and spine pain, serving patients from across the PCMC region including Pimpri.",
      "top_conditions": [
        "spine-sciatica-back-pain",
        "knee-joint-pain",
        "digestive-metabolic-disorders"
      ]
    },
    "faqs": [
      {
        "question": "Do you have a branch in Pimpri?",
        "answer": "No, our only clinic is located at 27/11 Swaraj Garden Road, Pimple Saudagar, just a short 10-minute drive from Pimpri."
      }
    ],
    "geo": {
      "latitude": 18.6279,
      "longitude": 73.8014,
      "postal_code": "411018"
    }
  },
  {
    "id": "kalewadi",
    "slug": "kalewadi",
    "name": "Kalewadi",
    "full_name": "Kalewadi, Pune",
    "seo": {
      "meta_title": "Ayurvedic Doctor in Kalewadi | Clinic near Kalewadi",
      "meta_description": "Authentic Ayurvedic doctor near Kalewadi. Karmanya Ayurveda is located just 5 mins away in Pimple Saudagar, offering specialized joint & spine care."
    },
    "hero": {
      "eyebrow": "5 MINS FROM KALEWADI \u2022 CLINIC IN PIMPLE SAUDAGAR",
      "h1": "Ayurvedic Clinic near Kalewadi \u2014 Karmanya Ayurveda",
      "lead": "Looking for genuine Ayurveda near Kalewadi? Karmanya Ayurveda is located just 2 km away in Pimple Saudagar, offering non-surgical treatments for chronic pain."
    },
    "transit": {
      "distance": "2.0 km from Kalewadi",
      "drive_time": "5 minutes drive to our Pimple Saudagar clinic",
      "landmarks": "Drive via Kalewadi Phata directly onto Swaraj Garden Road."
    },
    "clinical_focus": {
      "overview": "Patients from Kalewadi find it extremely convenient to attend daily Panchakarma and pain management therapies at our Swaraj Garden Road facility.",
      "top_conditions": [
        "knee-joint-pain",
        "spine-sciatica-back-pain",
        "womens-health-pcod-hormonal"
      ]
    },
    "faqs": [
      {
        "question": "Where is the clinic relative to Kalewadi?",
        "answer": "We are located at 27/11 Swaraj Garden Road, Pimple Saudagar, which is only about 2 km (a 5-minute drive) from Kalewadi."
      }
    ],
    "geo": {
      "latitude": 18.6046,
      "longitude": 73.7850,
      "postal_code": "411017"
    }
  },
  {
    "id": "thergaon",
    "slug": "thergaon",
    "name": "Thergaon",
    "full_name": "Thergaon, Pune",
    "seo": {
      "meta_title": "Ayurvedic Doctor in Thergaon | Clinic near Thergaon",
      "meta_description": "Looking for an Ayurvedic doctor in Thergaon? Karmanya Ayurveda is located just 10 mins away in Pimple Saudagar. Expert joint & spine pain treatments."
    },
    "hero": {
      "eyebrow": "10 MINS FROM THERGAON \u2022 CLINIC IN PIMPLE SAUDAGAR",
      "h1": "Ayurvedic Clinic near Thergaon \u2014 Karmanya Ayurveda",
      "lead": "Patients from Thergaon seeking genuine Kerala Panchakarma and pain management travel to our Pimple Saudagar facility for classical therapies."
    },
    "transit": {
      "distance": "4.5 km from Thergaon",
      "drive_time": "10 minutes drive to our Pimple Saudagar clinic",
      "landmarks": "Drive via Dange Chowk and Kalewadi Phata directly to Swaraj Garden Road."
    },
    "clinical_focus": {
      "overview": "We offer non-surgical treatments for chronic joint pain, slip disc, and sciatica for patients coming from Thergaon.",
      "top_conditions": [
        "knee-joint-pain",
        "spine-sciatica-back-pain",
        "cervical-spondylosis-neck-pain"
      ]
    },
    "faqs": [
      {
        "question": "Is there a Karmanya Ayurveda branch in Thergaon?",
        "answer": "No, our only clinic is located at 27/11 Swaraj Garden Road, Pimple Saudagar, just a 10-minute drive from Thergaon."
      }
    ],
    "geo": {
      "latitude": 18.6186,
      "longitude": 73.7656,
      "postal_code": "411033"
    }
  }
]

locations.extend(new_locations)

with open('data/locations.json', 'w') as f:
    json.dump(locations, f, indent=2)

