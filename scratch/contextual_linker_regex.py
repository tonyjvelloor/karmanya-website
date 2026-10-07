import os
import re

LINK_MAP = {
    r'\b(?i)sciatica\b': '/conditions/spine-sciatica-back-pain/',
    r'\b(?i)back pain\b': '/conditions/spine-sciatica-back-pain/',
    r'\b(?i)knee pain\b': '/conditions/knee-joint-pain/',
    r'\b(?i)arthritis\b': '/conditions/knee-joint-pain/',
    r'\b(?i)pcod\b': '/conditions/womens-health-pcod-hormonal/',
    r'\b(?i)pcos\b': '/conditions/womens-health-pcod-hormonal/',
    r'\b(?i)panchakarma\b': '/treatments/panchakarma/',
    r'\b(?i)shirodhara\b': '/treatments/shirodhara/',
    r'\b(?i)kerala ayurveda\b': '/treatments/kerala-chikitsa/'
}

public_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/public'
total_links = 0

def process_html(html, filepath):
    global total_links
    linked_keywords = set()
    
    # Find all <p> and <li> tags
    def replace_in_tag(match):
        global total_links
        tag_html = match.group(0)
        
        # Don't link inside a tags
        if '<a ' in tag_html or 'href=' in tag_html:
            return tag_html
            
        new_tag_html = tag_html
        for kw, url in LINK_MAP.items():
            if url.strip('/') == filepath.replace(public_dir, '').strip('/'):
                continue
            if kw in linked_keywords:
                continue
                
            # Regex to match keyword not inside HTML attributes (heuristic)
            # Find the word boundary and replace
            def link_replacer(m):
                linked_keywords.add(kw)
                global total_links
                total_links += 1
                return f'<a href="{url}" style="color: var(--color-accent); text-decoration: underline;">{m.group(0)}</a>'
                
            new_tag_html, count = re.subn(kw, link_replacer, new_tag_html, count=1)
            if count > 0:
                linked_keywords.add(kw)
                
        return new_tag_html

    # Replaces content in <p> tags and <li> tags
    html = re.sub(r'<p[^>]*>.*?</p>', replace_in_tag, html, flags=re.DOTALL)
    html = re.sub(r'<li[^>]*>.*?</li>', replace_in_tag, html, flags=re.DOTALL)
    return html

for root, _, files in os.walk(public_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            new_content = process_html(content, filepath)
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)

print(f"Regex Linker Complete! Injected {total_links} links.")
