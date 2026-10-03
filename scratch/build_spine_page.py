import os
import sys
import json

sys.path.append('.')
from build import generate_seo_head

with open('data/site.json', 'r') as f:
    site_data = json.load(f)

with open('templates/spine-care-program.html', 'r') as f:
    html = f.read()
    
# Mock page data for the landing page
page_data = {
    'title': 'Spine & Sciatica Care Program | Avoid Surgery | Karmanya Ayurveda',
    'excerpt': 'Clinically proven Ayurvedic Spine Care Program in Pune. Natural sciatica relief, slip disc treatment without surgery.',
    'image_url': 'https://karmanyaayurveda.com/images/protocols/protocol-spine-kati-basti.webp'
}

# Generate SEO tags
seo_tags = generate_seo_head(
    page_type='treatment',
    page_data=page_data,
    site_data=site_data
)

seo_tags = seo_tags.replace('href="https://karmanyaayurveda.com/"', 'href="https://karmanyaayurveda.com/spine-care-program/"')

html = html.replace('{{seo_head_tags}}', seo_tags)

os.makedirs('public/spine-care-program', exist_ok=True)

with open('public/spine-care-program/index.html', 'w') as f:
    f.write(html)
    
print("Successfully built public/spine-care-program/index.html")
