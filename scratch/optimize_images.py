import os
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/templates'

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
                
            # Replace .jpg and .png with .webp for image sources
            # But only for paths starting with /images/
            content = re.sub(r'src="(/images/[^"]+)\.(jpg|png)"', r'src="\1.webp"', content)
            
            with open(filepath, 'w') as f:
                f.write(content)
                
# Do the same for data JSONs just in case they reference JPGs
data_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/data'
for root, _, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.json'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            content = re.sub(r'(/images/[^"]+)\.(jpg|png)', r'\1.webp', content)
            with open(filepath, 'w') as f:
                f.write(content)
                
print("HTML templates and data JSONs updated to use WebP formats!")
