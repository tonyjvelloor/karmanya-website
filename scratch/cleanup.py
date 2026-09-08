import re

with open('templates/condition.html', 'r') as f:
    html = f.read()

# 1. Remove unresolved treatments block
html = re.sub(r'\{\{#clinical\.resolved_treatments\}\}.*?\{\{/clinical\.resolved_treatments\}\}', '', html, flags=re.DOTALL)

# 2. Remove the old FAQ block
html = re.sub(r'<!-- FAQs -->\s*\{\{#faqs\}\}.*?\{\{/faqs\}\}', '', html, flags=re.DOTALL)
# It seems the closing tag might be further down, let's just do a greedy replace for the faq section
html = re.sub(r'<!-- FAQs -->.*?\{\{/faqs\}\}', '', html, flags=re.DOTALL)

with open('templates/condition.html', 'w') as f:
    f.write(html)

print("condition.html cleaned")
