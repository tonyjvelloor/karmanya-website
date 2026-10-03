import os
import re

directories = [
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/templates',
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/data'
]

for base_dir in directories:
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.json'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                    
                # Revert logo.webp to logo.png
                content = content.replace('logo.webp', 'logo.png')
                
                with open(filepath, 'w') as f:
                    f.write(content)
                    
print("Reverted logo.webp to logo.png in templates and data.")
