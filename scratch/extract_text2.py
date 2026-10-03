from bs4 import BeautifulSoup

with open('/Users/tonyvelloor/.gemini/antigravity/brain/b1c28721-3e1e-4b3e-bcb0-291fe59002f2/.system_generated/steps/7151/content.md', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li']):
    text = tag.get_text(strip=True)
    if text:
        print(f"[{tag.name}] {text}")

print("\n--- IMAGES ---")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    if src:
        print(src)
