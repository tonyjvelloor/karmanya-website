import json

new_article = {
    "slug": "non-surgical-ayurvedic-treatment-back-pain-pune",
    "title": "Non-Surgical Ayurvedic Treatment for Back Pain in Pune: The Kerala Way",
    "meta_title": "Non-Surgical Back Pain Treatment Pune | Kerala Ayurveda",
    "meta_desc": "Looking for non-surgical treatment for back pain in Pune? Discover authentic Kerala Ayurvedic therapies like Kati Basti for sciatica, slip disc & chronic pain.",
    "category": "Treatments",
    "date": "October 7, 2026",
    "author": "Dr. Irshad T.M., BAMS, MD (Ayurveda)",
    "author_url": "/doctors/dr-irshad/",
    "condition_url": "/conditions/spine-sciatica-back-pain/",
    "read_time": "7 min read",
    "intro": "Back pain, whether from a slipped disc, sciatica, or chronic muscle stiffness, can severely impact your quality of life. Many patients are rushed into considering spinal surgery or rely heavily on painkillers. At Karmanya Ayurveda Chikitsalaya in Pimple Saudagar, Pune, we offer a proven, traditional alternative: non-surgical treatment for back pain using authentic Kerala Ayurvedic principles.",
    "sections": [
      {
        "heading": "Why Choose Non-Surgical Treatment for Back Pain?",
        "body": "Spinal surgery carries inherent risks, including nerve damage, prolonged recovery, and the possibility of failed back surgery syndrome. Before taking such a drastic step, exploring non-surgical treatment for back pain is crucial. Ayurveda addresses the root cause of the pain—typically an imbalance in the Vata dosha—rather than just masking the symptoms. Our approach focuses on reducing inflammation, healing damaged tissues, and strengthening the supportive musculature around the spine."
      },
      {
        "heading": "The Kerala Ayurveda Advantage",
        "body": "Karmanya Ayurveda brings the pure, unadulterated healing traditions of Kerala to Pune. Kerala Ayurveda is globally renowned for its highly specialized Panchakarma therapies and unique herbal formulations that are incredibly effective for musculoskeletal and neurological disorders.<br><br>Our treatments utilize medicated oils (Tailas) prepared exactly as described in ancient Kerala Ayurvedic texts like the Sahasrayogam. These potent herbal oils are designed to penetrate deeply into the tissues, providing structural nourishment and profound pain relief."
      },
      {
        "heading": "Key Therapies for Back Pain Relief",
        "body": "<strong>Kati Basti:</strong> This is the cornerstone of our non-surgical treatment for back pain. Warm, medicated oil is pooled over the lumbosacral region inside a dough ring. This deeply lubricates the spine, reduces nerve compression, and relieves muscle spasms.<br><br><strong>Patra Pinda Sweda (Elakizhi):</strong> Fresh, medicinal leaves with anti-inflammatory properties are roasted with herbal oils and tied in a cloth bolus (Kizhi). This warm bolus is massaged over the back, dramatically reducing pain and stiffness.<br><br><strong>Panchakarma (Basti/Enema):</strong> Medicated enemas are considered the ultimate treatment for Vata disorders in Ayurveda, directly addressing the root cause of sciatica and lower back pain at a systemic level."
      }
    ],
    "faqs": [
      {"q": "Can Ayurveda help with a herniated or slipped disc?", "a": "Yes. Our non-surgical Kerala Ayurvedic treatments aim to reduce the inflammation around the herniated disc, relieve the compression on the spinal nerves (like the sciatic nerve), and strengthen the surrounding muscles to support the spine."},
      {"q": "How long does the treatment take?", "a": "A typical course of therapy, such as Kati Basti, ranges from 7 to 21 days depending on the severity of the condition. Consistent treatment yields the best long-term results."}
    ]
}

with open('scratch/generate_blog.py', 'r') as f:
    content = f.read()

parts = content.split("articles = [\n")
if len(parts) == 2:
    new_article_str = json.dumps(new_article, indent=2)
    # add a comma
    new_article_str += ",\n"
    
    new_content = parts[0] + "articles = [\n" + new_article_str + parts[1]
    with open('scratch/generate_blog.py', 'w') as f:
        f.write(new_content)
    print("Injected new article into generate_blog.py")
else:
    print("Could not find articles array")
