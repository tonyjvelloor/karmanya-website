import os
import sys
import json

sys.path.append('.')
from build import generate_seo_head

with open('data/site.json', 'r') as f:
    site_data = json.load(f)

with open('templates/knee-pain-care-program.html', 'r') as f:
    html = f.read()
    
# Mock page data for the landing page
page_data = {
    'title': 'Knee Cushion Regeneration Program | Avoid Surgery | Karmanya Ayurveda',
    'excerpt': 'Clinically proven Ayurvedic Knee Care Program in Pune. Natural cartilage regeneration, reduce joint pain & stiffness without surgery.',
    'image_url': 'https://karmanyaayurveda.com/images/protocols/protocol-knee-janu-basti.webp'
}

# Generate SEO tags
seo_tags = generate_seo_head(
    page_type='treatment',
    page_data=page_data,
    site_data=site_data
)

# Overwrite canonical since it defaults to treatment.html slug mapping
seo_tags = seo_tags.replace('href="https://karmanyaayurveda.com/"', 'href="https://karmanyaayurveda.com/knee-pain-care-program/"')

html = html.replace('{{seo_head_tags}}', seo_tags)

os.makedirs('public/knee-pain-care-program', exist_ok=True)

with open('public/knee-pain-care-program/index.html', 'w') as f:
    f.write(html)
    
print("Successfully built public/knee-pain-care-program/index.html")
