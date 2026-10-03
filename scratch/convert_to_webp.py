import os
from PIL import Image

image_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/images'
converted_count = 0

for root, _, files in os.walk(image_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            original_path = os.path.join(root, file)
            # Create the webp filename
            base_name = os.path.splitext(file)[0]
            webp_path = os.path.join(root, base_name + '.webp')
            
            # Skip if webp already exists
            if os.path.exists(webp_path):
                continue
                
            try:
                with Image.open(original_path) as img:
                    img = img.convert('RGB') if img.mode == 'RGBA' and file.lower().endswith('.png') else img
                    img.save(webp_path, 'webp', quality=80)
                print(f"Converted: {file} -> {base_name}.webp")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {file}: {e}")

print(f"Successfully converted {converted_count} images to WebP!")
