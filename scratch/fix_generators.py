import re
import os

files = [
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/scratch/generate_condition_locations.py',
    '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/scratch/generate_occupational_health.py'
]

for fpath in files:
    with open(fpath, 'r') as f:
        content = f.read()
    
    # Replace the old replace logic with the new one
    old_replace = """    html = html.replace('{{seo.meta_title}}', meta_title)
    html = html.replace('{{seo.meta_description}}', meta_desc)
    html = html.replace('{{seo.og_title}}', meta_title)
    html = html.replace('{{seo.og_description}}', meta_desc)
    html = html.replace('{{seo.og_url}}', f"https://karmanyaayurveda.com/occupational/{slug}/")"""
    
    new_replace = """    seo_block = f'''
    <title>{meta_title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://karmanyaayurveda.com/occupational/{slug}/">
    <meta property="og:title" content="{meta_title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://karmanyaayurveda.com/occupational/{slug}/">
    <meta property="og:type" content="article">
    '''
    html = html.replace('{{seo_head_tags}}', seo_block)"""
    
    # For condition_locations, the url is different
    old_replace_cond = """    html = html.replace('{{seo.meta_title}}', meta_title)
    html = html.replace('{{seo.meta_description}}', meta_desc)
    html = html.replace('{{seo.og_title}}', meta_title)
    html = html.replace('{{seo.og_description}}', meta_desc)
    html = html.replace('{{seo.og_url}}', f"https://karmanyaayurveda.com/treatments/local/{slug}/")"""
    
    new_replace_cond = """    seo_block = f'''
    <title>{meta_title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://karmanyaayurveda.com/treatments/local/{slug}/">
    <meta property="og:title" content="{meta_title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://karmanyaayurveda.com/treatments/local/{slug}/">
    <meta property="og:type" content="article">
    '''
    html = html.replace('{{seo_head_tags}}', seo_block)"""

    if 'occupational' in fpath:
        content = content.replace(old_replace, new_replace)
    else:
        content = content.replace(old_replace_cond, new_replace_cond)
        
    with open(fpath, 'w') as f:
        f.write(content)
print("Generators fixed!")
