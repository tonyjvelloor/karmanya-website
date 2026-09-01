import json
import os
import sys

def render_template(template_str, data):
    import re
    
    # Simple list logic for {{#array}}...{{/array}}
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
                # If item is a string/primitive, we need a way to reference it.
                # We'll use {{.}} as a special token for primitive list items.
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
        errors.append(f"Missing seo.meta_title in {page['id']}")
    if 'seo' not in page or 'meta_description' not in page['seo']:
        errors.append(f"Missing seo.meta_description in {page['id']}")
    if 'safety' not in page:
        errors.append(f"Missing safety block in {page['id']}")
    elif 'emergency_rule' not in page['safety']:
        errors.append(f"Missing safety.emergency_rule in {page['id']}")
    if page_type == 'condition' and 'disclaimer' not in page.get('safety', {}):
        errors.append(f"Missing safety.disclaimer in condition {page['id']}")
    if page_type == 'treatment' and 'suitability' not in page.get('safety', {}):
        errors.append(f"Missing safety.suitability in treatment {page['id']}")
    if 'metadata' not in page or 'reviewed_by' not in page['metadata']:
        errors.append(f"Missing metadata.reviewed_by in {page['id']}")
    return errors

def build_site():
    base_dir = "/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website"
    
    # 0. Governance Check
    claims_errors = validate_claims(os.path.join(base_dir, 'data', 'claims.json'))
    if claims_errors:
        print("BUILD FAILED: Content Governance Violations")
        for err in claims_errors:
            print(f" - {err}")
        sys.exit(1)
    
    import shutil
    
    # 1. Load Data
    with open(os.path.join(base_dir, 'data', 'site.json'), 'r') as f:
        site_data = json.load(f)
    with open(os.path.join(base_dir, 'data', 'conditions.json'), 'r') as f:
        conditions = json.load(f)
    with open(os.path.join(base_dir, 'data', 'treatments.json'), 'r') as f:
        treatments = json.load(f)
    with open(os.path.join(base_dir, 'data', 'doctors.json'), 'r') as f:
        doctors = json.load(f)
        
    treat_dict = {t['id']: t for t in treatments}
    
    all_errors = []
    urls_for_sitemap = [
        'https://karmanyaayurveda.com/',
        'https://karmanyaayurveda.com/book-consultation/'
    ]
    
    # Copy Static Assets
    css_src = os.path.join(base_dir, 'css')
    css_dest = os.path.join(base_dir, 'public', 'css')
    if os.path.exists(css_dest):
        shutil.rmtree(css_dest)
    shutil.copytree(css_src, css_dest)
    
    img_src = os.path.join(base_dir, 'images')
    img_dest = os.path.join(base_dir, 'public', 'images')
    if os.path.exists(img_dest):
        shutil.rmtree(img_dest)
    if os.path.exists(img_src):
        shutil.copytree(img_src, img_dest)
    
    # Validate and Resolve
    for cond in conditions:
        urls_for_sitemap.append(f"https://karmanyaayurveda.com/conditions/{cond['slug']}/")
        all_errors.extend(validate_page(cond, 'condition'))
        resolved_treatments = []
        for t_id in cond.get('clinical', {}).get('related_treatments', []):
            if t_id in treat_dict:
                t = treat_dict[t_id]
                resolved_treatments.append({"name": t['title'], "url": f"/treatments/{t['slug']}/"})
        cond['clinical']['resolved_treatments'] = resolved_treatments

    for treat in treatments:
        urls_for_sitemap.append(f"https://karmanyaayurveda.com/treatments/{treat['slug']}/")
        all_errors.extend(validate_page(treat, 'treatment'))
        
    for doc in doctors:
        urls_for_sitemap.append(f"https://karmanyaayurveda.com/doctors/{doc['slug']}/")
        all_errors.extend(validate_page(doc, 'doctor'))

    if all_errors:
        print("BUILD FAILED: Validation Errors")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)
        
    print("Governance passed. Validation passed. Rendering expanded pages...")
    
    # 2. Render Conditions
    import re
    if os.path.exists(os.path.join(base_dir, 'templates', 'condition.html')):
        with open(os.path.join(base_dir, 'templates', 'condition.html'), 'r') as f:
            condition_template = f.read()
        for cond in conditions:
            html = condition_template
            # Global brand
            for k, v in site_data['brand'].items():
                html = html.replace(f'{{{{brand.{k}}}}}', str(v))
            
            # Condition specific
            for k, v in cond.items():
                if isinstance(v, str):
                    html = html.replace(f'{{{{condition.{k}}}}}', str(v))
                elif isinstance(v, dict) and k == 'safety':
                    for sk, sv in v.items():
                        html = html.replace(f'{{{{safety.{sk}}}}}', str(sv))
                        
            # Handle Therapy loops
            therapy_list_html = ""
            for t_id in cond.get('recommended_therapies', []):
                if t_id in treat_dict:
                    t = treat_dict[t_id]
                    therapy_list_html += f"<li><strong><a href='/treatments/{t['slug']}/'>{t['name']}</a>:</strong> {t['description']}</li>"
            html = re.sub(r'{{#recommended_therapies}}.*?{{/recommended_therapies}}', therapy_list_html, html, flags=re.DOTALL)
            
            # Handle FAQs loops
            if 'faqs' in cond and cond['faqs']:
                faq_html = ""
                schema_faqs = []
                for f_item in cond['faqs']:
                    q = f_item['question']
                    a = f_item['answer']
                    faq_html += f'<div style="padding: var(--space-6) 0; border-bottom: 1px solid var(--color-border);"><h4 style="font-size: 1.25rem; font-family: var(--font-body); font-weight: 600; margin-bottom: var(--space-2); color: var(--color-primary);">{q}</h4><p style="margin-bottom: 0; color: #555;">{a}</p></div>'
                    schema_faqs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
                
                # Generate FAQ Schema
                faq_schema = json.dumps({
                    "@context": "https://schema.org",
                    "@type": "FAQPage",
                    "mainEntity": schema_faqs
                })
                html = html.replace('</head>', f'<script type="application/ld+json">{faq_schema}</script>\n</head>')
                
                # Replace the {{#faqs}} loop block
                html = re.sub(r'{{#faqs}}.*?{{question}}.*?{{answer}}.*?{{/faqs}}', faq_html, html, flags=re.DOTALL)
            else:
                html = re.sub(r'{{#faqs}}.*?{{/faqs}}', '', html, flags=re.DOTALL)

            cond_dir = os.path.join(base_dir, 'public', 'conditions', cond['slug'])
            os.makedirs(cond_dir, exist_ok=True)
            with open(os.path.join(cond_dir, 'index.html'), 'w') as f:
                f.write(html)
            
    # 3. Render Treatments
    with open(os.path.join(base_dir, 'templates', 'treatment.html'), 'r') as f:
        treat_template = f.read()
    for treat in treatments:
        # Resolve related conditions
        resolved_conditions = []
        for c_id in treat.get('clinical', {}).get('related_conditions', []):
            for c in conditions:
                if c['slug'] == c_id or c['id'] == c_id:
                    resolved_conditions.append({'name': c.get('condition_name', c_id), 'url': f"/conditions/{c['slug']}/"})
                    break
        
        data = {**treat, **site_data}
        if 'clinical' in data:
            data['clinical']['related_conditions'] = resolved_conditions
            
        out_dir = os.path.join(base_dir, 'public', 'treatments', treat['slug'])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w') as f:
            f.write(render_template(treat_template, data))
            
    # 4. Render Doctors
    with open(os.path.join(base_dir, 'templates', 'doctor.html'), 'r') as f:
        doc_template = f.read()
    for doc in doctors:
        data = {**doc, **site_data}
        out_dir = os.path.join(base_dir, 'public', 'doctors', doc['slug'])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w') as f:
            f.write(render_template(doc_template, data))
            
    # 5. Render Homepage & Book Consult
    with open(os.path.join(base_dir, 'templates', 'index.html'), 'r') as f:
        index_template = f.read()
    with open(os.path.join(base_dir, 'public', 'index.html'), 'w') as f:
        f.write(render_template(index_template, site_data))
        
    with open(os.path.join(base_dir, 'templates', 'book-consultation.html'), 'r') as f:
        book_template = f.read()
    out_dir = os.path.join(base_dir, 'public', 'book-consultation')
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(render_template(book_template, site_data))
            
    # 6. Generate SEO Assets
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls_for_sitemap:
        sitemap_xml += f"  <url>\n    <loc>{url}</loc>\n  </url>\n"
    sitemap_xml += "</urlset>"
    with open(os.path.join(base_dir, 'public', 'sitemap.xml'), 'w') as f:
        f.write(sitemap_xml)
        
    with open(os.path.join(base_dir, 'public', 'robots.txt'), 'w') as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://karmanyaayurveda.com/sitemap.xml\n")

    print("Successfully built the expanded site and SEO assets!")

if __name__ == "__main__":
    build_site()
