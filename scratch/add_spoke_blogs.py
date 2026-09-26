import re

with open('scratch/generate_blog.py', 'r') as f:
    content = f.read()

new_blogs = """
  {
    "slug": "stage-4-knee-osteoarthritis-ayurvedic-treatment",
    "title": "Can Ayurveda Cure Stage 4 Knee Osteoarthritis? A Clinical View",
    "meta_title": "Stage 4 Arthritis Knee Treatment Without Surgery | Pune Ayurveda",
    "meta_desc": "Can Ayurveda cure stage 4 knee osteoarthritis without surgery? A clinical view on Janu Basti, cartilage regeneration, and pain management from Karmanya Ayurveda.",
    "category": "Knee & Joint Pain",
    "date": "September 26, 2026",
    "author": "Dr. Irshad T.M., BAMS, MD (Ayurveda)",
    "author_url": "/doctors/dr-irshad/",
    "condition_url": "/conditions/knee-joint-pain/",
    "read_time": "7 min read",
    "intro": "When a patient is diagnosed with Stage 4 (severe) knee osteoarthritis, the standard advice is immediate Total Knee Replacement (TKR). The cartilage is significantly worn down, and the joint space is severely narrowed (bone-on-bone). Many patients ask us: 'Can Ayurveda reverse Stage 4 arthritis?' Here is our honest, clinical perspective on what Ayurveda can and cannot do for end-stage knee degeneration.",
    "sections": [
      {
        "heading": "The Reality of Cartilage Regeneration",
        "body": "Let us be clear: no medical science—including Ayurveda—can miraculously regrow completely destroyed cartilage or reverse severe bone deformities. If you have complete joint ankylosis (the bones have fused), surgery is necessary. However, most 'Stage 4' diagnoses still have some joint space remaining, and the pain is primarily driven by severe inflammation, nerve hypersensitivity, and synovial fluid depletion."
      },
      {
        "heading": "How Ayurveda Manages Stage 4 Knee Pain",
        "body": "In Ayurveda, this is a severe state of <em>Janu Sandhigata Vata</em>. Our approach is palliative and restorative, aiming to delay surgery and improve quality of life.<br><br><strong>1. Janu Basti:</strong> By pooling warm, medicated oils (like Mahanarayana Taila) over the knee, we deeply lubricate the joint capsule and soothe irritated nerve endings.<br><strong>2. Patra Pinda Sweda:</strong> This reduces the severe muscle spasms in the calf and thigh that exacerbate knee pain.<br><strong>3. Internal Rasayanas:</strong> Herbs like Guggulu and Ashwagandha reduce systemic inflammation and support remaining tissue health."
      }
    ],
    "faqs": [
      {"q": "Can I avoid knee replacement entirely with Stage 4 arthritis?", "a": "It depends on the exact degree of bone erosion. Many of our Stage 4 patients have successfully delayed surgery for years by managing pain and inflammation through regular Ayurvedic therapies."},
      {"q": "How quickly will the pain reduce?", "a": "In severe cases, you may notice a reduction in stiffness within 7-10 days of intensive Janu Basti, though a full 21-day course is usually required for sustained relief."}
    ]
  },
  {
    "slug": "kati-basti-herniated-l4-l5-disc",
    "title": "Can Kati Basti Heal a Herniated L4-L5 Disc? Clinical Insights",
    "meta_title": "Kati Basti for Herniated L4-L5 Disc | Sciatica Treatment Pune",
    "meta_desc": "Learn how Kati Basti works to heal a herniated L4-L5 disc and relieve sciatica without surgery. A clinical guide by Karmanya Ayurveda, Pune.",
    "category": "Spine & Sciatica",
    "date": "September 26, 2026",
    "author": "Dr. Irshad T.M., BAMS, MD (Ayurveda)",
    "author_url": "/doctors/dr-irshad/",
    "condition_url": "/conditions/spine-sciatica-back-pain/",
    "read_time": "6 min read",
    "intro": "The L4-L5 and L5-S1 spinal segments are the most common sites for disc herniation. When a disc bulges or herniates here, it compresses the sciatic nerve, causing excruciating pain down the leg. The Ayurvedic therapy <em>Kati Basti</em> is renowned for treating this. But how exactly does pooling warm oil on your back heal a ruptured disc?",
    "sections": [
      {
        "heading": "The Mechanism of Kati Basti on a Herniated Disc",
        "body": "When a disc herniates, the surrounding paraspinal muscles immediately go into spasm to 'splint' and protect the spine. This spasm cuts off blood flow, causing the disc to dehydrate further. Kati Basti breaks this cycle.<br><br>The sustained warmth and specific herbal properties of the oil penetrate the skin, causing profound vasodilation (widening of blood vessels). This fresh blood flow flushes out inflammatory chemicals around the sciatic nerve root. It relaxes the muscle spasm, allowing the spine to decompress. When the pressure is taken off, the disc can rehydrate and, over time, the body's natural macrophage system can resorb the herniated fragment."
      },
      {
        "heading": "Why Oil Matters: Medicated Taila",
        "body": "We don't just use hot oil. We use classical formulations like <em>Ksheerabala Taila</em> (containing milk, Sida cordifolia, and sesame oil) which are specifically neuro-protective (nourishing to Majja Dhatu) and anti-inflammatory."
      }
    ],
    "faqs": [
      {"q": "Is Kati Basti safe for a severe slip disc?", "a": "Yes, Kati Basti is 100% non-invasive and does not involve bone manipulation or cracking. It is completely safe for slip discs."},
      {"q": "How long does it take to see results on an MRI?", "a": "While pain relief happens in weeks, structural changes on an MRI (disc resorption) typically take 3 to 6 months of sustained Ayurvedic management and postural care."}
    ]
  },
"""

content = content.replace("articles = [", "articles = [\n" + new_blogs)

with open('scratch/generate_blog.py', 'w') as f:
    f.write(content)

