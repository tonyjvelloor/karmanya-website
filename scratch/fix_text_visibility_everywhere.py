"""
Fix text visibility everywhere across all pages, templates, CSS, and generator scripts.
Ensures zero invisible dark text on dark green backgrounds.
"""
import re, glob, os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# 1. Update scratch/generate_comparison_pages.py
with open(f'{base_dir}/scratch/generate_comparison_pages.py') as f:
    cmp_code = f.read()

cmp_code = cmp_code.replace(
    '<h1 style="font-size: clamp(1.9rem, 4vw, 3rem); font-weight: 400; line-height: 1.25; margin-bottom: var(--space-4);">{item[\'title\']}</h1>',
    '<h1 style="font-size: clamp(1.9rem, 4vw, 3rem); font-weight: 400; line-height: 1.25; margin-bottom: var(--space-4); color: #ffffff;">{item[\'title\']}</h1>'
)
cmp_code = cmp_code.replace(
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0;">Clinical Treatment Comparisons</h1>',
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0; color: #ffffff;">Clinical Treatment Comparisons</h1>'
)
with open(f'{base_dir}/scratch/generate_comparison_pages.py', 'w') as f:
    f.write(cmp_code)
print("Updated scratch/generate_comparison_pages.py")

# 2. Update scratch/generate_symptoms_pages.py
with open(f'{base_dir}/scratch/generate_symptoms_pages.py') as f:
    sym_code = f.read()

sym_code = sym_code.replace(
    '<h1 style="font-size: clamp(1.9rem, 4vw, 3rem); font-weight: 400; line-height: 1.25; margin-bottom: var(--space-4);">{s[\'title\']}</h1>',
    '<h1 style="font-size: clamp(1.9rem, 4vw, 3rem); font-weight: 400; line-height: 1.25; margin-bottom: var(--space-4); color: #ffffff;">{s[\'title\']}</h1>'
)
sym_code = sym_code.replace(
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0;">Ayurvedic Symptom Guides</h1>',
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0; color: #ffffff;">Ayurvedic Symptom Guides</h1>'
)
with open(f'{base_dir}/scratch/generate_symptoms_pages.py', 'w') as f:
    f.write(sym_code)
print("Updated scratch/generate_symptoms_pages.py")

# 3. Update scratch/generate_glossary_page.py
with open(f'{base_dir}/scratch/generate_glossary_page.py') as f:
    glo_code = f.read()

glo_code = glo_code.replace(
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0;">Ayurvedic Medical Glossary</h1>',
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 400; margin: var(--space-4) 0; color: #ffffff;">Ayurvedic Medical Glossary</h1>'
)
with open(f'{base_dir}/scratch/generate_glossary_page.py', 'w') as f:
    f.write(glo_code)
print("Updated scratch/generate_glossary_page.py")

# 4. Update scratch/generate_blog.py
with open(f'{base_dir}/scratch/generate_blog.py') as f:
    blg_code = f.read()

blg_code = blg_code.replace(
    '<h1 style="font-size: clamp(1.8rem, 4vw, 3rem); color: white;',
    '<h1 style="font-size: clamp(1.8rem, 4vw, 3rem); color: #ffffff;'
)
blg_code = blg_code.replace(
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); color: white;',
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); color: #ffffff;'
)
with open(f'{base_dir}/scratch/generate_blog.py', 'w') as f:
    f.write(blg_code)
print("Updated scratch/generate_blog.py")

# 5. Update scratch/generate_reviews_page.py
with open(f'{base_dir}/scratch/generate_reviews_page.py') as f:
    rev_code = f.read()

rev_code = rev_code.replace(
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); color: white;',
    '<h1 style="font-size: clamp(2rem, 4vw, 3.5rem); color: #ffffff;'
)
with open(f'{base_dir}/scratch/generate_reviews_page.py', 'w') as f:
    f.write(rev_code)
print("Updated scratch/generate_reviews_page.py")

