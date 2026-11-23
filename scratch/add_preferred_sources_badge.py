import os
import glob
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

google_script_tag = """    <!-- Google Preferred Sources Publisher Script -->
    <script async src="https://news.google.com/swg/js/v1/publisher.js"></script>"""

preferred_card_blog = """            <!-- Google Preferred Source Card -->
            <div class="google-preferred-card" style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border: 1.5px solid #dadce0; border-radius: var(--radius-md, 12px); padding: 22px 24px; margin: var(--space-10, 40px) 0; box-shadow: 0 2px 10px rgba(0,0,0,0.04); display: flex; align-items: center; justify-content: space-between; gap: 20px; flex-wrap: wrap;">
                <div style="display: flex; align-items: center; gap: 16px; flex: 1; min-width: 280px;">
                    <div style="width: 48px; height: 48px; border-radius: 50%; background: #ffffff; box-shadow: 0 2px 6px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid #e8eaed;">
                        <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
                        </svg>
                    </div>
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                            <span style="font-size: 0.75rem; font-weight: 700; color: #1a73e8; text-transform: uppercase; letter-spacing: 0.8px; background: rgba(26,115,232,0.08); padding: 3px 8px; border-radius: 4px;">Google Preferred Source</span>
                            <span style="font-size: 0.75rem; color: #5f6368;">AI Overviews &bull; Discover</span>
                        </div>
                        <h4 style="font-size: 1.05rem; font-weight: 700; color: #202124; margin: 0 0 4px; line-height: 1.3;">Add Karmanya Ayurveda to Your Preferred Sources</h4>
                        <p style="font-size: 0.86rem; color: #5f6368; margin: 0; line-height: 1.4;">See our doctor-reviewed joint care, spine health, and authentic Kerala Panchakarma guides prioritized in your Google Search and AI Overviews.</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; flex-shrink: 0;">
                    <div google-add-preferred-source-btn data-theme="light" data-lang="en"></div>
                    <a href="https://www.google.com/preferences/source?q=karmanyaayurveda.com" target="_blank" rel="noopener" class="google-pref-fallback-btn" style="display: inline-flex; align-items: center; gap: 8px; padding: 9px 18px; background: #ffffff; color: #1a73e8; border: 1.5px solid #1a73e8; border-radius: 24px; font-size: 0.88rem; font-weight: 600; text-decoration: none; transition: all 0.2s ease; box-shadow: 0 1px 3px rgba(0,0,0,0.06);">
                        <span>+ Follow on Google</span>
                    </a>
                </div>
            </div>

"""

# 1. Update all blog articles
blog_files = glob.glob(os.path.join(base_dir, 'public', 'blog', '*', 'index.html'))
print(f"Processing {len(blog_files)} blog articles...")

for b in blog_files:
    with open(b, 'r') as f:
        content = f.read()

    modified = False

    # Inject script into head if missing
    if 'news.google.com/swg/js/v1/publisher.js' not in content:
        if '</head>' in content:
            content = content.replace('</head>', f'{google_script_tag}\n</head>')
            modified = True

    # Inject card before Author Box if missing
    if 'google-add-preferred-source-btn' not in content:
        if '<!-- Author Box -->' in content:
            content = content.replace('<!-- Author Box -->', f'{preferred_card_blog}<!-- Author Box -->')
            modified = True

    if modified:
        with open(b, 'w') as f:
            f.write(content)

print("Blog articles updated successfully.")

# 2. Update public/blog/index.html
blog_index_path = os.path.join(base_dir, 'public', 'blog', 'index.html')
if os.path.exists(blog_index_path):
    with open(blog_index_path, 'r') as f:
        b_idx = f.read()

    if 'news.google.com/swg/js/v1/publisher.js' not in b_idx:
        b_idx = b_idx.replace('</head>', f'{google_script_tag}\n</head>')

    preferred_card_blog_index = """    <div class="container container-editorial" style="margin-top: -30px; margin-bottom: 24px; position: relative; z-index: 5;">
        <div class="google-preferred-card" style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border: 1.5px solid #dadce0; border-radius: var(--radius-md, 12px); padding: 18px 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); display: flex; align-items: center; justify-content: space-between; gap: 20px; flex-wrap: wrap;">
            <div style="display: flex; align-items: center; gap: 14px; flex: 1; min-width: 280px;">
                <div style="width: 44px; height: 44px; border-radius: 50%; background: #ffffff; box-shadow: 0 2px 6px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid #e8eaed;">
                    <svg width="22" height="22" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                        <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                        <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
                        <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
                    </svg>
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 2px;">
                        <span style="font-size: 0.72rem; font-weight: 700; color: #1a73e8; text-transform: uppercase; letter-spacing: 0.8px; background: rgba(26,115,232,0.08); padding: 2px 7px; border-radius: 4px;">Google Preferred Source</span>
                        <span style="font-size: 0.75rem; color: #5f6368;">AI Overviews &bull; Discover &bull; Top Stories</span>
                    </div>
                    <h3 style="font-size: 1.05rem; font-weight: 700; color: #202124; margin: 0 0 2px;">Add Karmanya Ayurveda to Your Preferred Sources on Google</h3>
                    <p style="font-size: 0.85rem; color: #5f6368; margin: 0;">Get our physician-reviewed joint care &amp; Kerala wellness guides prioritized when searching on Google.</p>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; flex-shrink: 0;">
                <div google-add-preferred-source-btn data-theme="light" data-lang="en"></div>
                <a href="https://www.google.com/preferences/source?q=karmanyaayurveda.com" target="_blank" rel="noopener" class="google-pref-fallback-btn" style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: #ffffff; color: #1a73e8; border: 1.5px solid #1a73e8; border-radius: 20px; font-size: 0.85rem; font-weight: 600; text-decoration: none; box-shadow: 0 1px 3px rgba(0,0,0,0.06);">
                    <span>+ Add on Google</span>
                </a>
            </div>
        </div>
    </div>
"""
    if 'google-add-preferred-source-btn' not in b_idx:
        target_str = '<section class="section-padding">'
        if target_str in b_idx:
            b_idx = b_idx.replace(target_str, f'{preferred_card_blog_index}\n    {target_str}')

    with open(blog_index_path, 'w') as f:
        f.write(b_idx)
    print("public/blog/index.html updated successfully.")

print("Done.")
