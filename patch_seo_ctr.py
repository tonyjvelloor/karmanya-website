import json

# Update Conditions
with open('data/conditions.json', 'r') as f:
    conditions = json.load(f)

for c in conditions:
    if c['id'] == 'knee-joint-pain':
        c['seo']['meta_title'] = "Avoid Surgery: Ayurvedic Knee Pain Treatment in Pune | ₹500 Consult"
        c['seo']['meta_description'] = "Before considering knee replacement surgery, consult our BAMS specialists in Pimple Saudagar for a ₹500 non-surgical Kerala Ayurveda assessment."
    elif c['id'] == 'spine-sciatica-back-pain':
        c['seo']['meta_title'] = "Non-Surgical Sciatica & Back Pain Treatment in Pune | Kerala Ayurveda"
        c['seo']['meta_description'] = "Avoid spinal surgery and painkillers. Discover authentic Kerala Panchakarma therapies (Kati Basti) for slipped disc, sciatica, and chronic back pain."

with open('data/conditions.json', 'w') as f:
    json.dump(conditions, f, indent=2)

# Update site.json (Homepage)
with open('data/site.json', 'r') as f:
    site = json.load(f)

site['meta']['title'] = "Kerala Ayurvedic Clinic in Pune | Non-Surgical Joint & Spine Care"
site['meta']['description'] = "Karmanya Ayurveda in Pimple Saudagar specializes in non-surgical treatment for knee pain, sciatica, and slipped disc using authentic Kerala Panchakarma therapies. Book your ₹500 consult today."

with open('data/site.json', 'w') as f:
    json.dump(site, f, indent=2)

print("CTR-focused SEO metadata applied!")
