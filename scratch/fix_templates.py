import re

# Fix condition.html
with open('templates/condition.html', 'r') as f:
    content = f.read()

pattern_cond = re.compile(r'\{\{#clinical\.resolved_treatments\}\}.*?\{\{/clinical\.resolved_treatments\}\}', re.DOTALL)
content = pattern_cond.sub('{{clinical.treatments_list}}', content)

with open('templates/condition.html', 'w') as f:
    f.write(content)

# Fix treatment.html
with open('templates/treatment.html', 'r') as f:
    content = f.read()

pattern_treat = re.compile(r'\{\{#clinical\.related_conditions\}\}.*?\{\{/clinical\.related_conditions\}\}', re.DOTALL)
content = pattern_treat.sub('{{clinical.conditions_list}}', content)

with open('templates/treatment.html', 'w') as f:
    f.write(content)

print("Templates fixed.")
