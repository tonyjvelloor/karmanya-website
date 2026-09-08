import os
import glob
try:
    from PIL import Image
    for file in glob.glob("images/*.jpg") + glob.glob("images/*.png"):
        if "logo" in file: continue # keep logo png for transparency if needed
        img = Image.open(file)
        webp_file = os.path.splitext(file)[0] + ".webp"
        img.save(webp_file, "webp", optimize=True, quality=80)
        print(f"Converted {file} to {webp_file}")
    
    # Minify CSS slightly
    with open("css/components.css", "r") as f:
        css = f.read()
    
    css = css.replace("\n", "").replace("    ", "")
    with open("css/components.css", "w") as f:
        f.write(css)
    print("Minified components.css")
except ImportError:
    print("Pillow not installed, skipping image optimization.")
