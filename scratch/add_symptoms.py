import json
import re

file_path = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website/scratch/generate_symptoms_pages.py'
with open(file_path, 'r') as f:
    content = f.read()

new_symptoms = [
    {
        "slug": "pain-radiating-down-leg",
        "title": "Pain Radiating Down Leg: Identifying Sciatica vs Lumbar Strain",
        "meta_title": "Pain Radiating Down Right/Left Leg | Sciatica Treatment Pune",
        "meta_desc": "Is your back pain radiating down your thigh to your calf? Learn the Ayurvedic perspective on Sciatica (Gridhrasi) and how Kati Basti decompresses the sciatic nerve.",
        "symptom_name": "Pain Radiating Down Leg",
        "target_condition": "Sciatica & Slip Disc",
        "condition_url": "/conditions/spine-sciatica-back-pain/",
        "read_time": "5 min read",
        "summary": "A sharp, shooting, or burning pain that starts in the lower back and travels down the back of the thigh to the calf or foot is the classic presentation of Sciatica. In Ayurveda, this is known as Gridhrasi.",
        "sections": [
            {
                "heading": "Gridhrasi: The Vata Nerve Entrapment",
                "content": "Ayurveda describes Gridhrasi as an intense aggravation of Vata dosha in the lower back (Kati), pelvis, and legs. 'Gridhra' means vulture—describing the altered, limping gait patients develop as the sciatic nerve is compressed by a herniated or bulging lumbar disc (typically L4-L5 or L5-S1)."
            },
            {
                "heading": "Non-Surgical Decompression with Kati Basti",
                "content": "Modern medicine often suggests painkillers, epidural steroid injections, or microdiscectomy surgery. At Karmanya, we use <strong>Kati Basti</strong>—pooling warm medicated oils like <em>Sahacharadi</em> and <em>Dhanwantharam</em> over the lumbar spine. This reduces inflammation around the nerve root, hydrates the desiccated disc, and relieves the mechanical pressure without surgery."
            }
        ],
        "faqs": [
            {"q": "How do I know if it is Sciatica or a muscle pull?", "a": "A muscle pull typically remains localized to the lower back. If the pain shoots past your knee into your calf or foot, accompanied by numbness or tingling, it is a nerve issue (Sciatica)."}
        ]
    },
    {
        "slug": "severe-morning-heel-pain",
        "title": "Severe Morning Heel Pain: Plantar Fasciitis and Ayurvedic Calcaneal Spur Care",
        "meta_title": "Morning Heel Pain Treatment in Pune | Plantar Fasciitis Care",
        "meta_desc": "Do your first steps out of bed cause severe heel pain? Explore the Ayurvedic understanding of Plantar Fasciitis (Vatakantaka) and Agnikarma treatment.",
        "symptom_name": "Morning Heel Pain",
        "target_condition": "Plantar Fasciitis",
        "condition_url": "/conditions/",
        "read_time": "4 min read",
        "summary": "If taking your first steps out of bed in the morning feels like stepping on a nail, you are likely suffering from Plantar Fasciitis or a Calcaneal Spur. Ayurveda identifies this as Vatakantaka.",
        "sections": [
            {
                "heading": "Vatakantaka: When Vata Localizes in the Heel",
                "content": "Continuous standing, improper footwear, or metabolic blockages cause Vata to lodge in the heel (Parshni). This dries out the plantar fascia tendon, causing micro-tears and intense inflammation, which is worst after a period of rest (like sleeping)."
            },
            {
                "heading": "Agnikarma: The Ultimate Ayurvedic Pain Relief",
                "content": "While insoles provide temporary relief, Karmanya utilizes <strong>Agnikarma</strong> (thermal micro-cautery) and localized <em>Ishtika Sweda</em> (medicated brick fomentation). This immediately pacifies Vata, melts the accumulated stiffness (Stambha), and permanently alters the pain pathway at the heel."
            }
        ],
        "faqs": [
            {"q": "Will Ayurvedic treatment cure a heel spur?", "a": "Yes. While the bony spur might remain on an X-ray, the inflammation of the fascia and the agonizing pain can be completely resolved using Agnikarma and specific medicated oils."}
        ]
    },
    {
        "slug": "stiff-neck-and-finger-numbness",
        "title": "Stiff Neck with Numbness in Fingers: The Early Signs of Cervical Spondylosis",
        "meta_title": "Stiff Neck & Finger Numbness | Cervical Spondylosis Pune",
        "meta_desc": "Experiencing chronic neck stiffness accompanied by tingling or numbness in your fingers? Discover Ayurvedic Griva Basti treatment for cervical nerve compression.",
        "symptom_name": "Neck Stiffness & Numbness",
        "target_condition": "Cervical Spondylosis",
        "condition_url": "/conditions/cervical-spondylosis-neck-pain/",
        "read_time": "5 min read",
        "summary": "A stiff neck is common. However, when a stiff neck is accompanied by a 'pins and needles' sensation, tingling, or numbness radiating into your shoulders, arms, or fingers, it indicates cervical nerve compression (Cervical Spondylosis).",
        "sections": [
            {
                "heading": "Manyastambha and Nerve Compression",
                "content": "Constant downward looking at laptops and phones reverses the natural curve of the cervical spine. In Ayurveda, this causes Vata aggravation in the neck (Manyastambha), drying out the C4-C7 discs. As the disc space narrows, the nerves traveling down to your fingers get pinched."
            },
            {
                "heading": "Reversing 'Tech Neck' with Griva Basti",
                "content": "To prevent permanent nerve damage, Karmanya physicians administer <strong>Griva Basti</strong>. By pooling warm, Vata-pacifying oils over the cervical vertebrae, we reduce the localized inflammation, nourish the spinal nerves, and restore mobility to the neck without the need for cervical collars or surgery."
            }
        ],
        "faqs": [
            {"q": "Can Ayurveda cure tingling in the fingers?", "a": "Yes. The tingling in the fingers originates from the compressed nerves in the neck. By treating the root cause in the cervical spine through Griva Basti and Nasya, the finger numbness naturally resolves."}
        ]
    }
]

# Find the list of symptoms in the file
pattern = r'(symptoms = \[\n)(.*?)(\n\]\n)'
match = re.search(pattern, content, re.DOTALL)

if match:
    existing_symptoms_str = match.group(2)
    # create a json string for the new symptoms, strip the outer brackets
    new_symptoms_str = json.dumps(new_symptoms, indent=4)
    new_symptoms_str = new_symptoms_str[2:-2] # remove [\n and \n]
    
    updated_symptoms_str = existing_symptoms_str + ",\n    " + new_symptoms_str
    new_content = content[:match.start(2)] + updated_symptoms_str + content[match.end(2):]
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    print("Added new symptoms to generate_symptoms_pages.py")
else:
    print("Could not find symptoms array in the file")

