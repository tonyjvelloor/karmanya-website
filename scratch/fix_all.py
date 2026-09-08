import os
import json
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(os.path.join(base_dir, 'build.py'), 'r') as f:
    build_py = f.read()

# Let's fix build.py by replacing the condition rendering logic
condition_logic_old = """    # 3. Render Conditions
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

        cond_dir = os.path.join(base_dir, 'public', 'conditions', cond['slug'])
        os.makedirs(cond_dir, exist_ok=True)
        with open(os.path.join(cond_dir, 'index.html'), 'w') as f:
            f.write(html)"""

condition_logic_new = """    # 3. Render Conditions
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
            f.write(render_template(condition_template, data))"""

if condition_logic_old in build_py:
    build_py = build_py.replace(condition_logic_old, condition_logic_new)
else:
    # use regex
    build_py = re.sub(
        r'    # 3\. Render Conditions.*?f\.write\(html\)',
        condition_logic_new,
        build_py,
        flags=re.DOTALL
    )

with open(os.path.join(base_dir, 'build.py'), 'w') as f:
    f.write(build_py)

# Now fix condition.html to have the mustache block back
with open(os.path.join(base_dir, 'templates', 'condition.html'), 'r') as f:
    cond_html = f.read()

# we previously put {{clinical.treatments_list}}
cond_html = cond_html.replace('{{clinical.treatments_list}}', '''{{#clinical.resolved_treatments}}
                    <li>
                        <h4><a href="{{url}}">{{name}}</a></h4>
                    </li>
                    {{/clinical.resolved_treatments}}''')
                    
with open(os.path.join(base_dir, 'templates', 'condition.html'), 'w') as f:
    f.write(cond_html)

print("done")
