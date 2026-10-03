import re

with open('build.py', 'r') as f:
    content = f.read()

injection = """        cond_list_html = ""
        for rc in treat.get('clinical', {}).get('resolved_conditions', []):
            cond_list_html += f'<li style="background: white; border: 1px solid var(--color-border); padding: 8px 16px; border-radius: 20px; font-size: 0.95rem;"><a href="{rc["url"]}" style="color: var(--color-primary); text-decoration: none; font-weight: 500;">{rc["name"]}</a></li>\\n'
        
        if 'clinical' not in data: data['clinical'] = {}
        if cond_list_html:
            data['clinical']['conditions_list'] = cond_list_html
        else:
            data['clinical']['conditions_list'] = '<li style="color: #666; font-size: 0.95rem;">Consult physician for specific indications.</li>'

        out_dir = os.path.join(base_dir, 'public', 'treatments', treat['slug'])"""

content = content.replace("        out_dir = os.path.join(base_dir, 'public', 'treatments', treat['slug'])", injection)

with open('build.py', 'w') as f:
    f.write(content)

