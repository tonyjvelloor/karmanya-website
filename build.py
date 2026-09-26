import json
import os
import sys
import shutil
import re
import urllib.parse

def render_template(template_str, data):
    def list_replacer(match):
        key = match.group(1)
        inner_content = match.group(2)
        keys = key.split('.')
        val = data
        for k in keys:
            if isinstance(val, dict):
                val = val.get(k, None)
            else:
                val = None
        if isinstance(val, list):
            output = ""
            for item in val:
                if isinstance(item, dict):
                    output += render_template(inner_content, item)
                else:
                    output += inner_content.replace('{{.}}', str(item))
            return output
        return ""

    template_str = re.sub(r'\{\{#([\w.]+)\}\}(.*?)\{\{/\1\}\}', list_replacer, template_str, flags=re.DOTALL)
    
    def key_replacer(match):
        key = match.group(1)
        keys = key.split('.')
        val = data
        for k in keys:
            if isinstance(val, dict):
                val = val.get(k, "")
            else:
                return ""
        return str(val)
        
    return re.sub(r'\{\{([\w.]+)\}\}', key_replacer, template_str)

def validate_claims(claims_path):
    if not os.path.exists(claims_path):
        return []
    with open(claims_path, 'r') as f:
        claims = json.load(f)
    
    errors = []
    for claim in claims:
        if claim['status'] != 'approved' and claim['status'] != 'rejected':
            errors.append(f"Unresolved claim blocks build: {claim['id']} is '{claim['status']}'")
        if claim['status'] == 'approved':
            if not claim.get('approved_by'):
                errors.append(f"Approved claim missing reviewer: {claim['id']}")
            if not claim.get('approved_at'):
                errors.append(f"Approved claim missing date: {claim['id']}")
            if not claim.get('review_expires'):
                errors.append(f"Approved claim missing expiration date: {claim['id']}")
    return errors

def validate_page(page, page_type):
    errors = []
    if 'seo' not in page or 'meta_title' not in page['seo']:
        errors.append(f"Missing seo.meta_title in {page.get('id', page.get('slug'))}")
    if 'seo' not in page or 'meta_description' not in page['seo']:
        errors.append(f"Missing seo.meta_description in {page.get('id', page.get('slug'))}")
    if page_type in ['condition', 'treatment']:
        if 'safety' not in page:
            errors.append(f"Missing safety block in {page.get('id')}")
        elif 'emergency_rule' not in page['safety']:
            errors.append(f"Missing safety.emergency_rule in {page.get('id')}")
    if page_type == 'condition' and 'disclaimer' not in page.get('safety', {}):
        errors.append(f"Missing safety.disclaimer in condition {page.get('id')}")
    if page_type == 'treatment' and 'suitability' not in page.get('safety', {}):
        errors.append(f"Missing safety.suitability in treatment {page.get('id')}")
    if page_type in ['condition', 'treatment'] and ('metadata' not in page or 'reviewed_by' not in page['metadata']):
        errors.append(f"Missing metadata.reviewed_by in {page.get('id')}")
    return errors

def generate_seo_head(page_type, page_data, site_data):
    brand = site_data.get('brand', {})
    geo = brand.get('geo', {})
    
    title = f"{brand.get('name', 'Karmanya Ayurveda')}"
    desc = brand.get('subheadline', '')
    url = "https://karmanyaayurveda.com/"
    image = "https://karmanyaayurveda.com/images/doctor-consult.webp"
    
    breadcrumbs = []
    entity_schema = None
    faq_schema = None
    
    if page_type == 'home':
        title = f"Best Ayurvedic Clinic Near Me | Panchakarma & Ayurvedic Medical Center Pune | {brand.get('name')}"
        desc = "Looking for an Ayurvedic clinic near me or a Panchakarma center? Karmanya Ayurveda in Pune offers expert Ayurvedic medical care for knee & spine pain, and authentic Kerala therapies. Mon–Sun 10 AM–8 PM."
        url = "https://karmanyaayurveda.com/"
        
        entity_schema = {
            "@context": "https://schema.org",
            "@type": ["MedicalClinic", "LocalBusiness"],
            "name": brand.get('name'),
            "url": url,
            "telephone": brand.get('phone'),
            "priceRange": "$$",
            "image": image,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "27/11, Swaraj Garden Road, Near One Nation Apartment",
                "addressLocality": "Pimple Saudagar, Pimpri-Chinchwad, Pune",
                "addressRegion": "Maharashtra",
                "postalCode": "411027",
                "addressCountry": "IN"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": geo.get('latitude', 18.5956),
                "longitude": geo.get('longitude', 73.7979)
            },
            "hasMap": "https://maps.google.com/?cid=3077549578320836260",
            "sameAs": [
                "https://maps.google.com/?cid=3077549578320836260",
                "https://www.google.com/search?q=karmanya+ayurveda+address&ludocid=3077549578320836260",
                "https://www.instagram.com/karmanyaayurveda"
            ],
            "openingHoursSpecification": brand.get('opening_hours', []),
            "areaServed": [
                {"@type": "Place", "name": "Pimple Saudagar"},
                {"@type": "Place", "name": "Wakad"},
                {"@type": "Place", "name": "Hinjawadi"},
                {"@type": "Place", "name": "Baner"},
                {"@type": "Place", "name": "Aundh"},
                {"@type": "Place", "name": "Pimpri-Chinchwad"},
                {"@type": "Place", "name": "Rahatani"},
                {"@type": "Place", "name": "Ravet"}
            ],
            "medicalSpecialty": [
                "Ayurvedic", "Pain Management", "Panchakarma", "Spine Care", "Holistic Health"
            ],
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "bestRating": "5",
                "worstRating": "1",
                "reviewCount": "186"
            },
            "review": [
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Ramesh S."},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": "After 3 years of knee pain and mobility limitations, Dr. Irshad's protocol with Janu Basti gave me substantial relief in 6 weeks. I was able to regain comfortable mobility through conservative Ayurvedic care."
                },
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Priya N."},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": "I came expecting a massage. Instead, I got a full clinical assessment and a 3-month treatment plan. This is a real medical centre. My sciatica is 90% better."
                },
                {
                    "@type": "Review",
                    "author": {"@type": "Person", "name": "Snehal K."},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": "Dr. Tejasvi's approach to my PCOD was completely different — she addressed my insulin resistance and Kapha imbalance together. My cycles regularised within 2 months naturally."
                }
            ]
        }

        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Does Karmanya Ayurveda offer non-surgical treatment for knee and spine pain in Pune?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Yes. Karmanya Ayurveda specializes in physician-prescribed, non-surgical management of knee osteoarthritis, sciatica, and lumbar disc bulges. Using authentic Kerala therapies like Janu Basti, Kati Basti, and Patra Pinda Sweda, our doctors focus on restoring synovial fluid and decompressing trapped nerve roots without surgery."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How many sessions are required for Ayurvedic pain relief?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "In authentic classical Kerala Ayurveda, treatment duration and session frequency are never promised in advance. Every individual's body constitution (Prakriti), chronicity of pain, and tissue condition are distinct. Following an in-person Nadi Pariksha (pulse diagnosis) and scan review, our BAMS physicians prescribe a customized clinical care protocol (typically 7 to 14 days)."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How is Karmanya Ayurveda different from a commercial wellness spa?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Karmanya Ayurveda is a physician-led clinical treatment centre, not a day spa. Every therapy session is conducted under direct oversight of senior BAMS/MD Kerala physicians. We do not sell standardized relaxation packages; every protocol begins with a clinical diagnosis and uses 100% genuine GMP-certified medicines from Arya Vaidya Sala Kottakkal and Vaidyaratnam Oushadhasala."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Where is the Karmanya Ayurveda clinic located and what are the OPD timings?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Our clinic is located at 27/11 Swaraj Garden Road, near One Nation Apartment, Pimple Saudagar, Pune (411027). OPD timings are Monday to Sunday from 10:00 AM to 8:00 PM. Consultations are conducted in-person to ensure accurate Nadi Pariksha."
                    }
                },
                {
                    "@type": "Question",
                    "name": "Which areas in Pune are closest to Karmanya Ayurveda?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Karmanya Ayurveda serves patients across West Pune and PCMC, easily accessible within 5 to 15 minutes from Wakad (3.2 km), Hinjawadi IT Park (7.5 km), Baner (6.8 km), Aundh (5.5 km), Rahatani (1.5 km), and Ravet."
                    }
                }
            ]
        }
        
    elif page_type == 'location':
        loc_name = page_data.get('name', 'Pune')
        title = page_data.get('seo', {}).get('meta_title', f"Ayurvedic Clinic near {loc_name}, Pune | Karmanya Ayurveda")
        desc = page_data.get('seo', {}).get('meta_description', f"Authentic Kerala Ayurveda clinic near {loc_name}. Specialized Panchakarma, knee pain, and spine care.")
        url = f"https://karmanyaayurveda.com/locations/{page_data.get('slug')}/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Nearby Areas", "item": "https://karmanyaayurveda.com/locations/"},
            {"@type": "ListItem", "position": 3, "name": loc_name, "item": url}
        ]
        
        entity_schema = {
            "@context": "https://schema.org",
            "@type": ["MedicalClinic", "LocalBusiness"],
            "name": brand.get('name'),
            "url": url,
            "telephone": brand.get('phone'),
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "27/11, Swaraj Garden Road, Near One Nation Apartment",
                "addressLocality": "Pimple Saudagar, Pimpri-Chinchwad, Pune",
                "addressRegion": "Maharashtra",
                "postalCode": "411027",
                "addressCountry": "IN"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 18.5956,
                "longitude": 73.7979
            },
            "hasMap": "https://maps.google.com/?cid=3077549578320836260",
            "sameAs": [
                "https://maps.google.com/?cid=3077549578320836260",
                "https://www.google.com/search?q=karmanya+ayurveda+address&ludocid=3077549578320836260"
            ],
            "areaServed": {
                "@type": "Place",
                "name": loc_name,
                "postalCode": page_data.get('geo', {}).get('postal_code', '411027')
            },
            "openingHoursSpecification": brand.get('opening_hours', []),
            "medicalSpecialty": ["Ayurvedic", "Panchakarma", "Pain Management"]
        }
        
        if page_data.get('faqs'):
            schema_faqs = []
            for f_item in page_data['faqs']:
                schema_faqs.append({"@type": "Question", "name": f_item['question'], "acceptedAnswer": {"@type": "Answer", "text": f_item['answer']}})
            faq_schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": schema_faqs
            }
            
    elif page_type == 'locations_hub':
        title = f"Our Clinic Location & Nearby Areas Served | {brand.get('name')}"
        desc = "Karmanya Ayurveda operates exclusively from our single clinic at 27/11 Swaraj Garden Road, Pimple Saudagar, Pune. View commute and care guides for Wakad, Hinjawadi, Baner, Aundh & PCMC."
        url = "https://karmanyaayurveda.com/locations/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Nearby Areas", "item": url}
        ]

    elif page_type == 'condition':
        title = page_data.get('seo', {}).get('meta_title', f"Ayurvedic Treatment for {page_data.get('title')} in Pune | {brand.get('name')}")
        desc = page_data.get('seo', {}).get('meta_description', f"Ayurvedic treatment for {page_data.get('title')} in Pimple Saudagar, Pune.")
        url = f"https://karmanyaayurveda.com/conditions/{page_data.get('slug')}/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Conditions", "item": "https://karmanyaayurveda.com/conditions/"},
            {"@type": "ListItem", "position": 3, "name": page_data.get('title'), "item": url}
        ]
        
        treatments_ld = []
        for t in page_data.get('clinical', {}).get('resolved_treatments', []):
            treatments_ld.append({
                "@type": "MedicalTherapy",
                "name": t['name'],
                "url": f"https://karmanyaayurveda.com{t['url']}"
            })
            
        entity_schema = {
            "@context": "https://schema.org",
            "@type": "MedicalCondition",
            "name": page_data.get('title'),
            "description": page_data.get('clinical', {}).get('ayurvedic_perspective', ''),
            "possibleTreatment": treatments_ld,
            "url": url,
            "recognizingAuthority": {
                "@type": ["MedicalClinic", "Physician"],
                "@id": "https://karmanyaayurveda.com/#clinic",
                "name": "Karmanya Ayurveda Chikitsalaya - Dr. Irshad T.M.",
                "url": "https://karmanyaayurveda.com/",
                "telephone": brand.get('phone', '+919819820017'),
                "hasMap": "https://maps.google.com/?cid=3077549578320836260",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "27/11, Swaraj Garden Road, Near One Nation Apartment",
                    "addressLocality": "Pimple Saudagar, Pimpri-Chinchwad, Pune",
                    "addressRegion": "Maharashtra",
                    "postalCode": "411027",
                    "addressCountry": "IN"
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "bestRating": "5",
                    "reviewCount": "186"
                }
            }
        }
        
        if page_data.get('faqs'):
            schema_faqs = []
            for f_item in page_data['faqs']:
                schema_faqs.append({"@type": "Question", "name": f_item['question'], "acceptedAnswer": {"@type": "Answer", "text": f_item['answer']}})
            faq_schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": schema_faqs
            }
            
    elif page_type == 'conditions_hub':
        title = f"Ayurvedic Treatments & Conditions in Pune | {brand.get('name')}"
        desc = "Explore Ayurvedic treatments for Knee Joint Pain, Sciatica, Cervical Spondylosis, PCOS, Skin Disorders, and IBS at Karmanya Ayurveda in Pune."
        url = "https://karmanyaayurveda.com/conditions/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Conditions", "item": url}
        ]

    elif page_type == 'treatment':
        title = page_data.get('seo', {}).get('meta_title', f"{page_data.get('title')} Treatment in Pune | {brand.get('name')}")
        desc = page_data.get('seo', {}).get('meta_description', f"{page_data.get('title')} ayurvedic therapy in Pimple Saudagar, Pune.")
        url = f"https://karmanyaayurveda.com/treatments/{page_data.get('slug')}/"
        if page_data.get('marketing', {}).get('image_url'):
            image = f"https://karmanyaayurveda.com{page_data['marketing']['image_url']}"
            
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Treatments", "item": "https://karmanyaayurveda.com/treatments/"},
            {"@type": "ListItem", "position": 3, "name": page_data.get('title'), "item": url}
        ]
        
        entity_schema = {
            "@context": "https://schema.org",
            "@type": "MedicalTherapy",
            "name": page_data.get('title'),
            "description": page_data.get('clinical', {}).get('ayurvedic_perspective', ''),
            "url": url,
            "provider": {
                "@type": "MedicalClinic",
                "@id": "https://karmanyaayurveda.com/#clinic",
                "name": brand.get('name'),
                "url": "https://karmanyaayurveda.com/",
                "telephone": brand.get('phone', '+919819820017'),
                "hasMap": "https://maps.google.com/?cid=3077549578320836260",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "27/11, Swaraj Garden Road, Near One Nation Apartment",
                    "addressLocality": "Pimple Saudagar, Pimpri-Chinchwad, Pune",
                    "addressRegion": "Maharashtra",
                    "postalCode": "411027",
                    "addressCountry": "IN"
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "bestRating": "5",
                    "reviewCount": "186"
                }
            }
        }
        
    elif page_type == 'treatments_hub':
        title = f"Authentic Kerala Ayurvedic Therapies in Pune | {brand.get('name')}"
        desc = "Authentic Ashtavaidya Kerala therapies in Pune: Panchakarma, Janu Basti, Kati Basti, Shirodhara, Kizhi, and Abhyangam under qualified physicians."
        url = "https://karmanyaayurveda.com/treatments/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Treatments", "item": url}
        ]

    elif page_type == 'doctor':
        title = page_data.get('seo', {}).get('meta_title', f"{page_data.get('name')} | Ayurvedic Doctor in Pune")
        desc = page_data.get('seo', {}).get('meta_description', '')
        url = f"https://karmanyaayurveda.com/doctors/{page_data.get('slug')}/"
        if page_data.get('marketing', {}).get('image_url'):
            image = f"https://karmanyaayurveda.com{page_data['marketing']['image_url']}"
            
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Doctors", "item": "https://karmanyaayurveda.com/doctors/"},
            {"@type": "ListItem", "position": 3, "name": page_data.get('name'), "item": url}
        ]
        
        entity_schema = {
            "@context": "https://schema.org",
            "@type": "Physician",
            "name": page_data.get('name'),
            "jobTitle": page_data.get('title'),
            "medicalSpecialty": page_data.get('clinical', {}).get('specialties', []),
            "url": url,
            "image": image,
            "worksFor": {
                "@type": "MedicalClinic",
                "name": brand.get('name'),
                "url": "https://karmanyaayurveda.com/"
            }
        }
        
    elif page_type == 'doctors_hub':
        title = f"Our Ayurvedic Doctors in Pune | Dr. Irshad & Dr. Tejasvi | {brand.get('name')}"
        desc = "Consult expert Ayurvedic physicians at Karmanya Ayurveda in Pune. Specialized in Panchakarma, spine & joint pain, women's health, and dermatology."
        url = "https://karmanyaayurveda.com/doctors/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Doctors", "item": url}
        ]
        
    elif page_type == 'book':
        title = f"Book Ayurvedic Doctor Consultation (₹500) | Pimple Saudagar, Pune | {brand.get('name')}"
        desc = "Schedule your in-clinic consultation & Nadi Pariksha with senior Ayurvedic physicians in Pimple Saudagar, Pune. Transparent ₹500 fee · Mon–Sun OPD (10 AM–8 PM)."
        url = "https://karmanyaayurveda.com/book-consultation/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Book Consultation", "item": url}
        ]

    # Compile HTML & GEO Meta Tags
    html_tags = f"""
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-NP2DTL98');</script>
    <!-- End Google Tag Manager -->
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-QWH0NSNLVE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-QWH0NSNLVE');
    </script>
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    <link rel="alternate" hreflang="en-IN" href="{url}">
    <link rel="alternate" hreflang="x-default" href="{url}">
    
    <!-- Favicon & App Icons -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#634119">
    
    <!-- Geo Targeting Meta Tags -->
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Pimple Saudagar, Pune">
    <meta name="geo.position" content="18.5956;73.7979">
    <meta name="ICBM" content="18.5956, 73.7979">
    
    <!-- OpenGraph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{image}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{brand.get('name')}">
    <meta property="og:see_also" content="https://www.instagram.com/karmanyaayurveda">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{image}">
    """
    
    if breadcrumbs:
        bc_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumbs
        }
        html_tags += f'\n    <script type="application/ld+json">\n{json.dumps(bc_schema, indent=2)}\n    </script>'
        
    if entity_schema:
        html_tags += f'\n    <script type="application/ld+json">\n{json.dumps(entity_schema, indent=2)}\n    </script>'
        
    if faq_schema:
        html_tags += f'\n    <script type="application/ld+json">\n{json.dumps(faq_schema, indent=2)}\n    </script>'
        
    return html_tags


def build_site():
    base_dir = "/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website"
    
    # 0. Governance Check
    claims_errors = validate_claims(os.path.join(base_dir, 'data', 'claims.json'))
    if claims_errors:
        print("BUILD FAILED: Content Governance Violations")
        for err in claims_errors:
            print(f" - {err}")
        sys.exit(1)
        
    # Sync CSS assets to public/css
    os.makedirs(os.path.join(base_dir, 'public', 'css'), exist_ok=True)
    for fname in os.listdir(os.path.join(base_dir, 'css')):
        if fname.endswith('.css'):
            shutil.copy2(os.path.join(base_dir, 'css', fname), os.path.join(base_dir, 'public', 'css', fname))
    
    # 1. Load Data
    with open(os.path.join(base_dir, 'data', 'site.json'), 'r') as f:
        site_data = json.load(f)
    with open(os.path.join(base_dir, 'data', 'conditions.json'), 'r') as f:
        conditions = json.load(f)
    with open(os.path.join(base_dir, 'data', 'treatments.json'), 'r') as f:
        treatments = json.load(f)
    with open(os.path.join(base_dir, 'data', 'doctors.json'), 'r') as f:
        doctors = json.load(f)
    with open(os.path.join(base_dir, 'data', 'locations.json'), 'r') as f:
        locations = json.load(f)
        
    treat_dict = {t['slug']: t for t in treatments}
    cond_dict = {c['slug']: c for c in conditions}
    
    all_errors = []
    urls_for_sitemap = [
        ('https://karmanyaayurveda.com/', '1.0', 'weekly'),
        ('https://karmanyaayurveda.com/our-story/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/treatments/', '0.9', 'weekly'),
        ('https://karmanyaayurveda.com/conditions/', '0.9', 'weekly'),
        ('https://karmanyaayurveda.com/doctors/', '0.9', 'monthly'),
        ('https://karmanyaayurveda.com/locations/', '0.9', 'weekly'),
        ('https://karmanyaayurveda.com/book-consultation/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/reviews/', '0.85', 'weekly'),
        ('https://karmanyaayurveda.com/blog/', '0.85', 'weekly'),
        ('https://karmanyaayurveda.com/blog/ayurvedic-treatment-knee-pain-pune/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/blog/ayurvedic-sciatica-treatment-pune/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/blog/panchakarma-pune-what-to-expect/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/blog/ayurvedic-treatment-pcod-pune/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/blog/shirodhara-for-stress-insomnia-pune/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/compare/', '0.85', 'weekly'),
        ('https://karmanyaayurveda.com/compare/ayurveda-vs-knee-replacement-surgery/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/compare/ayurveda-vs-surgery-painkillers-sciatica/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/compare/ayurveda-vs-hormonal-pills-pcod/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/symptoms/', '0.85', 'weekly'),
        ('https://karmanyaayurveda.com/symptoms/knee-clicking-popping-sound/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/symptoms/lower-back-pain-when-sitting/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/symptoms/stiff-neck-computer-work/', '0.8', 'monthly'),
        ('https://karmanyaayurveda.com/glossary/', '0.85', 'monthly')
    ]
    
    # Copy Static Assets
    css_src = os.path.join(base_dir, 'css')
    css_dest = os.path.join(base_dir, 'public', 'css')
    if os.path.exists(css_dest):
        shutil.rmtree(css_dest)
    shutil.copytree(css_src, css_dest)
    
    os.makedirs(os.path.join(base_dir, 'images', 'doctors'), exist_ok=True)
    img_src = os.path.join(base_dir, 'images')
    img_dest = os.path.join(base_dir, 'public', 'images')
    if os.path.exists(img_dest):
        shutil.rmtree(img_dest)
    if os.path.exists(img_src):
        shutil.copytree(img_src, img_dest)
    
    # Copy root favicon & webmanifest assets
    root_static_files = [
        'favicon.ico', 'favicon-16x16.png', 'favicon-32x32.png', 'favicon-48x48.png',
        'apple-touch-icon.png', 'android-chrome-192x192.png', 'android-chrome-512x512.png',
        'site.webmanifest'
    ]
    for rf in root_static_files:
        src_path = os.path.join(base_dir, rf)
        if os.path.exists(src_path):
            shutil.copy2(src_path, os.path.join(base_dir, 'public', rf))
    
    # Cross-link and validate
    for cond in conditions:
        urls_for_sitemap.append((f"https://karmanyaayurveda.com/conditions/{cond['slug']}/", '0.85', 'weekly'))
        all_errors.extend(validate_page(cond, 'condition'))
        resolved_treatments = []
        for t_id in cond.get('clinical', {}).get('related_treatments', []):
            if t_id in treat_dict:
                t = treat_dict[t_id]
                resolved_treatments.append({"name": t['title'], "url": f"/treatments/{t['slug']}/"})
        cond['clinical']['resolved_treatments'] = resolved_treatments
        
        resolved_doctors = []
        for doc in doctors:
            if cond['slug'] in doc.get('clinical', {}).get('related_conditions', []):
                resolved_doctors.append({'name': doc['name'], 'title': doc['title'], 'url': f"/doctors/{doc['slug']}/"})
        cond['clinical']['resolved_doctors'] = resolved_doctors

    for treat in treatments:
        urls_for_sitemap.append((f"https://karmanyaayurveda.com/treatments/{treat['slug']}/", '0.85', 'weekly'))
        all_errors.extend(validate_page(treat, 'treatment'))
        resolved_conditions = []
        for c_id in treat.get('clinical', {}).get('related_conditions', []):
            if c_id in cond_dict:
                c = cond_dict[c_id]
                resolved_conditions.append({'name': c['title'], 'url': f"/conditions/{c['slug']}/"})
        treat['clinical']['resolved_conditions'] = resolved_conditions
        
    for doc in doctors:
        urls_for_sitemap.append((f"https://karmanyaayurveda.com/doctors/{doc['slug']}/", '0.8', 'monthly'))
        all_errors.extend(validate_page(doc, 'doctor'))

    for loc in locations:
        urls_for_sitemap.append((f"https://karmanyaayurveda.com/locations/{loc['slug']}/", '0.85', 'weekly'))
        all_errors.extend(validate_page(loc, 'location'))

    if all_errors:
        print("BUILD FAILED: Validation Errors")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)
        
    print("Governance passed. Validation passed. Rendering expanded pages...")
    
    # 2. Render Programmatic Locations
    with open(os.path.join(base_dir, 'templates', 'location.html'), 'r') as f:
        location_template = f.read()
        
    for loc in locations:
        html = location_template
        loc_data = {**loc, **site_data}
        loc_data['seo_head_tags'] = generate_seo_head('location', loc, site_data)
        
        for k, v in site_data['brand'].items():
            html = html.replace(f'{{{{brand.{k}}}}}', str(v))
        html = html.replace("{{seo_head_tags}}", loc_data['seo_head_tags'])
        
        html = html.replace('{{location.name}}', loc['name'])
        html = html.replace('{{location.slug}}', loc['slug'])
        html = html.replace('{{location.hero.eyebrow}}', loc['hero']['eyebrow'])
        html = html.replace('{{location.hero.h1}}', loc['hero']['h1'])
        html = html.replace('{{location.hero.lead}}', loc['hero']['lead'])
        html = html.replace('{{location.transit.distance}}', loc['transit']['distance'])
        html = html.replace('{{location.transit.drive_time}}', loc['transit']['drive_time'])
        html = html.replace('{{location.transit.landmarks}}', loc['transit']['landmarks'])
        html = html.replace('{{location.clinical_focus.overview}}', loc['clinical_focus']['overview'])
        
        faq_html = ""
        for faq in loc.get('faqs', []):
            faq_html += f"""
            <div class="faq-accordion">
                <button class="faq-question">{faq['question']}</button>
                <div class="faq-answer">
                    <p>{faq['answer']}</p>
                </div>
            </div>"""
        html = html.replace('<!-- FAQS_LOOP_PLACEHOLDER -->', faq_html)
        
        loc_dir = os.path.join(base_dir, 'public', 'locations', loc['slug'])
        os.makedirs(loc_dir, exist_ok=True)
        with open(os.path.join(loc_dir, 'index.html'), 'w') as f:
            f.write(html)
            
    # 2b. Render Locations Directory Hub
    with open(os.path.join(base_dir, 'templates', 'locations.html'), 'r') as f:
        locations_hub_template = f.read()
    
    loc_grid_html = ""
    for loc in locations:
        lead_raw = loc['hero']['lead']
        if len(lead_raw) > 175:
            lead_snippet = lead_raw[:175].rsplit(' ', 1)[0] + '...'
        else:
            lead_snippet = lead_raw
        loc_card = f"""
        <div class="location-card">
            <div>
                <span style="color: var(--color-accent); font-weight: 600; font-size: 0.85rem; text-transform: uppercase;">Distance: {loc['transit']['distance']}</span>
                <h3 style="margin: 8px 0 12px; font-size: 1.6rem;"><a href="/locations/{loc['slug']}/" style="color: var(--color-primary); text-decoration: none;">{loc['name']}</a></h3>
                <p style="color: #555; font-size: 1rem; line-height: 1.5; margin-bottom: 16px;">{lead_snippet}</p>
                <p style="font-size: 0.9rem; color: #777;"><strong>Commute to Pimple Saudagar Clinic:</strong> {loc['transit']['drive_time']}</p>
            </div>
            <div style="margin-top: 16px;">
                <a href="/locations/{loc['slug']}/" class="btn btn-secondary" style="padding: 8px 18px; font-size: 0.9rem;">View Commute & Care Guide &rarr;</a>
            </div>
        </div>
        """
        loc_grid_html += loc_card
        
    locations_hub_template = locations_hub_template.replace('<!-- LOCATIONS_GRID_PLACEHOLDER -->', loc_grid_html)
    locations_hub_template = locations_hub_template.replace('{{seo_head_tags}}', generate_seo_head('locations_hub', {}, site_data))
    for k, v in site_data['brand'].items():
        locations_hub_template = locations_hub_template.replace(f'{{{{brand.{k}}}}}', str(v))
        
    hub_loc_dir = os.path.join(base_dir, 'public', 'locations')
    os.makedirs(hub_loc_dir, exist_ok=True)
    with open(os.path.join(hub_loc_dir, 'index.html'), 'w') as f:
        f.write(locations_hub_template)

    # 3. Render Conditions
    with open(os.path.join(base_dir, 'templates', 'condition.html'), 'r') as f:
        condition_template = f.read()
    for cond in conditions:
        data = {**cond, **site_data}
        data['seo_head_tags'] = generate_seo_head('condition', cond, site_data)
        
        # Build resolved_treatments
        resolved = []
        for r_slug in cond.get('clinical', {}).get('related_treatments', []):
            resolved.append({
                "name": r_slug.replace("-", " ").title(),
                "url": f"/treatments/{r_slug}/"
            })
        if 'clinical' not in data: data['clinical'] = {}
        data['clinical']['resolved_treatments'] = resolved

        cond_dir = os.path.join(base_dir, 'public', 'conditions', cond['slug'])
        os.makedirs(cond_dir, exist_ok=True)
        with open(os.path.join(cond_dir, 'index.html'), 'w') as f:
            f.write(render_template(condition_template, data))
            
    # 3b. Render Conditions Directory Hub
    with open(os.path.join(base_dir, 'templates', 'conditions.html'), 'r') as f:
        conditions_hub_template = f.read()
        
    cond_grid_html = ""
    for c in conditions:
        img_url = c.get('marketing', {}).get('image_url', '')
        c_title = c['title']
        img_html = f'<div class="condition-card-image" style="height: 160px; margin-bottom: 14px;"><img src="{img_url}" alt="{c_title} Ayurvedic Treatment" loading="lazy"></div>' if img_url else ''
        card = f"""
        <div class="condition-card">
            <div>
                {img_html}
                <span style="color: var(--color-accent); font-weight: 600; font-size: 0.85rem; text-transform: uppercase;">{c['marketing']['hero_eyebrow']}</span>
                <h3 style="margin: 8px 0 12px; font-size: 1.6rem;"><a href="/conditions/{c['slug']}/" style="color: var(--color-primary); text-decoration: none;">{c['title']}</a></h3>
                <p style="color: #555; font-size: 1rem; line-height: 1.5; margin-bottom: 16px;">{c['marketing']['hero_description']}</p>
                <p style="font-size: 0.9rem; color: #777;"><strong>Medically Reviewed By:</strong> {c['metadata']['reviewed_by']}</p>
            </div>
            <div style="margin-top: 16px;">
                <a href="/conditions/{c['slug']}/" class="btn btn-secondary" style="padding: 8px 18px; font-size: 0.9rem;">Explore Treatment Guide &rarr;</a>
            </div>
        </div>
        """
        cond_grid_html += card
        
    conditions_hub_template = conditions_hub_template.replace('<!-- CONDITIONS_GRID_PLACEHOLDER -->', cond_grid_html)
    conditions_hub_template = conditions_hub_template.replace('{{seo_head_tags}}', generate_seo_head('conditions_hub', {}, site_data))
    for k, v in site_data['brand'].items():
        conditions_hub_template = conditions_hub_template.replace(f'{{{{brand.{k}}}}}', str(v))
        
    hub_cond_dir = os.path.join(base_dir, 'public', 'conditions')
    os.makedirs(hub_cond_dir, exist_ok=True)
    with open(os.path.join(hub_cond_dir, 'index.html'), 'w') as f:
        f.write(conditions_hub_template)

    # 4. Render Treatments
    with open(os.path.join(base_dir, 'templates', 'treatment.html'), 'r') as f:
        treat_template = f.read()
    for treat in treatments:
        data = {**treat, **site_data}
        data['seo_head_tags'] = generate_seo_head('treatment', treat, site_data)

        # Build FAQ HTML and inject FAQPage schema (same pattern as conditions)
        faqs = treat.get('faqs', [])
        if faqs:
            faq_html = '<div class="faq-section" style="margin-top: var(--space-12); border-top: 2px solid var(--color-accent); padding-top: var(--space-8);">'
            faq_html += '<h2 style="font-size: 2rem; color: var(--color-primary); margin-bottom: var(--space-6);">Frequently Asked Questions</h2>'
            for faq in faqs:
                faq_html += f'''<div style="border-bottom: 1px solid var(--color-border); padding: var(--space-5) 0;">
                    <h3 style="font-size: 1.1rem; font-weight: 600; color: var(--color-primary); margin-bottom: var(--space-2);">{faq["question"]}</h3>
                    <p style="color: #555; margin: 0; line-height: 1.7;">{faq["answer"]}</p>
                </div>'''
            faq_html += '</div>'
            data['faqs_html'] = faq_html

            # Inject FAQPage schema into seo_head_tags
            schema_faqs = [{"@type": "Question", "name": f["question"], "acceptedAnswer": {"@type": "Answer", "text": f["answer"]}} for f in faqs]
            faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": schema_faqs}
            import json as _json
            faq_script = f'\n    <script type="application/ld+json">\n{_json.dumps(faq_schema, indent=2)}\n    </script>'
            data['seo_head_tags'] += faq_script
        else:
            data['faqs_html'] = ''

        out_dir = os.path.join(base_dir, 'public', 'treatments', treat['slug'])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w') as f:
            f.write(render_template(treat_template, data))
            
    # 4b. Render Treatments Directory Hub
    with open(os.path.join(base_dir, 'templates', 'treatments.html'), 'r') as f:
        treatments_hub_template = f.read()
        
    treat_grid_html = ""
    category_meta = {
        'panchakarma': {
            'categories': 'detox',
            'badge': 'Ashtavaidya Detox',
            'indications': ['Cellular Detox', 'Metabolic Reset', 'Virechana & Vasti']
        },
        'janu-basti': {
            'categories': 'spine',
            'badge': 'Targeted Joint Care',
            'indications': ['Knee Osteoarthritis', 'Cartilage Wear', 'Synovial Fluid']
        },
        'kati-basti': {
            'categories': 'spine',
            'badge': 'Spine & Sciatica',
            'indications': ['L4-L5 / L5-S1 Sciatica', 'Disc Herniation', 'Lower Back Pain']
        },
        'shirodhara': {
            'categories': 'neuro',
            'badge': 'Neuro-Calm & Sleep',
            'indications': ['Insomnia & Sleep Reset', 'Chronic Anxiety', 'Migraines']
        },
        'kizhi': {
            'categories': 'spine detox',
            'badge': 'Herbal Poultice',
            'indications': ['Cervical Stiffness', 'Frozen Shoulder', 'Joint Inflammation']
        },
        'abhyangam': {
            'categories': 'neuro detox',
            'badge': 'Kerala Full Body',
            'indications': ['Chronic Fatigue', 'Vata Balance', 'Lymphatic Flow']
        },
        'kerala-chikitsa': {
            'categories': 'spine neuro',
            'badge': 'Heritage Chikitsa',
            'indications': ['Marma Physiotherapy', 'Degenerative Spine', 'Paralysis Care']
        },
        'nadi-pariksha': {
            'categories': 'neuro detox',
            'badge': 'Classical Pulse Diagnosis',
            'indications': ['Root-Cause Analysis', 'Prakriti Assessment', 'Dosha Reading']
        },
        'nasya': {
            'categories': 'detox neuro',
            'badge': 'Cranial Cleansing',
            'indications': ['Cervical Spondylosis', 'Chronic Sinusitis', 'Headaches']
        },
        'pizhichil': {
            'categories': 'neuro spine',
            'badge': 'Royal Oil Squeeze',
            'indications': ['Neuromuscular Recovery', 'Severe Spondylosis', 'Full-Body Vata']
        },
        'netratarpana': {
            'categories': 'metabolic neuro',
            'badge': 'Ophthalmic Care',
            'indications': ['IT Digital Screen Strain', 'Dry Eye Syndrome', 'Optic Fatigue']
        },
        'udvartana': {
            'categories': 'metabolic detox',
            'badge': 'Lymphatic Scrub',
            'indications': ['Metabolic Sluggishness', 'Cellulite Mobilization', 'PCOS Support']
        },
        'agnikarma': {
            'categories': 'spine',
            'badge': 'Instant Pain Relief',
            'indications': ['Calcaneal Heel Spur', 'Frozen Shoulder', 'Tendonitis']
        },
        'garbha-sanskar': {
            'categories': 'metabolic',
            'badge': 'Maternal Wellness',
            'indications': ['Pre-Conception Care', 'Prenatal Trimester Support', 'Postpartum Recovery']
        },
        'mukhalepam': {
            'categories': 'metabolic',
            'badge': 'Herbal Dermatology',
            'indications': ['Melasma & Dark Spots', 'Acne Scars', 'Cellular Skin Radiance']
        }
    }

    for t in treatments:
        t_img = t.get('marketing', {}).get('image_url', '')
        t_title = t['title']
        t_slug = t['slug']
        t_desc = t['marketing']['hero_description']
        t_category = t['category']
        meta = category_meta.get(t_slug, {
            'categories': 'spine',
            'badge': 'Classical Protocol',
            'indications': ['Physician Prescribed']
        })
        cats = meta['categories']
        badge_text = meta['badge']
        pills_html = "".join([f'<span class="indication-pill">{ind}</span>' for ind in meta['indications']])
        wa_text = f"Hello Karmanya Ayurveda, I would like to inquire about {t_title} therapy."
        wa_url = "https://wa.me/919819820017?text=" + urllib.parse.quote(wa_text)
        
        t_img_html = f'<div class="treatment-interactive-thumb"><img src="{t_img}" alt="{t_title} at Karmanya Ayurveda" loading="lazy"><span class="treatment-badge-tag">{badge_text}</span></div>' if t_img else ''
        
        card = f"""
        <div class="treatment-interactive-card" data-categories="{cats}">
            {t_img_html}
            <div class="treatment-interactive-content">
                <div class="treatment-category-label">{t_category}</div>
                <h3 class="treatment-card-title"><a href="/treatments/{t_slug}/">{t_title}</a></h3>
                <p class="treatment-card-desc">{t_desc}</p>
                <div class="treatment-indications-wrap">
                    {pills_html}
                </div>
                <div class="treatment-card-actions">
                    <a href="/treatments/{t_slug}/" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.88rem;">Clinical Details &rarr;</a>
                    <a href="{wa_url}" target="_blank" rel="noopener" class="btn-wa-inquire">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="white" style="flex-shrink: 0;"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                        Inquire
                    </a>
                </div>
            </div>
        </div>
        """
        treat_grid_html += card
        
    treatments_hub_template = treatments_hub_template.replace('<!-- TREATMENTS_GRID_PLACEHOLDER -->', treat_grid_html)
    treatments_hub_template = treatments_hub_template.replace('{{seo_head_tags}}', generate_seo_head('treatments_hub', {}, site_data))
    for k, v in site_data['brand'].items():
        treatments_hub_template = treatments_hub_template.replace(f'{{{{brand.{k}}}}}', str(v))
        
    hub_treat_dir = os.path.join(base_dir, 'public', 'treatments')
    os.makedirs(hub_treat_dir, exist_ok=True)
    with open(os.path.join(hub_treat_dir, 'index.html'), 'w') as f:
        f.write(treatments_hub_template)

    # 5. Render Doctors
    with open(os.path.join(base_dir, 'templates', 'doctor.html'), 'r') as f:
        doc_template = f.read()
    for doc in doctors:
        data = {**doc, **site_data}
        data['seo_head_tags'] = generate_seo_head('doctor', doc, site_data)
        out_dir = os.path.join(base_dir, 'public', 'doctors', doc['slug'])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w') as f:
            f.write(render_template(doc_template, data))
            
    # 5b. Render Doctors Hub
    with open(os.path.join(base_dir, 'templates', 'doctors.html'), 'r') as f:
        doctors_hub_template = f.read()
    
    doctors_html = ""
    for doc in doctors:
        role_sub = doc['clinical'].get('role_subtitle', doc['title'])
        doc_html = f"""
        <div class="doctor-card" style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-8); margin-bottom: var(--space-8); box-shadow: var(--shadow-sm);">
            <div style="display: flex; gap: var(--space-6); align-items: flex-start; flex-wrap: wrap;">
                <div style="flex-shrink: 0;">
                    <img src="{doc['marketing']['image_url']}" alt="Photo of {doc['name']}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; object-position: top center; border: 3px solid var(--color-accent); display: block;">
                </div>
                <div style="flex: 1; min-width: 260px;">
                    <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;">STAFF PHYSICIAN &bull; {doc['clinical']['experience']}</div>
                    <h2 style="margin-bottom: 6px;"><a href="/doctors/{doc['slug']}/" style="color: var(--color-primary); text-decoration: none;">{doc['name']}</a></h2>
                    <p style="font-weight: 600; color: #555; margin-bottom: 12px;">{doc['qualifications']} &bull; {role_sub}</p>
                    <p style="font-size: 1.05rem; line-height: 1.6; color: #444; margin-bottom: 16px;">{doc['marketing']['hero_description']}</p>
                    <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
                        <a href="/doctors/{doc['slug']}/" class="btn btn-secondary" style="padding: 8px 18px; font-size: 0.9rem;">View Clinical Profile &rarr;</a>
                        <a href="/book-consultation/" class="btn btn-primary" style="padding: 8px 18px; font-size: 0.9rem;">Book Consultation</a>
                    </div>
                </div>
            </div>
        </div>
        """
        doctors_html += doc_html
    
    doctors_hub_template = doctors_hub_template.replace('<!-- DOCTORS_LOOP_PLACEHOLDER -->', doctors_html)
    doctors_hub_template = doctors_hub_template.replace('{{seo_head_tags}}', generate_seo_head('doctors_hub', {}, site_data))
    for k, v in site_data['brand'].items():
        doctors_hub_template = doctors_hub_template.replace(f'{{{{brand.{k}}}}}', str(v))

    hub_dir = os.path.join(base_dir, 'public', 'doctors')
    os.makedirs(hub_dir, exist_ok=True)
    with open(os.path.join(hub_dir, 'index.html'), 'w') as f:
        f.write(doctors_hub_template)

    # Render Our Story
    with open(os.path.join(base_dir, 'templates', 'our-story.html'), 'r') as f:
        story_template = f.read()
    out_dir = os.path.join(base_dir, 'public', 'our-story')
    os.makedirs(out_dir, exist_ok=True)
    site_data['seo_head_tags'] = '''<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NP2DTL98');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QWH0NSNLVE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-QWH0NSNLVE');
</script>
<title>Our Story & Founders | Dr. Anandhu & Dr. Aditya | Karmanya Ayurveda Pune</title>
<meta name="description" content="Discover the story of Karmanya Ayurveda in Pune. Founded by Dr. Anandhu & Dr. Aditya with a vision for authentic Kerala Ashtavaidya medicine, clinically led by resident staff physicians Dr. Irshad T.M. and Dr. Tejasvi Mulik.">
<link rel="canonical" href="https://karmanyaayurveda.com/our-story/">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#634119">
<meta property="og:title" content="Our Story & Founders | Dr. Anandhu & Dr. Aditya | Karmanya Ayurveda">
<meta property="og:description" content="How Dr. Anandhu & Dr. Aditya founded Karmanya Ayurveda to bring authentic Kerala Ashtavaidya Chikitsa to Pune, led by resident staff physicians Dr. Irshad T.M. and Dr. Tejasvi Mulik.">
<meta property="og:url" content="https://karmanyaayurveda.com/our-story/">
<meta property="og:type" content="article">
<meta property="og:image" content="https://karmanyaayurveda.com/images/brand-logo-square.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Our Story & Founders | Karmanya Ayurveda Pune">
<meta name="twitter:description" content="Authentic Kerala Ashtavaidya medicine founded by Dr. Anandhu & Dr. Aditya, clinically directed by Dr. Irshad T.M. & Dr. Tejasvi Mulik in Pimple Saudagar, Pune.">
<meta name="twitter:image" content="https://karmanyaayurveda.com/images/brand-logo-square.png">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "Our Story & Founders | Karmanya Ayurveda Chikitsalaya",
  "url": "https://karmanyaayurveda.com/our-story/",
  "mainEntity": {
    "@type": "MedicalClinic",
    "name": "Karmanya Ayurveda Chikitsalaya",
    "url": "https://karmanyaayurveda.com/",
    "telephone": "+91 98198 20017",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "27/11, Swaraj Garden Road, Near One Nation Apartment",
      "addressLocality": "Pimple Saudagar, Pimpri-Chinchwad, Pune",
      "addressRegion": "Maharashtra",
      "postalCode": "411027",
      "addressCountry": "IN"
    },
    "founder": [
      {
        "@type": "Person",
        "name": "Dr. Anandhu",
        "jobTitle": "Co-Founder",
        "description": "Co-founder of Karmanya Ayurveda, steeped in classical Kerala Ashtavaidya heritage with deep roots in Pune."
      },
      {
        "@type": "Person",
        "name": "Dr. Aditya",
        "jobTitle": "Co-Founder",
        "description": "Co-founder of Karmanya Ayurveda with a clinical dedication to authentic classical Panchakarma without commercial spa shortcuts."
      }
    ],
    "employee": [
      {
        "@type": "Physician",
        "name": "Dr. Irshad T.M.",
        "jobTitle": "Senior Staff Physician",
        "medicalSpecialty": ["Ayurvedic", "Panchakarma", "Nadi Pariksha", "Pain Management"],
        "description": "Senior resident physician with 15+ years of clinical experience in Ashtavaidya Kerala therapies."
      },
      {
        "@type": "Physician",
        "name": "Dr. Tejasvi Mulik",
        "jobTitle": "Staff Physician & Consultant",
        "medicalSpecialty": ["Ayurvedic", "Women's Health", "Metabolic Disorders"],
        "description": "Resident physician with 10+ years of clinical experience in pulse diagnosis and chronic disease management."
      }
    ]
  }
}
</script>'''
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(render_template(story_template, site_data))
        
    # Render Homepage

    # 6. Render Homepage & Book Consult
    with open(os.path.join(base_dir, 'templates', 'index.html'), 'r') as f:
        index_template = f.read()
    site_data['seo_head_tags'] = generate_seo_head('home', {}, site_data)
    with open(os.path.join(base_dir, 'public', 'index.html'), 'w') as f:
        f.write(render_template(index_template, site_data))
        
    with open(os.path.join(base_dir, 'templates', 'book-consultation.html'), 'r') as f:
        book_template = f.read()
    out_dir = os.path.join(base_dir, 'public', 'book-consultation')
    os.makedirs(out_dir, exist_ok=True)
    site_data['seo_head_tags'] = generate_seo_head('book', {}, site_data)
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(render_template(book_template, site_data))
            
    # 7. Generate Enhanced XML Sitemap
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url, priority, freq in urls_for_sitemap:
        sitemap_xml += f"""  <url>
    <loc>{url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""
    sitemap_xml += "</urlset>"
    with open(os.path.join(base_dir, 'public', 'sitemap.xml'), 'w') as f:
        f.write(sitemap_xml)
        
    with open(os.path.join(base_dir, 'public', 'robots.txt'), 'w') as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://karmanyaayurveda.com/sitemap.xml\n")

    # 7b. Generate Legacy Redirect Fallback Files
    legacy_redirects = {
        'panchakarma': '/treatments/panchakarma/',
        'kizhi': '/treatments/kizhi/',
        'dhara': '/treatments/shirodhara/',
        'about-karmanya-ayurveda': '/our-story/',
        'karmanya-health': '/',
        'contact-karmanya-ayurvedic': '/book-consultation/',
        'stress-management-program': '/conditions/stress-insomnia-anxiety/',
        'diabetes-management': '/conditions/digestive-metabolic-disorders/',
        'obesity-management': '/conditions/digestive-metabolic-disorders/',
        'pain-management': '/conditions/spine-sciatica-back-pain/',
        'spine-and-joint-care-program': '/conditions/spine-sciatica-back-pain/',
        'panchakarma-detoxification-program': '/treatments/panchakarma/',
        'hypertension-management': '/conditions/stress-insomnia-anxiety/',
        'ayurvedic-services-pune': '/treatments/',
        '2024': '/blog/',
        '2024/06/28': '/blog/',
        'monsoon-and-your-health-what-you-need-to-know-karkidakam-ayurveda': '/blog/',
        'nasya': '/treatments/nasya/',
        'pizhichil': '/treatments/pizhichil/',
        'netratarpana': '/treatments/netratarpana/',
        'netra-tarpana': '/treatments/netratarpana/',
        'urdvartana': '/treatments/udvartana/',
        'udvartana': '/treatments/udvartana/',
        'agnikarma': '/treatments/agnikarma/',
        'garbha-sanskar': '/treatments/garbha-sanskar/',
        'swedana': '/treatments/panchakarma/',
        'snehana': '/treatments/panchakarma/',
        'pichu': '/treatments/kati-basti/',
        'uzhichil': '/treatments/abhyangam/',
        'physiotherapy': '/treatments/kerala-chikitsa/',
        'thalam': '/treatments/shirodhara/',
        'dhumapanam': '/treatments/nasya/',
        'mukhalepam': '/treatments/mukhalepam/',
        'vidhakarma': '/treatments/agnikarma/',
        'viddhakarma': '/treatments/agnikarma/'
    }
    for slug, target in legacy_redirects.items():
        clean_slug = slug.strip('/')
        out_dir = os.path.join(base_dir, 'public', clean_slug)
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, 'index.html')
        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="https://karmanyaayurveda.com{target}">
  <title>Redirecting to Karmanya Ayurveda...</title>
  <script>window.location.replace("{target}");</script>
</head>
<body>
  <p>Redirecting to <a href="{target}">{target}</a>...</p>
</body>
</html>
'''
        with open(out_file, 'w') as f:
            f.write(html_content)

    # 8. Generate AI-SEO (llms.txt & llms-full.txt)
    llms_txt = """# Karmanya Ayurveda Chikitsalaya
> Authentic Ashtavaidya Kerala Ayurveda Treatment Centre in Pimple Saudagar, Pune.

## Clinic Overview
- Clinic Name: Karmanya Ayurveda Chikitsalaya
- Address: 27/11, Swaraj Garden Road, Near One Nation Apartment, Pimple Saudagar, Pimpri-Chinchwad, Pune, Maharashtra 411027
- Direct Phone: +91 98198 20017
- Timings: Monday to Sunday, 10:00 AM – 8:00 PM (Active OPD open 7 days a week)
- Consultation Fee: ₹500 only (Includes comprehensive Nadi Pariksha / pulse diagnosis, joint assessment, scan review; zero surprise charges)
- Google Review Rating: 4.9 / 5.0 Stars (Verified patient outcomes for spine, knee, and chronic care)

## Founders & Clinical Leadership
- Co-Founders: Dr. Anandhu & Dr. Aditya (Established Karmanya to bring authentic Kerala Ashtavaidya Chikitsa to Pune without commercial day-spa shortcuts)
- Senior Staff Physician: Dr. Irshad T.M., BAMS, MD (Ayurveda) — 15+ years of clinical experience in Kerala Ashtavaidya protocols & Panchakarma
- Staff Physician & Consultant: Dr. Tejasvi Mulik, BAMS — 10+ years of clinical experience in Nadi Pariksha, metabolic disorders, and women's health

## 20 Specialized Chronic Conditions Treated
1. Digestive & Metabolic: GERD / Acid Reflux, Chronic Constipation, Irritable Bowel Syndrome (IBS), Chronic Bloating, Type-2 Diabetes Management
2. Joint & Musculoskeletal: Knee Osteoarthritis (Janu Sandhigata Vata), Lower Back Pain (Kati Shula), Rheumatoid & Osteo Arthritis, Frozen Shoulder (Apabahuka)
3. Orthopedic & Nerve Decompression: Tennis Elbow, Carpal Tunnel Syndrome (Wrist Pain), Sciatica (Gridhrasi / Slip Disc), Cervical Spondylosis (Neck & Desk Strain)
4. Women's Health & Hormonal: Adenomyosis & Endometriosis, PCOS & PCOD, Uterine Fibroids, Infertility (Vandhyatva) & Garbha Sanskar
5. Dermatology & Neuro-Vascular: Psoriasis (Kitibha Kushta), Chronic Eczema (Vicharchika), Migraine & Tension Headaches (Ardhavabhedaka), Stress & Insomnia (Anidra)

## Classical Kerala Therapies Administered
- Nadi Pariksha: Traditional 3-finger radial pulse diagnosis for Dosha imbalance, Dhatu health, and metabolic root-cause mapping
- Panchakarma: Complete 5-fold classical detoxification (Vamana, Virechana, Basti, Nasya, Raktamokshana) under strict medical supervision
- Janu Basti: Classical warm medicated herbal oil reservoir over knee joints for cartilage restoration and synovial fluid nourishment
- Kati Basti: Medicated herbal oil pool on the lumbosacral junction for disc herniation and sciatica nerve decompression
- Griva Basti: Medicated herbal oil pool on the cervical spine for neck stiffness and cervical spondylosis
- Shirodhara: Continuous rhythmic stream of warm medicated herbal oil (or Takra) on the forehead for anxiety, insomnia, and nervous system reboot
- Kizhi (Patra Pinda & Churna Pinda Sweda): Medicated herbal poultices steamed in herbal decoctions for acute and chronic joint inflammation
- Pizhichil: King's therapy — warm medicated herbal oil bath combined with gentle synchronized strokes for neuromuscular rejuvenation
- Agnikarma: Precision thermal micro-cautery for immediate relief in chronic heel pain, calcaneal spurs, and tendonitis
- Mukhalepam: Classical Ayurvedic facial therapy with fresh herbal pastes (Manjistha, Lodhra, Chandan) for dermatological health
- Udvartana: Therapeutic herbal powder scrub for lymphatic drainage and metabolic fat breakdown
- Nasya: Medicated nasal administration of classical herbal drops for sinusitis, migraines, and cervical disorders
- Netratarpana: Medicated ghee pooling therapy for digital eye strain, dryness, and visual clarity

## Core Pages & Patient Resources
- Homepage: https://karmanyaayurveda.com/
- Our Story & Founders: https://karmanyaayurveda.com/our-story/
- Book Doctor Consultation (₹500): https://karmanyaayurveda.com/book-consultation/
- Verified Patient Reviews (4.9★): https://karmanyaayurveda.com/reviews/
- Clinical Treatments Directory: https://karmanyaayurveda.com/treatments/
- Chronic Conditions Directory: https://karmanyaayurveda.com/conditions/
- Doctor Profiles: https://karmanyaayurveda.com/doctors/
- Patient Education Blog: https://karmanyaayurveda.com/blog/
- Early Symptom Diagnostic Guides: https://karmanyaayurveda.com/symptoms/
- Treatment Comparisons (Ayurveda vs Modern Surgery): https://karmanyaayurveda.com/compare/
- Ayurvedic Medical Glossary: https://karmanyaayurveda.com/glossary/

## Geographic Location & Commute from Pune Neighborhoods
Single Flagship Facility: 27/11, Swaraj Garden Road, Near One Nation Apartment, Pimple Saudagar, Pune 411027
- Pimple Saudagar Clinic Hub: https://karmanyaayurveda.com/locations/pimple-saudagar/
- Wakad (3.2 km, ~8 mins): https://karmanyaayurveda.com/locations/wakad/
- Hinjawadi IT Park (7.5 km, ~15 mins): https://karmanyaayurveda.com/locations/hinjawadi/
- Baner (6.8 km, ~12 mins): https://karmanyaayurveda.com/locations/baner/
- Aundh (5.5 km, ~10 mins): https://karmanyaayurveda.com/locations/aundh/
- PCMC / Pimpri-Chinchwad (4.5 km, ~10 mins): https://karmanyaayurveda.com/locations/pcmc/
- Rahatani & Kalewadi (1.5 km, ~3 mins): https://karmanyaayurveda.com/locations/rahatani/
- Ravet & Punawale (7.8 km, ~14 mins): https://karmanyaayurveda.com/locations/ravet/
"""
    with open(os.path.join(base_dir, 'public', 'llms.txt'), 'w') as f:
        f.write(llms_txt)
    with open(os.path.join(base_dir, 'public', 'llms-full.txt'), 'w') as f:
        f.write(llms_txt)

    print("Successfully built all programmatic locations, conditions, treatments, doctors, sitemap, and AI-SEO assets!")

if __name__ == "__main__":
    build_site()
