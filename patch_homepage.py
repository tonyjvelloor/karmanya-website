import re
with open('public/index.html', 'r') as f:
    content = f.read()

# Replace homepage title
new_title = "Kerala Ayurvedic Clinic in Pune | Non-Surgical Joint & Spine Care | Karmanya Ayurveda"
content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)

with open('public/index.html', 'w') as f:
    f.write(content)
print("Homepage title patched!")
