import os
from PIL import Image

image_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/images'
png_files = ['logo.png', 'brand-logo-square.png', 'brand-emblem-square.png']

for file in png_files:
    original_path = os.path.join(image_dir, file)
    if os.path.exists(original_path):
        base_name = os.path.splitext(file)[0]
        webp_path = os.path.join(image_dir, base_name + '.webp')
        
        try:
            with Image.open(original_path) as img:
                # Do NOT convert to RGB. Keep RGBA for transparency.
                img.save(webp_path, 'webp', quality=80)
            print(f"Fixed transparency for: {base_name}.webp")
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

