import re

with open('scratch/generate_comparison_pages.py', 'r') as f:
    content = f.read()

new_comps = """
    {
        "slug": "karmanya-ayurveda-vs-jivan-urja-chikitsalaya",
        "title": "Karmanya Ayurveda vs Jivan Urja Chikitsalaya: Choosing the Right Ayurvedic Clinic in Pune",
        "meta_title": "Karmanya Ayurveda vs Jivan Urja Chikitsalaya | Pune Clinic Comparison",
        "meta_desc": "Comparing Karmanya Ayurveda (Pimple Saudagar) vs Jivan Urja Chikitsalaya. Read our guide to understand the differences in treatments, physician care, and panchakarma.",
        "condition_name": "Ayurvedic Treatment in Pune",
        "condition_url": "/locations/",
        "read_time": "5 min read",
        "summary": "When searching for authentic Ayurvedic treatment in Pune, patients often compare top clinics. Both Karmanya Ayurveda and Jivan Urja Chikitsalaya are well-known, but they have different clinical models and treatment approaches.",
        "table": [
            ("Parameter", "Karmanya Ayurveda (Pimple Saudagar)", "Jivan Urja Chikitsalaya"),
            ("Specialization", "Clinical Kerala Ayurveda, Pain Management, Panchakarma", "General Ayurveda & Wellness"),
            ("Primary Treatments", "Janu Basti, Kati Basti, Authentic Njavara Kizhi", "General consultations and mixed therapies"),
            ("Physician Led", "Yes, direct MD/BAMS oversight for all procedures", "Physician consultation available"),
            ("Location", "Pimple Saudagar (serving PCMC, Wakad, Hinjawadi)", "Multiple / specific local branches")
        ],
        "sections": [
            {
                "heading": "The Kerala Ayurveda Difference",
                "content": "Karmanya Ayurveda strictly adheres to the classical Kerala Ayurvedic tradition. Our therapeutic formulations are sourced from the legendary Arya Vaidya Sala Kottakkal and Vaidyaratnam Oushadhasala. Every procedure, from Janu Basti to full Panchakarma detoxification, is executed under strict clinical protocols."
            },
            {
                "heading": "Focus on Pain Management without Surgery",
                "content": "While many clinics offer general wellness massages, Karmanya is fundamentally a pain management and clinical treatment center. Our success in managing Grade 1-3 knee osteoarthritis and lumbar disc herniation (sciatica) without surgery draws patients from across Pune and PCMC."
            }
        ],
        "faqs": [
            {
                "q": "Does Karmanya Ayurveda treat the same conditions as Jivan Urja?",
                "a": "Yes, we treat similar chronic conditions, but our approach relies heavily on specialized Kerala therapies like Kizhi, Pizhichil, and targeted Basti programs."
            },
            {
                "q": "Why choose Karmanya Ayurveda?",
                "a": "Patients choose Karmanya for the individualized clinical attention from Dr. Irshad and Dr. Tejasvi, genuine medicines, and the highly specific, non-surgical pain management protocols."
            }
        ]
    },
    {
        "slug": "karmanya-ayurveda-vs-sadhana-ayurvedic-clinic",
        "title": "Karmanya Ayurveda vs Sadhana Ayurvedic Clinic",
        "meta_title": "Karmanya Ayurveda vs Sadhana Ayurvedic Clinic Pune | Compare Clinics",
        "meta_desc": "Comparing Karmanya Ayurveda and Sadhana Ayurvedic Clinic in Pune. Understand the differences in approach, therapies, and specializations for knee pain and sciatica.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "5 min read",
        "summary": "Many patients seeking relief from chronic pain or metabolic disorders in Pune weigh their options between Karmanya Ayurveda and Sadhana Ayurvedic Clinic. This page provides a transparent comparison to help you choose the best clinical fit for your needs.",
        "table": [
            ("Parameter", "Karmanya Ayurveda", "Sadhana Ayurvedic Clinic"),
            ("Core Focus", "Non-Surgical Joint & Spine Care, Women's Health", "Ayurvedic Consultations & General Care"),
            ("Tradition", "Authentic Kerala Ayurvedic Protocols", "Traditional Ayurveda"),
            ("Medicine Sourcing", "Arya Vaidya Sala Kottakkal & Vaidyaratnam", "In-house or varied sources"),
            ("Patient Experience", "1-on-1 clinical tracking, structured rehab plans", "Consultation-focused")
        ],
        "sections": [
            {
                "heading": "Specialized Spine and Joint Programs",
                "content": "Karmanya Ayurveda is renowned in Pimple Saudagar and West Pune for its highly structured Spine & Pain Management Programs. We don't just offer temporary relief; we use diagnostic integration (MRI/X-Ray review + Nadi Pariksha) to deliver targeted therapies like Kati Basti and Viddhakarma to avoid surgery."
            },
            {
                "heading": "Clinical Panchakarma vs Spa Detox",
                "content": "Panchakarma at Karmanya is a medical procedure. It requires pre-purification (Purvakarma), strict dietary adherence, and post-procedure recovery (Paschat Karma). It is never sold as a relaxing spa package, ensuring high clinical efficacy for conditions like PCOD, IBS, and severe Vata disorders."
            }
        ],
        "faqs": [
            {
                "q": "Where is Karmanya Ayurveda located compared to other clinics?",
                "a": "We are centrally located in Pimple Saudagar, making it highly accessible for patients from Wakad, Hinjawadi, Aundh, and Baner."
            }
        ]
    },
"""

content = content.replace("comparisons = [", "comparisons = [\n" + new_comps)

with open('scratch/generate_comparison_pages.py', 'w') as f:
    f.write(content)

