import re
import os

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'
build_path = os.path.join(base_dir, 'build.py')

with open(build_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update robots.txt block
old_robots = """    with open(os.path.join(base_dir, 'public', 'robots.txt'), 'w') as f:
        f.write("User-agent: *\\nAllow: /\\nSitemap: https://karmanyaayurveda.com/sitemap.xml\\n")"""

new_robots = """    robots_txt = \"\"\"User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: https://karmanyaayurveda.com/sitemap.xml
\"\"\"
    with open(os.path.join(base_dir, 'public', 'robots.txt'), 'w') as f:
        f.write(robots_txt)"""

if old_robots in code:
    code = code.replace(old_robots, new_robots)
    print("Updated robots.txt in build.py")
else:
    print("Could not match old_robots, attempting regex")
    code = re.sub(r'with open\(os\.path\.join\(base_dir, \'public\', \'robots\.txt\'\), \'w\'\) as f:\s*f\.write\([^\)]+\)', new_robots, code)

# 2. Update legacy redirects
code = code.replace("'diabetes-management': '/conditions/digestive-metabolic-disorders/'", "'diabetes-management': '/conditions/diabetes-madhumeha/'")
code = code.replace("'obesity-management': '/conditions/digestive-metabolic-disorders/'", "'obesity-management': '/conditions/obesity-weight-loss/'")
code = code.replace("'hypertension-management': '/conditions/stress-insomnia-anxiety/'", "'hypertension-management': '/conditions/hypertension-high-bp/'")
print("Updated legacy redirects in build.py")

# 3. Update AI-SEO and add pricing.md
pricing_code = """    # 7c. Generate AI-Readable Pricing (/pricing.md)
    pricing_md = \"\"\"# Karmanya Ayurveda Chikitsalaya - Official Pricing Policy

> Transparent, physician-led clinical care in Pimple Saudagar, Pune. Zero hidden charges, zero surprise registration fees.

## Doctor Consultation Fee
| Service | Fee | Details |
| :--- | :--- | :--- |
| **Initial Clinical Consultation** | **₹500** | Dedicated 45-minute consultation with senior BAMS physician (Dr. Tejasvi Mulik), classical Nadi Pariksha (three-finger radial pulse diagnosis), detailed review of your existing MRI/X-ray reports, Prakriti constitutional mapping, and personalized dietary/lifestyle prescription. |
| **Follow-up Review Consultation** | **Included** | Comprehensive progress review and doshic re-assessment during active therapy course. |

## In-Clinic Procedural Therapies
*Note: All procedural therapies are prescribed strictly on clinical necessity following in-person pulse diagnosis and imaging review. Never sold as generic day-spa packages.*

| Clinical Therapy | Primary Indication | Duration | Price Guidance |
| :--- | :--- | :--- | :--- |
| **Janu Basti** | Knee Osteoarthritis, Cartilage Wear, Crepitus | 45-50 mins | Prescribed in 7 to 14 session courses; individual session pricing explained transparently during consult. |
| **Kati Basti** | Slipped Disc, Lumbar Spondylosis, Sciatica | 45-50 mins | Warm medicated herbal oil pooling at lumbosacral junction to decompress pinched spinal nerves. |
| **Greeva Basti** | Cervical Spondylosis, Neck Stiffness, Arm Numbness | 40-45 mins | Localized medicinal oil retention on cervical spine. |
| **Shirodhara** | Hypertension, Stress, Insomnia, Anxiety | 45-50 mins | Rhythmic stream of warm herbal oil or Takradhara on forehead. |
| **Patra Pinda Sweda (Kizhi)** | Severe Joint Inflammation, Muscle Spasms | 45 mins | Steamed medicinal herbal leaf poultices applied in rhythm. |
| **Udvartana** | Obesity, Stubborn Visceral Fat, Sluggish Metabolism | 45 mins | Upward herbal powder scrub for subcutaneous fat liquefaction. |
| **Abhyangam & Swedanam** | Neuromuscular Stiffness, Poor Circulation | 60 mins | Full-body synchronised medicated oil therapy and herbal steam. |

## Intensive Multi-Day Clinical Packages (Diwali Vacation Care)
| Program | Structure | Target Candidates |
| :--- | :--- | :--- |
| **7-Day Intensive Panchakarma Detox** | Daily therapies, digestive fire (Agni) reset, targeted Virechana | Chronic acidity, metabolic sluggishness, high uric acid, early hypertension. |
| **14-Day Joint & Spine Preservation Protocol** | Daily Basti, Kizhi, localized oil retention, internal neuro-regenerative medicines | Severe Grade 2-3 knee osteoarthritis or lumbar disc herniations seeking to avoid surgery. |
| **Visiting Parents Second Opinion Program** | 45-min scan review, pulse diagnosis, non-surgical conservative plan | Elderly parents visiting Pune for Diwali advised joint replacement or spine surgery. |

## Payment & Clinic Policies
- **Payment Method:** UPI, Credit/Debit Cards, Cash, Net Banking. Pay at the clinic.
- **Location:** 27/11, Swaraj Garden Road, Near One Nation Apartment, Pimple Saudagar, Pune 411027
- **Direct Helpline:** +91 98198 20017
- **Operating Hours:** Open Monday to Sunday, 10:00 AM – 8:00 PM (365 days a year, including Diwali holidays).
\"\"\"
    with open(os.path.join(base_dir, 'public', 'pricing.md'), 'w') as f:
        f.write(pricing_md)
"""

if 'pricing_md' not in code:
    code = code.replace("    # 8. Generate AI-SEO", pricing_code + "\n    # 8. Generate AI-SEO")
    print("Added pricing_md generation in build.py")

# 4. Update llms_txt to remove Dr. Irshad and feature Dr. Tejasvi Mulik
code = code.replace("Senior Staff Physician: Dr. Irshad T.M., BAMS, MD (Ayurveda) — 15+ years of clinical experience in Kerala Ashtavaidya protocols & Panchakarma\n- Staff Physician & Consultant: Dr. Tejasvi Mulik, BAMS — 10+ years of clinical experience in Nadi Pariksha, metabolic disorders, and women's health",
                    "Senior Consulting Physician: Dr. Tejasvi Mulik, BAMS — 10+ years of clinical experience in classical Ashtavaidya Nadi Pariksha, non-surgical spine & joint care, metabolic disorders, and women's health")

with open(build_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("build.py updated successfully.")
