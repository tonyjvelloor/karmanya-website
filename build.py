import json
import os
import sys
import shutil
import re

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
    image = "https://karmanyaayurveda.com/images/doctor-consult.jpg"
    
    breadcrumbs = []
    entity_schema = None
    faq_schema = None
    
    if page_type == 'home':
        title = f"Ayurvedic Clinic in Pimple Saudagar, Pune | {brand.get('name')}"
        desc = "Authentic Kerala Ayurvedic clinic in Pimple Saudagar, Pune. Physician-led Panchakarma, non-surgical knee joint pain, sciatica spine care, and holistic wellness."
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
                "https://www.google.com/search?q=karmanya+ayurveda+address&ludocid=3077549578320836260"
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
            "url": url
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
                "name": brand.get('name'),
                "url": "https://karmanyaayurveda.com/"
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
        title = f"Book Ayurvedic Consultation in Pimple Saudagar, Pune | {brand.get('name')}"
        desc = "Schedule your in-depth pulse diagnosis (Nadi Pariksha) consultation with our experienced Ayurvedic physicians in Pimple Saudagar, Pune."
        url = "https://karmanyaayurveda.com/book-consultation/"
        
        breadcrumbs = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karmanyaayurveda.com/"},
            {"@type": "ListItem", "position": 2, "name": "Book Consultation", "item": url}
        ]

    # Compile HTML & GEO Meta Tags
    html_tags = f"""
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    
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
        ('https://karmanyaayurveda.com/treatments/', '0.9', 'weekly'),
        ('https://karmanyaayurveda.com/conditions/', '0.9', 'weekly'),
        ('https://karmanyaayurveda.com/doctors/', '0.9', 'monthly'),
        ('https://karmanyaayurveda.com/locations/', '0.9', 'weekly'),
        ('https://karmanyaayurveda.com/book-consultation/', '0.8', 'monthly')
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
        loc_card = f"""
        <div class="location-card">
            <div>
                <span style="color: var(--color-accent); font-weight: 600; font-size: 0.85rem; text-transform: uppercase;">Distance: {loc['transit']['distance']}</span>
                <h3 style="margin: 8px 0 12px; font-size: 1.6rem;"><a href="/locations/{loc['slug']}/" style="color: var(--color-primary); text-decoration: none;">{loc['name']}</a></h3>
                <p style="color: #555; font-size: 1rem; line-height: 1.5; margin-bottom: 16px;">{loc['hero']['lead'][:180]}...</p>
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
        html = condition_template
        cond['seo_head_tags'] = generate_seo_head('condition', cond, site_data)
        for k, v in site_data['brand'].items():
            html = html.replace(f'{{{{brand.{k}}}}}', str(v))
        
        html = html.replace("{{seo_head_tags}}", cond.get("seo_head_tags", ""))
        html = html.replace("{{marketing.hero_eyebrow}}", cond.get('marketing', {}).get('hero_eyebrow', ''))
        html = html.replace("{{marketing.hero_title}}", cond.get('marketing', {}).get('hero_title', ''))
        html = html.replace("{{marketing.hero_description}}", cond.get('marketing', {}).get('hero_description', ''))
        html = html.replace("{{title}}", cond.get('title', ''))
        html = html.replace("{{condition.title}}", cond.get('title', ''))
        html = html.replace("{{metadata.reviewed_by}}", cond.get('metadata', {}).get('reviewed_by', 'Dr. Irshad T.M.'))
        html = html.replace("{{metadata.reviewed_date}}", cond.get('metadata', {}).get('reviewed_date', 'September 2026'))
        html = html.replace("{{metadata.doctor_url}}", cond.get('metadata', {}).get('doctor_url', '/doctors/dr-irshad/'))
        html = html.replace("{{clinical.ayurvedic_perspective}}", cond.get('clinical', {}).get('ayurvedic_perspective', ''))
        html = html.replace("{{clinical.assessment_process}}", cond.get('clinical', {}).get('assessment_process', ''))
        html = html.replace("{{safety.disclaimer}}", cond.get('safety', {}).get('disclaimer', ''))
        html = html.replace("{{safety.emergency_rule}}", cond.get('safety', {}).get('emergency_rule', ''))
        
        # Handle Therapy loops
        therapy_list_html = ""
        for t in cond.get('clinical', {}).get('resolved_treatments', []):
            therapy_list_html += f"<li><h4><a href='{t['url']}'>{t['name']}</a></h4></li>"
        html = html.replace('<!-- THERAPY_SECTION_PLACEHOLDER -->', f'<ul class="treatment-list">{therapy_list_html}</ul>' if therapy_list_html else '')
        html = re.sub(r'{{#recommended_therapies}}.*?{{/recommended_therapies}}', therapy_list_html, html, flags=re.DOTALL)
        
        # Handle Doctor loops
        doctor_list_html = ""
        for doc in cond.get('clinical', {}).get('resolved_doctors', []):
            doctor_list_html += f"<li><h4><a href='{doc['url']}'>{doc['name']}</a></h4><p>{doc['title']}</p></li>"
        
        if doctor_list_html:
            doctor_section = f'<div class="content-section"><h2>Our Specialists</h2><ul class="treatment-list">{doctor_list_html}</ul></div>'
        else:
            doctor_section = ""
        html = html.replace('<!-- DOCTOR_SECTION_PLACEHOLDER -->', doctor_section)

        # Handle FAQs
        faq_html = ""
        for faq in cond.get('faqs', []):
            faq_html += f"""
            <div class="faq-accordion">
                <button class="faq-question">{faq['question']}</button>
                <div class="faq-answer">
                    <p>{faq['answer']}</p>
                </div>
            </div>"""
        html = re.sub(r'{{#faqs}}.*?{{/faqs}}', faq_html, html, flags=re.DOTALL)
        html = html.replace('<!-- FAQS_LOOP_PLACEHOLDER -->', faq_html)

        cond_dir = os.path.join(base_dir, 'public', 'conditions', cond['slug'])
        os.makedirs(cond_dir, exist_ok=True)
        with open(os.path.join(cond_dir, 'index.html'), 'w') as f:
            f.write(html)
            
    # 3b. Render Conditions Directory Hub
    with open(os.path.join(base_dir, 'templates', 'conditions.html'), 'r') as f:
        conditions_hub_template = f.read()
        
    cond_grid_html = ""
    for c in conditions:
        card = f"""
        <div class="condition-card">
            <div>
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
        out_dir = os.path.join(base_dir, 'public', 'treatments', treat['slug'])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w') as f:
            f.write(render_template(treat_template, data))
            
    # 4b. Render Treatments Directory Hub
    with open(os.path.join(base_dir, 'templates', 'treatments.html'), 'r') as f:
        treatments_hub_template = f.read()
        
    treat_grid_html = ""
    for t in treatments:
        card = f"""
        <div class="treatment-card">
            <div>
                <span style="color: var(--color-accent); font-weight: 600; font-size: 0.85rem; text-transform: uppercase;">{t['category']}</span>
                <h3 style="margin: 8px 0 12px; font-size: 1.6rem;"><a href="/treatments/{t['slug']}/" style="color: var(--color-primary); text-decoration: none;">{t['title']}</a></h3>
                <p style="color: #555; font-size: 1rem; line-height: 1.5; margin-bottom: 16px;">{t['marketing']['hero_description']}</p>
            </div>
            <div style="margin-top: 16px;">
                <a href="/treatments/{t['slug']}/" class="btn btn-secondary" style="padding: 8px 18px; font-size: 0.9rem;">View Therapy Details &rarr;</a>
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
                <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--color-primary); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-family: var(--font-heading); font-size: 1.6rem; font-weight: 700; flex-shrink: 0;">
                    Dr
                </div>
                <div style="flex: 1; min-width: 260px;">
                    <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;">SENIOR CONSULTANT &bull; {doc['clinical']['experience']}</div>
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

    # 8. Generate AI-SEO (llms.txt & llms-full.txt)
    llms_txt = """# Karmanya Ayurveda Chikitsalaya
> Authentic Ashtavaidya Kerala Ayurveda in Pimple Saudagar, Pune.

## Clinic Overview
- Name: Karmanya Ayurveda Chikitsalaya
- Location: 27/11, Swaraj Garden Road, Near One Nation Apartment, Pimple Saudagar, Pune, Maharashtra 411027
- Phone: +91 98198 20017
- Timings: Monday to Sunday, 10:00 AM – 8:00 PM
- Chief Physician: Dr. Irshad T.M., BAMS, MD (Ayurveda) - 15+ years experience
- Senior Consultant: Dr. Tejasvi Mulik, BAMS - 10+ years experience

## Core Clinical Specialties
- Knee & Joint Pain (Janu Sandhigata Vata): Non-surgical management, Janu Basti, avoiding knee replacement.
- Spine & Sciatica (Gridhrasi / Slip Disc): Kati Basti, nerve decompression, posture rehabilitation.
- Cervical Spondylosis (Neck & Desk Strain): Griva Basti, Nasya, ergonomic strain relief.
- Women's Hormonal Health (PCOS/PCOD): Cycle regulation, fertility support, metabolic balancing.
- Chronic Dermatology (Psoriasis & Eczema): Blood purification (Raktaprasadana), Takradhara.
- Digestive Health (IBS & Acid Peptic Disease): Agni rekindling, gut barrier repair.
- Stress, Anxiety & Insomnia: Kerala Shirodhara, restorative nervous system therapy.

## Authentic Kerala Therapies Provided
- Panchakarma (5-fold classical detoxification)
- Janu Basti (Warm medicated oil pooling on knee joints)
- Kati Basti (Warm medicated oil pooling on lumbar spine)
- Shirodhara (Rhythmic warm herbal oil stream on forehead)
- Kizhi / Patra Pinda Sweda (Medicated herbal leaf boluses)
- Abhyangam (Synchronized full-body therapeutic oil massage)
- Pizhichil & Njavarakizhi (Signature Ashtavaidya immersion therapies)

## Physical Location (Single Facility)
- Single Clinic Address: 27/11, Swaraj Garden Road, Near One Nation Apartment, Pimple Saudagar, Pimpri-Chinchwad, Pune, Maharashtra 411027
- Notice: Karmanya operates exclusively from this single clinic in Pimple Saudagar. We do NOT operate branch dispensaries. Patients travel to our Pimple Saudagar centre from surrounding areas across West Pune.

## Commute Guides from Nearby Areas
- Pimple Saudagar (Flagship Clinic): https://karmanyaayurveda.com/locations/pimple-saudagar/
- Wakad (3.2 km, 8 mins away): https://karmanyaayurveda.com/locations/wakad/
- Hinjawadi IT Park (7.5 km, 15 mins away): https://karmanyaayurveda.com/locations/hinjawadi/
- Baner (6.8 km, 12 mins away): https://karmanyaayurveda.com/locations/baner/
- Aundh (5.5 km, 10 mins away): https://karmanyaayurveda.com/locations/aundh/
- Pimpri-Chinchwad / PCMC (4.5 km away): https://karmanyaayurveda.com/locations/pcmc/
- Rahatani & Kalewadi (1.5 km, 3 mins away): https://karmanyaayurveda.com/locations/rahatani/
- Ravet & Punawale (7.8 km, 14 mins away): https://karmanyaayurveda.com/locations/ravet/

## Website Directory
- Main Website: https://karmanyaayurveda.com/
- Treatments Directory: https://karmanyaayurveda.com/treatments/
- Conditions Directory: https://karmanyaayurveda.com/conditions/
- Doctors Directory: https://karmanyaayurveda.com/doctors/
- Service Areas: https://karmanyaayurveda.com/locations/
- Book Consultation: https://karmanyaayurveda.com/book-consultation/
"""
    with open(os.path.join(base_dir, 'public', 'llms.txt'), 'w') as f:
        f.write(llms_txt)
    with open(os.path.join(base_dir, 'public', 'llms-full.txt'), 'w') as f:
        f.write(llms_txt)

    print("Successfully built all programmatic locations, conditions, treatments, doctors, sitemap, and AI-SEO assets!")

if __name__ == "__main__":
    build_site()
