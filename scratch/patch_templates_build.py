import re

for filename in ['templates/condition.html', 'templates/treatment.html']:
    with open(filename, 'r') as f:
        content = f.read()
    
    # insert {{faqs_html}} before the Medical Notice block
    pattern = r'(<div class="content-section" style="background-color: var\(--color-bg\);">\s*<span class="eyebrow">Medical Notice</span>)'
    if '{{faqs_html}}' not in content:
        new_content = re.sub(pattern, r'{{faqs_html}}\n\n            \1', content)
        with open(filename, 'w') as f:
            f.write(new_content)

with open('build.py', 'r') as f:
    build_content = f.read()

faq_builder_cond = """
        # Build FAQs
        faqs_html = ''
        if 'faqs' in c:
            faqs_html += '<div class="content-section"><h2>Frequently Asked Questions</h2><div class="faq-list">'
            for faq in c['faqs']:
                faqs_html += f'''
                <div class="faq-item" style="border-bottom: 1px solid var(--color-border); padding: 16px 0;">
                    <h3 class="faq-question" style="font-size: 1.1rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; margin:0; color:var(--color-primary);">
                        {faq['question']}
                        <span style="color:var(--color-accent); font-weight:bold;">+</span>
                    </h3>
                    <div class="faq-answer" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease-out;">
                        <p style="color: #555; margin-top:12px; margin-bottom:4px;">{faq['answer']}</p>
                    </div>
                </div>'''
            faqs_html += '</div></div>'
            
            # Update schema
            schema_type = schema.get('@type', 'MedicalCondition')
            if isinstance(schema_type, list):
                if 'FAQPage' not in schema_type:
                    schema_type.append('FAQPage')
            else:
                schema_type = [schema_type, 'FAQPage']
            schema['@type'] = schema_type
            
            if 'mainEntity' not in schema:
                schema['mainEntity'] = []
                
            for faq in c['faqs']:
                schema['mainEntity'].append({
                    "@type": "Question",
                    "name": faq['question'],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq['answer']
                    }
                })
        html = html.replace('{{faqs_html}}', faqs_html)
"""

faq_builder_treat = faq_builder_cond.replace("in c:", "in t:").replace("c['faqs']", "t['faqs']")

# We need to inject this right before html = html.replace('</body>', ... + json.dumps(schema))
# Let's find a reliable anchor point
build_content = re.sub(
    r"(        html = html\.replace\('</body>', f'<script type=\"application/ld\+json\">\n\{json\.dumps\(schema, indent=2\)\}\n</script>\n</body>'\))",
    lambda m: faq_builder_cond + "\n" + m.group(1),
    build_content,
    count=1 # condition
)

build_content = re.sub(
    r"(        html = html\.replace\('</body>', f'<script type=\"application/ld\+json\">\n\{json\.dumps\(schema, indent=2\)\}\n</script>\n</body>'\))",
    lambda m: faq_builder_treat + "\n" + m.group(1),
    build_content,
    count=1 # treatment
)

with open('build.py', 'w') as f:
    f.write(build_content)

print("build.py and templates updated.")
