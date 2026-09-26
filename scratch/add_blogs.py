import re

with open('scratch/generate_blog.py', 'r') as f:
    content = f.read()

new_blogs = """
  {
    "slug": "kamar-dard-ka-ayurvedic-ilaj",
    "title": "Kamar Dard (Back Pain) Ka Ayurvedic Ilaj Pune Mein",
    "meta_title": "Kamar Dard Ka Ayurvedic Ilaj | Back Pain Treatment in Pune",
    "meta_desc": "Pune mein kamar dard ka ayurvedic ilaj. Janu Basti, Kati Basti, and physician-led care for chronic lower back pain relief at Karmanya Ayurveda.",
    "category": "Spine & Sciatica",
    "date": "September 25, 2026",
    "author": "Dr. Irshad T.M., BAMS, MD (Ayurveda)",
    "author_url": "/doctors/dr-irshad/",
    "condition_url": "/conditions/spine-sciatica-back-pain/",
    "read_time": "6 min read",
    "intro": "Kamar dard (lower back pain) aaj ke samay mein sabse aam samasya ban gayi hai. IT professionals, homemakers, aur elderly patients sabhi iska shikar hote hain. Pune ke Karmanya Ayurveda mein hum sciatica, slip disc aur kamar dard ka bina surgery ayurvedic ilaj karte hain.",
    "sections": [
      {
        "heading": "Kamar Dard Ke Mukhya Karan (Causes of Back Pain)",
        "body": "Ayurveda ke anusar, kamar dard 'Kati Shoola' aur 'Gridhrasi' (Sciatica) Vata dosha ke badhne ke karan hota hai. Lamba samay baithna, galat posture, aur galat khaan-paan Vata ko badhata hai, jisse spinal disc mein rukhapan (dryness) aata hai aur nase dabne lagti hain."
      },
      {
        "heading": "Kamar Dard Ka Ayurvedic Ilaj (Ayurvedic Treatment)",
        "body": "Humare clinic mein kamar dard ka ilaj <strong>Kati Basti</strong> se shuru hota hai. Isme kamar ke nichle hisse par aate ka ghera banakar garm medicated tel bhara jata hai. Yeh tel dard aur sujan ko kam karta hai, nason ko aaram deta hai, aur slip disc ko theek hone mein madad karta hai. Iske alawa, <strong>Patra Pinda Sweda (Kizhi)</strong> massage se manspeshiyon (muscles) ka khichav kam kiya jata hai."
      }
    ],
    "faqs": [
      {"q": "Kya Kati Basti se kamar dard theek hota hai?", "a": "Haan, Kati Basti kamar dard ke liye sabse prabhavi ayurvedic treatment hai. Yeh naso ki sujan kam karta hai aur disc ko nutrition deta hai."},
      {"q": "Kati Basti ke kitne session lene padte hain?", "a": "Aam taur par 14 se 21 din ka session zaroori hota hai."}
    ]
  },
  {
    "slug": "gudghe-dukhi-gharguti-upay-ayurveda",
    "title": "Gudghe Dukhi Gharguti Upay (Marathi) & Ayurvedic Treatment",
    "meta_title": "Gudghe Dukhi Gharguti Upay | Ayurvedic Treatment for Knee Pain Pune",
    "meta_desc": "Gudghe dukhi gharguti upay (home remedies for knee pain) and doctor-prescribed Ayurvedic treatments for arthritis in Pune. Avoid knee surgery with Ayurveda.",
    "category": "Knee & Joint Pain",
    "date": "September 24, 2026",
    "author": "Dr. Tejasvi Mulik, BAMS",
    "author_url": "/doctors/dr-tejasvi/",
    "condition_url": "/conditions/knee-joint-pain/",
    "read_time": "6 min read",
    "intro": "Gudghe dukhi (knee pain) hi atyant samanya samasya ahe. Aamhi tumhala gudghe dukhivaril gharguti upay aani Pune madhil Karmanya Ayurveda madhye dilyaa janarya ayurvedic upcharan baddal mahiti denar aahot.",
    "sections": [
      {
        "heading": "Gudghe Dukhi Sathi Gharguti Upay (Home Remedies)",
        "body": "1. <strong>Erandel Tel (Castor Oil):</strong> Erandel telane halke hatane massage kelyas gudghyatil suuj aani vedana kami hotat.<br>2. <strong>Halad aani Aale:</strong> Halad aani aale (ginger) madhye anti-inflammatory gun astat. Tyaancha kadha ghyava.<br>3. <strong>Saindhav Meeth:</strong> Garam panyat saindhav meeth takun shek ghyava."
      },
      {
        "heading": "Karmanya Ayurveda Madhil Janu Basti Upchar",
        "body": "Gharguti upayani pharak na padlyas, Ayurveda madhil <strong>Janu Basti</strong> ha shastriya upchar gheta yeto. Yachyamadhye gudghyavar ubdar ayurvedic tel thevale jate, jyane gudghyatil vata kami houn vedana thambtat aani surgery taalni shakya hote."
      }
    ],
    "faqs": [
      {"q": "Janu Basti mhanje kay?", "a": "Janu Basti ha gudghya sathi ek ayurvedic upchar ahe jyat aushadhi tel gudghyavar thevale jate."},
      {"q": "Pune madhye Janu Basti kuthe milte?", "a": "Karmanya Ayurveda, Pimple Saudagar, Pune madhye Janu Basti chya suvidha uplabdh ahet."}
    ]
  },
"""

content = content.replace("articles = [", "articles = [\n" + new_blogs)

with open('scratch/generate_blog.py', 'w') as f:
    f.write(content)

