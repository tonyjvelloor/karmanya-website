import json

with open('data/treatments.json', 'r') as f:
    treatments = json.load(f)

for t in treatments:
    if t['id'] == 'panchakarma':
        t['faqs'].insert(0, {
            "question": "How much does Panchakarma cost?",
            "answer": "Because Panchakarma is an individualized medical procedure and not a fixed spa package, costs vary significantly depending on the specific therapies (Vamana, Virechana, Basti), the herbal medicines required, and the duration (7 to 21 days). During your initial ₹500 clinical assessment, our physicians will prescribe a precise protocol and our clinic team will provide a transparent, itemized cost estimate before any treatment begins."
        })
        break

with open('data/treatments.json', 'w') as f:
    json.dump(treatments, f, indent=4)
