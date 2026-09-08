import re

with open('templates/doctor.html', 'r') as f:
    content = f.read()

pattern = re.compile(r'\{\{#clinical\.specialties\}\}.*?\{\{/clinical\.specialties\}\}', re.DOTALL)
content = pattern.sub('{{clinical.specialties_list}}', content)

with open('templates/doctor.html', 'w') as f:
    f.write(content)

print("Doctor template fixed.")
