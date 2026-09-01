import os
import re

base_dir = "/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/templates"

header_html = """
    <!-- Global Header -->
    <header class="global-header">
        <div class="container" style="display: flex; justify-content: space-between; align-items: center; padding-top: var(--space-4); padding-bottom: var(--space-4);">
            <a href="/" class="brand-logo" style="font-family: var(--font-heading); font-size: 1.75rem; color: var(--color-primary); text-decoration: none; display: flex; align-items: center; gap: 8px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L15 8H9L12 2Z" fill="var(--color-accent)"/><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22ZM12 20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4C16.4183 4 20 7.58172 20 12C20 16.4183 16.4183 20 12 20Z" fill="var(--color-primary)"/></svg>
                {{brand.name}}
            </a>
            <nav class="desktop-nav" style="display: flex; gap: var(--space-6); align-items: center;">
                <a href="/treatments/kerala-chikitsa/" class="nav-link">Kerala Treatments</a>
                <a href="/treatments/panchakarma/" class="nav-link">Panchakarma</a>
                <a href="/conditions/knee-joint-pain/" class="nav-link">Conditions</a>
                <a href="/doctors/dr-irshad/" class="nav-link">Our Doctors</a>
                <a href="/book-consultation/" class="btn btn-primary" style="padding: 8px 24px; font-size: 0.9rem;">Book Consult</a>
            </nav>
        </div>
    </header>
"""

# Pattern to find if it already has a header to avoid duplicates
has_header = re.compile(r'<header class="global-header">')

for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
            
        if not has_header.search(content):
            # Inject right after <body>
            content = content.replace("<body>", "<body>\n" + header_html)
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Added header to {filename}")
