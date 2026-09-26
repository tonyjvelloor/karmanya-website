import re

with open('scratch/generate_comparison_pages.py', 'r') as f:
    content = f.read()

new_comps = """
    {
        "slug": "karmanya-ayurveda-vs-punarvasu-ayurved",
        "title": "Karmanya Ayurveda vs Punarvasu Ayurved in Pune",
        "meta_title": "Karmanya Ayurveda vs Punarvasu Ayurved Pune | Compare",
        "meta_desc": "Compare Karmanya Ayurveda in Pimple Saudagar with Punarvasu Ayurved. Learn about our targeted clinical protocols for knee and spine pain.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "4 min read",
        "summary": "Patients exploring Ayurvedic treatment options in Pune frequently consider both Karmanya Ayurveda and Punarvasu Ayurved. This comparison helps clarify our specialized clinical approach.",
        "table": [
            ("Parameter", "Karmanya Ayurveda", "Punarvasu Ayurved"),
            ("Specialization", "Non-Surgical Joint & Spine Care", "General Ayurveda"),
            ("Therapies", "Authentic Kerala Protocols", "Traditional Ayurvedic treatments"),
            ("Location", "Pimple Saudagar", "Pune locations")
        ],
        "sections": [
            {
                "heading": "Specialized Kerala Pain Management",
                "content": "Karmanya's core focus is on preventing surgery for conditions like Stage 4 Knee Osteoarthritis and Lumbar Disc Herniation. Our highly specific Kerala protocols (Janu Basti, Kati Basti) are administered directly under MD/BAMS physician oversight."
            }
        ],
        "faqs": [
            {
                "q": "What makes Karmanya Ayurveda different?",
                "a": "Our intense clinical focus on pain management and avoiding surgery, combined with authentic Kerala medicines."
            }
        ]
    },
    {
        "slug": "karmanya-ayurveda-vs-tapasvi-ayurved",
        "title": "Karmanya Ayurveda vs Tapasvi Ayurved",
        "meta_title": "Karmanya Ayurveda vs Tapasvi Ayurved Pune | Compare",
        "meta_desc": "Comparing Karmanya Ayurveda with Tapasvi Ayurved. Discover our physician-led Kerala therapies for sciatica, joint pain, and panchakarma.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "4 min read",
        "summary": "When deciding between Karmanya Ayurveda and Tapasvi Ayurved, it helps to understand their different clinical models and treatment specialties.",
        "table": [
            ("Parameter", "Karmanya Ayurveda", "Tapasvi Ayurved"),
            ("Clinic Model", "Physician-Led Pain Management Clinic", "General Ayurveda Clinic"),
            ("Core Treatments", "Kerala Panchakarma, Kizhi, Basti", "General consultations"),
            ("Location", "Pimple Saudagar", "Pune")
        ],
        "sections": [
            {
                "heading": "Clinical Panchakarma",
                "content": "Panchakarma at Karmanya is an intensive medical protocol requiring pre-purification (Purvakarma) and post-recovery (Paschat Karma). We focus on delivering clinical results for conditions like PCOD and severe Vata disorders."
            }
        ],
        "faqs": [
            {
                "q": "Why do patients travel to Pimple Saudagar for Karmanya?",
                "a": "For the specific Kerala Ayurvedic protocols that have proven successful in managing severe joint and spine pain without surgery."
            }
        ]
    },
    {
        "slug": "karmanya-ayurveda-vs-khadiwale-vaidya",
        "title": "Karmanya Ayurveda vs Khadiwale Vaidya",
        "meta_title": "Karmanya Ayurveda vs Khadiwale Vaidya Pune | Compare",
        "meta_desc": "Compare Karmanya Ayurveda with the traditional approach of Khadiwale Vaidya in Pune.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "4 min read",
        "summary": "Khadiwale Vaidya is a historic and highly respected name in Pune's traditional Ayurveda. Karmanya Ayurveda brings a different approach: specialized Kerala Ayurvedic clinical protocols.",
        "table": [
            ("Parameter", "Karmanya Ayurveda", "Khadiwale Vaidya"),
            ("Tradition", "Kerala Ayurveda (Ashtavaidya tradition)", "Maharashtrian Traditional Ayurveda"),
            ("Focus", "Intensive In-Clinic Therapies (Basti, Kizhi)", "Herbal dispensing and consultations"),
            ("Medicines", "Arya Vaidya Sala Kottakkal", "Khadiwale products")
        ],
        "sections": [
            {
                "heading": "In-Clinic Therapy vs Dispensing",
                "content": "While traditional setups often focus heavily on dispensing medicines for home use, Karmanya is a fully equipped therapy center. For conditions like severe sciatica, we perform daily Kati Basti and Njavara Kizhi in-clinic to achieve structural pain relief."
            }
        ],
        "faqs": [
            {
                "q": "Does Karmanya use local medicines?",
                "a": "We strictly use classical formulations from reputed Kerala pharmacies to ensure maximum potency for our pain management protocols."
            }
        ]
    },
"""

content = content.replace("comparisons = [", "comparisons = [\n" + new_comps)

with open('scratch/generate_comparison_pages.py', 'w') as f:
    f.write(content)

