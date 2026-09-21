#!/usr/bin/env python3
import os
import sys
import shutil
import struct
import zlib
import subprocess

SOURCE_IMAGE = "/Users/tonyvelloor/.gemini/antigravity/brain/b1c28721-3e1e-4b3e-bcb0-291fe59002f2/.user_uploaded/media_1789975753653.png"
BASE_DIR = "/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website"
TMP_DIR = os.path.join(BASE_DIR, "scratch", "favicon_build")

os.makedirs(TMP_DIR, exist_ok=True)

print("1. Parsing source image...")
with open(SOURCE_IMAGE, "rb") as f:
    data = f.read()

pos = 8
idat = bytearray()
width, height = 0, 0

while pos < len(data):
    length, chunk_type = struct.unpack(">I4s", data[pos:pos+8])
    pos += 8
    chunk_data = data[pos:pos+length]
    pos += length + 4
    if chunk_type == b"IHDR":
        width, height, bit_depth, color_type, comp, filt, interlace = struct.unpack(">IIBBBBB", chunk_data)
    elif chunk_type == b"IDAT":
        idat.extend(chunk_data)
    elif chunk_type == b"IEND":
        break

raw = zlib.decompress(idat)
bpp = 4
stride = 1 + width * bpp
pixels = bytearray(width * height * bpp)
prev_row = bytearray(width * bpp)

def paeth(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc: return a
    if pb <= pc: return b
    return c

for y in range(height):
    filter_type = raw[y * stride]
    row_data = raw[y * stride + 1 : (y + 1) * stride]
    curr_row = bytearray(width * bpp)
    for x in range(width * bpp):
        filt_byte = row_data[x]
        left = curr_row[x - bpp] if x >= bpp else 0
        up = prev_row[x]
        up_left = prev_row[x - bpp] if x >= bpp else 0
        if filter_type == 0: val = filt_byte
        elif filter_type == 1: val = (filt_byte + left) & 0xff
        elif filter_type == 2: val = (filt_byte + up) & 0xff
        elif filter_type == 3: val = (filt_byte + ((left + up) // 2)) & 0xff
        elif filter_type == 4: val = (filt_byte + paeth(left, up, up_left)) & 0xff
        curr_row[x] = val
    pixels[y * width * bpp : (y + 1) * width * bpp] = curr_row
    prev_row = curr_row

bg_color = (pixels[0], pixels[1], pixels[2], 255)
print(f"   Background color: #{bg_color[0]:02x}{bg_color[1]:02x}{bg_color[2]:02x}")

# 2. Extract emblem and center on 640x640 canvas
print("2. Extracting emblem onto square canvas...")
CANVAS_SIZE = 640
canvas = bytearray([bg_color[0], bg_color[1], bg_color[2], 255] * (CANVAS_SIZE * CANVAS_SIZE))

src_min_y, src_max_y = 168, 688
src_min_x, src_max_x = 336, 683
emblem_h = src_max_y - src_min_y
emblem_w = src_max_x - src_min_x

dest_offset_y = (CANVAS_SIZE - emblem_h) // 2
dest_offset_x = (CANVAS_SIZE - emblem_w) // 2

for dy in range(emblem_h):
    sy = src_min_y + dy
    for dx in range(emblem_w):
        sx = src_min_x + dx
        src_idx = (sy * width + sx) * bpp
        dest_idx = ((dest_offset_y + dy) * CANVAS_SIZE + (dest_offset_x + dx)) * 4
        canvas[dest_idx : dest_idx + 4] = pixels[src_idx : src_idx + 4]

def write_png(filename, w, h, rgba_data):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        raw.extend(rgba_data[y * w * 4 : (y + 1) * w * 4])
    compressed = zlib.compress(bytes(raw), level=9)
    def chunk(chunk_type, data):
        c = chunk_type + data
        crc = zlib.crc32(c)
        return struct.pack(">I", len(data)) + c + struct.pack(">I", crc)
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    png_bytes = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")
    with open(filename, "wb") as f:
        f.write(png_bytes)

master_emblem_path = os.path.join(TMP_DIR, "master_emblem.png")
write_png(master_emblem_path, CANVAS_SIZE, CANVAS_SIZE, canvas)
print(f"   Created master emblem: {master_emblem_path}")

# 3. Generate PNG sizes using sips
sizes = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-48x48.png": 48,
    "apple-touch-icon.png": 180,
    "android-chrome-192x192.png": 192,
    "android-chrome-512x512.png": 512
}

print("3. Resampling PNG sizes with sips...")
for filename, sz in sizes.items():
    out_path = os.path.join(TMP_DIR, filename)
    subprocess.run(["sips", "-z", str(sz), str(sz), master_emblem_path, "--out", out_path], check=True, stdout=subprocess.DEVNULL)
    print(f"   Generated {filename} ({sz}x{sz})")

# 4. Generate Multi-size ICO (16, 32, 48)
print("4. Building multi-resolution favicon.ico...")
ico_sizes = [16, 32, 48]
entries = []
images = []

for sz in ico_sizes:
    temp_ico = os.path.join(TMP_DIR, f"temp_{sz}.ico")
    subprocess.run(["sips", "-s", "format", "ico", "-z", str(sz), str(sz), master_emblem_path, "--out", temp_ico], check=True, stdout=subprocess.DEVNULL)
    with open(temp_ico, "rb") as f:
        ico_bytes = f.read()
    w, h, c, r, planes, bpp, size, offset = struct.unpack("<BBBBHHII", ico_bytes[6:22])
    img_data = ico_bytes[offset : offset + size]
    entries.append((w, h, c, r, planes, bpp, size))
    images.append(img_data)

n = len(entries)
header = struct.pack("<HHH", 0, 1, n)
current_offset = 6 + 16 * n
packed_entries = []

for i in range(n):
    w, h, c, r, planes, bpp, size = entries[i]
    packed_entries.append(struct.pack("<BBBBHHII", w, h, c, r, planes, bpp, size, current_offset))
    current_offset += size

multi_ico_bytes = header + b"".join(packed_entries) + b"".join(images)
ico_dest = os.path.join(TMP_DIR, "favicon.ico")
with open(ico_dest, "wb") as f:
    f.write(multi_ico_bytes)
print("   Generated favicon.ico (multi-resolution 16x16, 32x32, 48x48)")

# 5. Generate site.webmanifest
print("5. Generating site.webmanifest...")
manifest_content = """{
  "name": "Karmanya Ayurveda Chikitsalaya",
  "short_name": "Karmanya",
  "icons": [
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#634119",
  "background_color": "#634119",
  "display": "standalone"
}
"""
manifest_dest = os.path.join(TMP_DIR, "site.webmanifest")
with open(manifest_dest, "w") as f:
    f.write(manifest_content)

# 6. Copy all generated assets to BASE_DIR, public/, and images/
print("6. Copying assets to target directories...")
target_dirs = [BASE_DIR, os.path.join(BASE_DIR, "public")]
files_to_copy = list(sizes.keys()) + ["favicon.ico", "site.webmanifest"]

for d in target_dirs:
    for fname in files_to_copy:
        src = os.path.join(TMP_DIR, fname)
        dst = os.path.join(d, fname)
        shutil.copy2(src, dst)

# Also copy high-res brand logos to images/ and public/images/
for img_dir in [os.path.join(BASE_DIR, "images"), os.path.join(BASE_DIR, "public", "images")]:
    os.makedirs(img_dir, exist_ok=True)
    shutil.copy2(SOURCE_IMAGE, os.path.join(img_dir, "brand-logo-square.png"))
    shutil.copy2(master_emblem_path, os.path.join(img_dir, "brand-emblem-square.png"))

print("Favicon and icon assets successfully generated and deployed!")
