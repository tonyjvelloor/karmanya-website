from PIL import Image

img = Image.open('/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/images/logo.png')
print(f"Original mode: {img.mode}")

webp_img = Image.open('/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/images/logo.webp')
print(f"WebP mode: {webp_img.mode}")
