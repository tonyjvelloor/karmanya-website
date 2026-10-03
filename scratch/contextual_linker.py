import os
import re
from bs4 import BeautifulSoup

# Define our keyword to URL mapping (Target Money Pages)
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

total_links_injected = 0

def process_text_node(text, keyword, url, linked_keywords):
    # Only link once per keyword per page
    if keyword in linked_keywords:
        return text
        
    # Search for the keyword
    match = re.search(keyword, text)
    if match:
        matched_str = match.group(0)
        # We use a placeholder here so BeautifulSoup doesn't escape the HTML tags
        linked_keywords.add(keyword)
        # Using a special marker that we will replace later with actual HTML
        return text[:match.start()] + f"__LINK_START_{url}_LINK_MID__{matched_str}__LINK_END__" + text[match.end():]
    return text

for root, _, files in os.walk(public_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r') as f:
                html = f.read()
                
            soup = BeautifulSoup(html, 'html.parser')
            
            linked_keywords = set()
            page_modified = False
            
            # We only want to inject links in paragraph <p> or list item <li> text
            for tag in soup.find_all(['p', 'li']):
                # Don't inject if the tag itself is inside an <a> tag
                if tag.find_parent('a'):
                    continue
                    
                # We need to modify the string contents of the tag
                # But since a tag can have multiple children (text, b, strong, a), 
                # we iterate through NavigableString children
                for child in tag.children:
                    if hasattr(child, 'string') and child.string and not child.name:
                        original_text = str(child.string)
                        new_text = original_text
                        
                        for keyword, url in LINK_MAP.items():
                            # Don't link a page to itself!
                            if url.strip('/') == filepath.replace(public_dir, '').strip('/'):
                                continue
                            
                            new_text = process_text_node(new_text, keyword, url, linked_keywords)
                            
                        if new_text != original_text:
                            child.replace_with(new_text)
                            page_modified = True

            if page_modified:
                # Convert soup back to html string
                final_html = str(soup)
                
                # Now replace our placeholders with actual <a> tags
                # This ensures BeautifulSoup doesn't escape our injected HTML
                def replacer(m):
                    url = m.group(1)
                    anchor_text = m.group(2)
                    global total_links_injected
                    total_links_injected += 1
                    return f'<a href="{url}" style="color: var(--color-accent); text-decoration: underline;">{anchor_text}</a>'
                
                final_html = re.sub(r'__LINK_START_(.+?)_LINK_MID__(.+?)__LINK_END__', replacer, final_html)
                
                with open(filepath, 'w') as f:
                    f.write(final_html)

print(f"Contextual Link Graphing Complete! Injected {total_links_injected} contextual links across the site.")
