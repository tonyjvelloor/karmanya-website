import json
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

SERVICE_ACCOUNT_FILE = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/service_account.json'

priority_urls = [
    # Core Homepage & Key Directives
    "https://karmanyaayurveda.com/",
    "https://karmanyaayurveda.com/book-consultation/",
    "https://karmanyaayurveda.com/pricing.md",
    "https://karmanyaayurveda.com/llms.txt",
    
    # Conditions (All Pain & Metabolic Hubs)
    "https://karmanyaayurveda.com/conditions/",
    "https://karmanyaayurveda.com/conditions/knee-joint-pain/",
    "https://karmanyaayurveda.com/conditions/spine-sciatica-back-pain/",
    "https://karmanyaayurveda.com/conditions/cervical-spondylosis-neck-pain/",
    "https://karmanyaayurveda.com/conditions/kerala-ayurveda/",
    "https://karmanyaayurveda.com/conditions/diabetes-madhumeha/",
    "https://karmanyaayurveda.com/conditions/hypertension-high-bp/",
    "https://karmanyaayurveda.com/conditions/obesity-weight-loss/",
    "https://karmanyaayurveda.com/conditions/stress-insomnia-anxiety/",
    "https://karmanyaayurveda.com/conditions/digestive-metabolic-disorders/",
    "https://karmanyaayurveda.com/conditions/womens-health-pcod-hormonal/",
    
    # Core Specialized Treatment Hubs
    "https://karmanyaayurveda.com/treatments/",
    "https://karmanyaayurveda.com/treatments/janu-basti/",
    "https://karmanyaayurveda.com/treatments/kati-basti/",
    "https://karmanyaayurveda.com/treatments/panchakarma/",
    "https://karmanyaayurveda.com/treatments/shirodhara/",
    "https://karmanyaayurveda.com/treatments/kizhi/",
    "https://karmanyaayurveda.com/treatments/udvartana/",
    "https://karmanyaayurveda.com/treatments/kerala-chikitsa/",
    "https://karmanyaayurveda.com/treatments/nadi-pariksha/",
    
    # High-Intent Blogs (Diwali Vacation & Pain vs Surgery)
    "https://karmanyaayurveda.com/blog/diwali-vacation-ayurveda-panchakarma-pune/",
    "https://karmanyaayurveda.com/blog/best-kerala-ayurveda-pune/",
    "https://karmanyaayurveda.com/blog/non-surgical-ayurvedic-treatment-back-pain-pune/",
    "https://karmanyaayurveda.com/blog/ayurveda-vs-knee-replacement-surgery-janu-basti/",
    "https://karmanyaayurveda.com/blog/stage-4-knee-osteoarthritis-ayurvedic-treatment/",
    "https://karmanyaayurveda.com/blog/kati-basti-herniated-l4-l5-disc/",
    "https://karmanyaayurveda.com/blog/ayurvedic-treatment-knee-pain-pune/",
    "https://karmanyaayurveda.com/blog/ayurvedic-sciatica-treatment-pune/",
    "https://karmanyaayurveda.com/blog/ayurvedic-treatment-diabetes-madhumeha-pune/",
    "https://karmanyaayurveda.com/blog/ayurvedic-treatment-hypertension-high-bp-pune/",
    "https://karmanyaayurveda.com/blog/ayurvedic-weight-loss-treatment-udvartana-pune/",
    
    # High-Traffic Local Programmatic Pain Locations
    "https://karmanyaayurveda.com/locations/pimple-saudagar/",
    "https://karmanyaayurveda.com/locations/wakad/",
    "https://karmanyaayurveda.com/locations/hinjawadi/",
    "https://karmanyaayurveda.com/locations/baner/",
    "https://karmanyaayurveda.com/locations/aundh/",
    "https://karmanyaayurveda.com/locations/pcmc/"
]

print(f"Authenticating to push {len(priority_urls)} priority URLs...")
try:
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=['https://www.googleapis.com/auth/indexing']
    )
    session = AuthorizedSession(credentials)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

success = 0
failed = 0
for u in priority_urls:
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    payload = {"url": u, "type": "URL_UPDATED"}
    resp = session.post(endpoint, json=payload)
    if resp.status_code == 200:
        print(f"✅ Indexed: {u}")
        success += 1
    else:
        print(f"⚠️ Failed ({resp.status_code}): {u} - {resp.text[:80]}")
        failed += 1

print(f"\nCompleted! {success} URLs successfully submitted to Google Indexing API. ({failed} failed)")
