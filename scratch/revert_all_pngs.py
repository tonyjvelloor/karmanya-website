import os
import re

directories = [
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/templates',
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/data'
]

png_files = ['logo', 'brand-logo-square', 'brand-emblem-square']

for base_dir in directories:
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.json'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                    
                for png in png_files:
                    content = content.replace(f'{png}.webp', f'{png}.png')
                
                with open(filepath, 'w') as f:
                    f.write(content)
                    
print("Reverted all transparent PNGs.")
