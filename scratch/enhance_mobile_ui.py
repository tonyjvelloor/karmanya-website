import os
import glob
import re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

# 1. Update css/components.css
components_css_path = f"{base_dir}/css/components.css"
with open(components_css_path, "r") as f:
    css_content = f.read()

mobile_css_additions = """
/* ==========================================================================
   Comprehensive Mobile UI & UX Optimization
   ========================================================================== */

/* Prevent horizontal scroll on mobile */
html, body {
    overflow-x: hidden;
    width: 100%;
}

/* Mobile Hamburger Button */
.mobile-menu-toggle {
    display: none;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 42px;
    height: 42px;
    background: #FFFFFF;
    border: 1px solid var(--color-border);
    border-radius: 8px;
    cursor: pointer;
    gap: 5px;
    padding: 0;
    transition: all 0.2s ease;
    box-shadow: var(--shadow-sm);
}
.mobile-menu-toggle:hover {
    background: rgba(44, 62, 45, 0.05);
    border-color: var(--color-accent);
}
.hamburger-bar {
    width: 20px;
    height: 2px;
    background-color: var(--color-primary);
    border-radius: 2px;
    transition: all 0.3s ease;
    display: block;
}

/* Mobile Navigation Drawer */
.mobile-nav-drawer {
    display: none;
    position: fixed;
    top: 0;
    right: -100%;
    width: 85%;
    max-width: 320px;
    height: 100vh;
    height: 100dvh;
    background: #FFFFFF;
    z-index: 100001;
    box-shadow: -8px 0 30px rgba(0,0,0,0.2);
    transition: right 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    overflow-y: auto;
    padding: 20px 18px 36px;
    box-sizing: border-box;
    flex-direction: column;
}
.mobile-nav-drawer.active {
    right: 0 !important;
}

/* Backdrop for Mobile Drawer */
.mobile-nav-backdrop {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    height: 100dvh;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(2px);
    z-index: 100000;
    opacity: 0;
    transition: opacity 0.3s ease;
}
.mobile-nav-backdrop.active {
    display: block !important;
    opacity: 1 !important;
}

.mobile-nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--color-border);
    margin-bottom: 16px;
}
.mobile-nav-close {
    background: none;
    border: none;
    font-size: 1.8rem;
    line-height: 1;
    color: var(--color-primary);
    cursor: pointer;
    padding: 4px 8px;
    border-radius: 6px;
}
.mobile-nav-close:hover {
    background: var(--color-surface);
}

.mobile-nav-links {
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.mobile-nav-item {
    padding: 10px 12px;
    font-size: 1rem;
    font-weight: 500;
    color: var(--color-text);
    text-decoration: none;
    border-radius: 8px;
    transition: background 0.2s ease, color 0.2s ease;
    display: flex;
    align-items: center;
    gap: 10px;
}
.mobile-nav-item:hover, .mobile-nav-item:active {
    background: var(--color-surface);
    color: var(--color-accent);
}

@media (max-width: 768px) {
    .mobile-menu-toggle {
        display: flex !important;
    }
    .mobile-nav-drawer {
        display: flex;
    }
    .desktop-nav {
        display: none !important;
    }
    
    /* Top utility bar on mobile */
    .top-utility-bar {
        padding: 6px 0 !important;
        font-size: 0.78rem !important;
    }
    .top-utility-inner {
        flex-direction: column !important;
        gap: 4px !important;
        text-align: center !important;
        justify-content: center !important;
    }
    .top-utility-badge {
        display: none !important;
    }
    
    /* Hide floating WhatsApp button on mobile because sticky bottom bar has it */
    #whatsapp-float,
    .floating-whatsapp {
        display: none !important;
    }
    
    /* Ensure body has safe bottom spacing for sticky bar */
    body {
        padding-bottom: calc(72px + env(safe-area-inset-bottom, 0px)) !important;
    }
    
    /* Ensure mobile sticky bar is prominent and clean */
    #mobile-sticky-bar {
        display: flex !important;
        padding: 8px 12px calc(8px + env(safe-area-inset-bottom, 0px)) !important;
        z-index: 99998 !important;
    }
    
    /* Hero section improvements on mobile */
    .hero {
        padding: 3rem 0 2rem !important;
        min-height: auto !important;
    }
    .hero h1 {
        font-size: clamp(1.85rem, 5.5vw, 2.6rem) !important;
        line-height: 1.15 !important;
    }
    .hero p {
        font-size: 1rem !important;
        line-height: 1.55 !important;
    }
    .hero .btn {
        width: 100% !important;
        max-width: 320px !important;
    }
    .trust-strip {
        position: relative !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.05em !important;
        padding: 10px 14px !important;
        line-height: 1.4 !important;
        text-align: center !important;
        margin-top: 1.5rem !important;
    }
    
    /* Shloka banner on mobile */
    .kerala-shloka-banner {
        padding: 20px 16px !important;
        margin: 24px auto 32px !important;
    }
    .shloka-sanskrit {
        font-size: 1.05rem !important;
        line-height: 1.5 !important;
    }
    .shloka-translation {
        font-size: 0.92rem !important;
    }
    
    /* Doctor profile card on mobile */
    .doctor-card {
        padding: 20px 16px !important;
    }
    
    /* Consultation booking card on mobile */
    .booking-hero-card {
        grid-template-columns: 1fr !important;
        border-radius: 12px !important;
    }
    .booking-left-col, .booking-right-col {
        padding: 20px 16px !important;
    }
    
    /* Container padding */
    .container {
        padding: 0 16px !important;
    }
}
"""

if "mobile-nav-drawer" not in css_content:
    with open(components_css_path, "a") as f:
        f.write("\n" + mobile_css_additions)
    print("css/components.css updated with mobile UI styles.")
else:
    # Replace existing mobile css if present
    print("css/components.css already has mobile-nav-drawer, updating...")
    idx = css_content.find("/* ==========================================================================\n   Comprehensive Mobile UI")
    if idx != -1:
        css_content = css_content[:idx] + mobile_css_additions
        with open(components_css_path, "w") as f:
            f.write(css_content)

# 2. Update HTML templates with hamburger toggle and drawer
MOBILE_NAV_HEADER_SNIPPET = """            <!-- Mobile Menu Hamburger Button -->
            <button class="mobile-menu-toggle" id="mobileMenuBtn" aria-label="Toggle navigation menu">
                <span class="hamburger-bar"></span>
                <span class="hamburger-bar"></span>
                <span class="hamburger-bar"></span>
            </button>
        </div>
        <!-- Mobile Navigation Drawer -->
        <div class="mobile-nav-drawer" id="mobileNavDrawer">
            <div class="mobile-nav-header">
                <span style="font-weight: 700; color: var(--color-primary); font-size: 1.1rem; font-family: var(--font-heading);">Menu</span>
                <button class="mobile-nav-close" id="mobileNavClose" aria-label="Close menu">&times;</button>
            </div>
            <nav class="mobile-nav-links">
                <a href="/treatments/" class="mobile-nav-item">🌿 Treatments</a>
                <a href="/conditions/" class="mobile-nav-item">🩺 Conditions We Treat</a>
                <a href="/our-story/" class="mobile-nav-item">📜 Our Story</a>
                <a href="/doctors/" class="mobile-nav-item">👨‍⚕️ Our Doctors</a>
                <a href="/blog/" class="mobile-nav-item">📖 Patient Education</a>
                <a href="/reviews/" class="mobile-nav-item">⭐ Patient Reviews</a>
                <a href="/locations/" class="mobile-nav-item">📍 Nearby Areas</a>
                <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid var(--color-border);">
                    <a href="/book-consultation/" class="btn btn-primary" style="display: block; width: 100%; text-align: center; padding: 12px; margin-bottom: 10px; box-sizing: border-box;">Book Consultation</a>
                    <a href="https://wa.me/919819820017" target="_blank" rel="noopener" class="btn" style="display: block; width: 100%; text-align: center; padding: 12px; background: #25D366; color: white; box-sizing: border-box;">💬 WhatsApp Us</a>
                </div>
            </nav>
        </div>
        <!-- Mobile Menu Backdrop -->
        <div class="mobile-nav-backdrop" id="mobileNavBackdrop"></div>"""

MOBILE_JS_SNIPPET = """
<script>
// Mobile Navigation Drawer Toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.getElementById('mobileMenuBtn');
    const closeBtn = document.getElementById('mobileNavClose');
    const drawer = document.getElementById('mobileNavDrawer');
    const backdrop = document.getElementById('mobileNavBackdrop');
    
    function openMenu() {
        if (drawer) drawer.classList.add('active');
        if (backdrop) backdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    
    function closeMenu() {
        if (drawer) drawer.classList.remove('active');
        if (backdrop) backdrop.classList.remove('active');
        document.body.style.overflow = '';
    }
    
    if (menuBtn) menuBtn.addEventListener('click', openMenu);
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    if (backdrop) backdrop.addEventListener('click', closeMenu);
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeMenu();
    });
});
</script>
"""

templates = glob.glob(f'{base_dir}/templates/*.html')
for t in templates:
    with open(t, 'r') as f:
        tmpl = f.read()
    
    # Update CSS version query parameter to ?v=10 for cache busting
    tmpl = re.sub(r'components\.css(\?v=\d+)?', 'components.css?v=10', tmpl)
    tmpl = re.sub(r'base\.css(\?v=\d+)?', 'base.css?v=10', tmpl)
    
    # Add mobile nav if not present
    if 'mobileMenuBtn' not in tmpl:
        # Find closing </nav>\n        </div> inside <header class="global-header">
        # Replace </nav>\n        </div> with </nav>\n MOBILE_NAV_HEADER_SNIPPET
        # Let's use regex
        pattern = r'(<nav class="desktop-nav"[^>]*>[\s\S]*?</nav>\s*</div>)'
        match = re.search(pattern, tmpl)
        if match:
            old_nav_block = match.group(1)
            # Remove closing </div> and replace
            nav_without_closing_div = old_nav_block[:-6].rstrip()
            new_nav_block = nav_without_closing_div + "\n" + MOBILE_NAV_HEADER_SNIPPET
            tmpl = tmpl.replace(old_nav_block, new_nav_block)
    
    # Add JS script if not present
    if 'mobileMenuBtn' in tmpl and 'Mobile Navigation Drawer Toggle' not in tmpl:
        tmpl = tmpl.replace('</body>', MOBILE_JS_SNIPPET + '\n</body>')
        
    with open(t, 'w') as f:
        f.write(tmpl)

print("All templates updated with mobile navigation and CSS v10.")
