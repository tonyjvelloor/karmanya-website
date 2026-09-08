import re
import glob

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# Update components.css
with open(f"{base_dir}/css/components.css", "r") as f:
    css = f.read()

css = css.replace(
"""    .trust-strip {
        position: relative !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.05em !important;
        padding: 10px 14px !important;
        line-height: 1.4 !important;
        text-align: center !important;
        margin-top: 1.5rem !important;
    }""",
"""    .trust-strip {
        position: relative !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.05em !important;
        padding: 10px 14px !important;
        line-height: 1.4 !important;
        text-align: center !important;
        margin: 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }"""
)

with open(f"{base_dir}/css/components.css", "w") as f:
    f.write(css)

# Update all templates with ?v=11
templates = glob.glob(f'{base_dir}/templates/*.html')
for t in templates:
    with open(t, 'r') as f:
        tmpl = f.read()
    
    tmpl = re.sub(r'components\.css(\?v=\d+)?', 'components.css?v=11', tmpl)
    tmpl = re.sub(r'base\.css(\?v=\d+)?', 'base.css?v=11', tmpl)
    
    with open(t, 'w') as f:
        f.write(tmpl)

print("CSS updated and templates bumped to v11.")
