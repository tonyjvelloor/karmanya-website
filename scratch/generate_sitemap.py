import os
from datetime import datetime

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/public'
base_url = 'https://karmanyaayurveda.com'

def get_html_files(directory):
    html_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                # Get relative path
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                html_files.append(rel_path)
    return html_files

html_files = get_html_files(base_dir)

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for rel_path in html_files:
    # Convert index.html paths to clean URLs
    if rel_path == 'index.html':
        url = base_url + '/'
        priority = '1.0'
    elif rel_path.endswith('/index.html'):
        url = base_url + '/' + rel_path.replace('index.html', '')
        priority = '0.8'
    else:
        url = base_url + '/' + rel_path
        priority = '0.7'
        
    # Exclude 404
    if '404.html' in rel_path:
        continue
        
    sitemap_xml += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_xml += "</urlset>"

with open(os.path.join(base_dir, 'sitemap.xml'), 'w') as f:
    f.write(sitemap_xml)

print(f"Generated comprehensive sitemap with {len(html_files)} URLs.")
