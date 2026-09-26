import re

with open('scratch/generate_comparison_pages.py', 'r') as f:
    content = f.read()

new_comps = """
    {
        "slug": "karmanya-ayurveda-vs-nisarg-ayurved-pune",
        "title": "Karmanya Ayurveda vs Nisarg Ayurved: A Clinical Comparison in Pune",
        "meta_title": "Karmanya Ayurveda vs Nisarg Ayurved Pune | Compare Clinics",
        "meta_desc": "Comparing Karmanya Ayurveda (Pimple Saudagar) and Nisarg Ayurved. Understand the differences in Panchakarma, pain management, and physician care.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "5 min read",
        "summary": "When seeking authentic Ayurvedic treatments in Pune, patients often compare Karmanya Ayurveda and Nisarg Ayurved. Both offer traditional therapies, but their clinical focus and methodologies differ.",
        "table": [
            ("Parameter", "Karmanya Ayurveda", "Nisarg Ayurved"),
            ("Clinical Focus", "Non-Surgical Joint/Spine Care & Medical Panchakarma", "General Ayurveda & Wellness"),
            ("Specialization", "Kerala Ayurvedic Therapies (Kizhi, Basti)", "Traditional Ayurvedic Treatments"),
            ("Patient Experience", "Physician-led individualized protocols", "Consultation and general therapy")
        ],
        "sections": [
            {
                "heading": "Medical Panchakarma vs General Detox",
                "content": "At Karmanya, Panchakarma is conducted as a strict medical procedure. It is never offered as a spa package. Our focus on chronic conditions like Sciatica and Grade 4 Arthritis means therapies like Kati Basti and Janu Basti are administered with precision and classical medicated oils."
            }
        ],
        "faqs": [
            {
                "q": "Why choose Karmanya over general clinics?",
                "a": "Karmanya specializes in avoiding surgery for joint and spine issues using authentic Kerala protocols, backed by experienced MD/BAMS doctors."
            }
        ]
    },
    {
        "slug": "karmanya-ayurveda-vs-jiva-ayurveda-pune",
        "title": "Karmanya Ayurveda vs Jiva Ayurveda (Pune Clinics)",
        "meta_title": "Karmanya Ayurveda vs Jiva Ayurveda Pune | Compare",
        "meta_desc": "Comparing the boutique clinical care of Karmanya Ayurveda in Pimple Saudagar with the corporate chain model of Jiva Ayurveda in Pune.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "6 min read",
        "summary": "Jiva Ayurveda is a well-known national chain, while Karmanya Ayurveda operates as a highly specialized, single-location boutique clinic in Pimple Saudagar. Here is how they compare.",
        "table": [
            ("Parameter", "Karmanya Ayurveda (Pimple Saudagar)", "Jiva Ayurveda (Pune Clinics)"),
            ("Clinic Model", "Boutique, Single-Location Physician-Led Clinic", "National Corporate Chain"),
            ("Doctor Interaction", "Consistent 1-on-1 care with Dr. Irshad or Dr. Tejasvi", "Rotating doctors across branches"),
            ("Medicines", "Arya Vaidya Sala Kottakkal & Vaidyaratnam", "In-house Jiva brand products"),
            ("Therapy Style", "Authentic Kerala therapies (wooden droni)", "Standardized chain therapies")
        ],
        "sections": [
            {
                "heading": "The Boutique vs Chain Experience",
                "content": "As a national chain, Jiva Ayurveda offers accessibility across India. However, patients looking for highly personalized, consistent doctor-patient relationships prefer Karmanya's single-clinic model. Here, the doctor who diagnoses you is the same doctor who oversees your daily therapy."
            },
            {
                "heading": "Sourcing Genuine Kerala Medicines",
                "content": "Karmanya does not manufacture its own white-label products. We source our medicated oils and Kashayams directly from the most respected traditional pharmacies in Kerala, ensuring uncompromised potency for our pain management protocols."
            }
        ],
        "faqs": [
            {
                "q": "Is Karmanya Ayurveda part of a chain?",
                "a": "No. We operate a single, highly specialized clinic in Pimple Saudagar, Pune, to maintain strict quality control over our treatments."
            }
        ]
    },
    {
        "slug": "karmanya-ayurveda-vs-muppra-kerala",
        "title": "Karmanya Ayurveda vs Muppra Kerala Ayurveda Pune",
        "meta_title": "Karmanya Ayurveda vs Muppra Kerala Ayurveda Pune",
        "meta_desc": "Compare Karmanya Ayurveda in Pimple Saudagar with Muppra Kerala Ayurveda. Both offer Kerala therapies, but their focus areas differ.",
        "condition_name": "Ayurvedic Clinics",
        "condition_url": "/locations/",
        "read_time": "5 min read",
        "summary": "Both Karmanya Ayurveda and Muppra Kerala Ayurveda specialize in Kerala-style treatments in Pune. This page outlines the differences to help you decide.",
        "table": [
            ("Parameter", "Karmanya Ayurveda", "Muppra Kerala Ayurveda"),
            ("Location", "Pimple Saudagar (West Pune/PCMC)", "Multiple locations"),
            ("Primary Focus", "Non-Surgical Spine & Joint Pain, PCOD", "Kerala Therapies & Wellness"),
            ("Diagnostics", "Nadi Pariksha + MRI/X-Ray Integration", "Standard Consultation")
        ],
        "sections": [
            {
                "heading": "Targeted Pain Management Protocols",
                "content": "Karmanya has built its reputation on rescuing patients from imminent knee and spine surgeries. Our 14-to-21 day intensive protocols for Sciatica and Osteoarthritis are strictly doctor-managed."
            }
        ],
        "faqs": [
            {
                "q": "Which clinic is better for slip disc?",
                "a": "Karmanya's specific Spine Care program integrates Kati Basti, Basti, and Viddhakarma to decompress nerves effectively without surgery."
            }
        ]
    },
"""

content = content.replace("comparisons = [", "comparisons = [\n" + new_comps)

with open('scratch/generate_comparison_pages.py', 'w') as f:
    f.write(content)

