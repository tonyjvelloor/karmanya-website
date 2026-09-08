import json
import os

CONDITIONS_FILE = "data/conditions.json"
TREATMENTS_FILE = "data/treatments.json"

with open(CONDITIONS_FILE, "r") as f:
    conditions = json.load(f)

for c in conditions:
    if c["id"] == "knee-joint-pain":
        c["clinical"]["ayurvedic_perspective"] = "In Ayurveda, Knee Joint Pain is primarily classified under 'Janu Sandhigata Vata'. This condition arises when Vata dosha becomes aggravated and localizes in the knee joints (Janu Sandhi). The excess Vata causes depletion of synovial fluid (Shleshaka Kapha), leading to a dry, rough joint space, which results in friction, pain, crepitus (cracking sounds), and restricted movement. In chronic cases, Ama (metabolic toxins) can also accumulate, leading to inflammation and swelling, known as 'Amavata' when systemic or 'Kroshtukashirsha' when localized specifically with intense swelling."
        c["clinical"]["approach"] = "Our approach focuses on three pillars: 1. Pacifying Vata and reducing pain through specialized oil pooling (Janu Basti). 2. Restoring joint lubrication and repairing cartilage through localized and systemic Rasayana (rejuvenating) herbs. 3. Strengthening the surrounding ligaments and muscles with targeted physiotherapy and Panchakarma modalities like Patra Pinda Sweda (Kizhi)."
        c["faqs"] = [
            {
                "question": "Can Ayurveda help avoid knee replacement surgery?",
                "answer": "Yes, in mild to moderate cases of osteoarthritis, authentic Ayurvedic therapies like Janu Basti and Lepam can significantly reduce pain, improve joint mobility, and delay or even prevent the need for surgical intervention by naturally lubricating the joint space."
            },
            {
                "question": "How many sessions of Janu Basti are required?",
                "answer": "Typically, a continuous course of 7, 14, or 21 days is recommended depending on the severity of cartilage degeneration and Vata vitiation."
            },
            {
                "question": "Are there specific dietary restrictions for knee pain?",
                "answer": "Yes. To balance Vata, patients are advised to avoid dry, cold, and stale foods, as well as excess legumes (like chickpeas) which increase internal dryness. Warm, freshly cooked meals with moderate healthy fats like pure cow's ghee are highly recommended."
            }
        ]
    elif c["id"] == "spine-sciatica-back-pain":
        c["clinical"]["ayurvedic_perspective"] = "Spinal issues and Sciatica are deeply understood in Ayurveda as 'Gridhrasi' (Sciatica) and 'Kati Shoola' (Lower Back Pain). Gridhrasi refers to the gait of a vulture, characteristic of the limp caused by sciatic nerve compression. It is primarily a Vata Vyadhi (neurological disorder caused by Vata), often complicated by Kapha (causing stiffness). The intervertebral discs act as shock absorbers; when Vata dries them out, disc desiccation or herniation (slip disc) occurs, pinching the spinal nerves."
        c["clinical"]["approach"] = "The Karmanya protocol strictly avoids forceful adjustments. Instead, we use continuous warm oil therapies (Kati Basti) to deeply penetrate the paraspinal muscles, release spasms, and nourish the dehydrated discs. This is followed by specialized enemas (Basti) which is the most potent treatment for systemic Vata disorders, acting directly on the gut-brain-nerve axis."
        c["faqs"] = [
            {
                "question": "What is Kati Basti and how does it help a slipped disc?",
                "answer": "Kati Basti involves pooling warm, medicated herbal oil over the lower back using a dough ring. The heat and specific herbs penetrate the tissues, relaxing severe muscle spasms and increasing blood circulation to the dehydrated disc, aiding in natural healing."
            },
            {
                "question": "Is Ayurvedic treatment safe for severe sciatica?",
                "answer": "Yes, Ayurveda offers non-invasive, gentle therapies. We do not perform harsh bone manipulation. Treatment focuses on reducing nerve inflammation and muscle tension through external oils and internal medicines."
            },
            {
                "question": "How soon can I see relief from back pain?",
                "answer": "Patients often experience reduced muscle stiffness within the first 3-5 sessions of external therapy. Comprehensive healing of the nerve and disc structure typically requires a tailored 14 to 21-day program."
            }
        ]

with open(CONDITIONS_FILE, "w") as f:
    json.dump(conditions, f, indent=2)


with open(TREATMENTS_FILE, "r") as f:
    treatments = json.load(f)

for t in treatments:
    if t["id"] == "panchakarma":
        t["clinical"]["ayurvedic_perspective"] = "Panchakarma is not merely a relaxation massage; it is the ultimate, profound detoxification and cellular rejuvenation protocol documented in classical Ayurvedic texts (Charaka Samhita). It literally means 'Five Actions' (Vamana, Virechana, Basti, Nasya, Raktamokshana) designed to uproot deeply embedded metabolic toxins (Ama) from the cellular level and expel them through the body's natural excretory channels."
        t["clinical"]["process"] = "A complete Panchakarma consists of three phases: 1. Purvakarma (Preparation) - internal oleation with medicated ghee (Snehapana) and external sweating (Swedana) to loosen toxins. 2. Pradhana Karma (Main Action) - the specific cleansing procedure like therapeutic purgation or enema. 3. Paschat Karma (Post-Therapy) - strict dietary protocols (Samsarjana Krama) to gradually rebuild the digestive fire (Agni)."
        t["faqs"] = [
            {
                "question": "How many days does a full Panchakarma take?",
                "answer": "A traditional, authentic Panchakarma program takes a minimum of 14 to 21 days depending on the specific procedures prescribed by the physician. Shorter 7-day programs are available for specific localized detox."
            },
            {
                "question": "Is Panchakarma only for sick people?",
                "answer": "No. While highly effective for chronic conditions like autoimmune disorders, arthritis, and metabolic syndrome, Panchakarma is highly recommended as a preventive, annual wellness reset for healthy individuals to maintain longevity and vitality."
            },
            {
                "question": "Can I work during my Panchakarma treatment?",
                "answer": "We strongly advise physical and mental rest during the intensive phases of Panchakarma. The body uses significant energy for deep cellular cleansing, and working can disrupt the therapeutic process."
            }
        ]
    elif t["id"] == "shirodhara":
        t["clinical"]["ayurvedic_perspective"] = "Shirodhara directly soothes Prana Vata and Sadhaka Pitta located in the head and brain (Murdha). The forehead is the site of the Ajna Chakra and a major Marma (vital point). Continuous rhythmic pouring of oil induces a state of deep physiological relaxation, activating the parasympathetic nervous system. Modern research shows Shirodhara lowers sympathetic arousal, slows heart rate, increases alpha and theta brainwaves, and dramatically reduces serum cortisol levels."
        t["clinical"]["process"] = "The patient reclines comfortably in a quiet, dimly lit room on an authentic Kerala Droni (wooden table). A Dhara Patra (vessel) suspended above the head rhythmically pours a gentle, continuous, precise stream of warm herbal oil across the forehead in a specific oscillating pattern. The process typically lasts 45 to 60 minutes."
        t["faqs"] = [
            {
                "question": "What kind of oil is used in Shirodhara?",
                "answer": "The oil is strictly customized based on your clinical assessment. We commonly use Ksheerabala Taila for severe stress and insomnia, Brahmi Taila for cognitive enhancement, or medicated buttermilk (Takradhara) for psoriasis and cooling effects."
            },
            {
                "question": "Does Shirodhara help with hair fall?",
                "answer": "Yes, stress-induced hair fall (Telogen Effluvium) responds excellently to Shirodhara, especially when specific cooling oils like Neelibhringadi or Bhringamalakadi are used, as it improves scalp circulation and reduces heat (Pitta) in the hair follicles."
            },
            {
                "question": "How will I feel immediately after the session?",
                "answer": "Most patients report a feeling of profound mental stillness, clarity, and lightness in the head. It is common to feel deeply relaxed or sleepy. We advise resting and avoiding bright screens or heavy work immediately afterward."
            }
        ]

with open(TREATMENTS_FILE, "w") as f:
    json.dump(treatments, f, indent=2)

print("Expanded SEO content and FAQs injected successfully.")
