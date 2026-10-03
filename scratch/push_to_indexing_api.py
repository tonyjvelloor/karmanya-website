import json
import requests
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# --- CONFIGURATION ---
SERVICE_ACCOUNT_FILE = 'service_account.json'
SITEMAP_FILE = 'public/sitemap.xml'
# ---------------------

def get_urls_from_sitemap(sitemap_path):
    print(f"Reading URLs from {sitemap_path}...")
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        urls = []
        # XML namespaces can be tricky, so we'll just search for 'loc' tags
        for loc in root.iter():
            if 'loc' in loc.tag:
                urls.append(loc.text)
        return urls
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
        return []

def push_urls_to_api(urls):
    print("Authenticating with Google Cloud...")
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=['https://www.googleapis.com/auth/indexing']
        )
        session = AuthorizedSession(credentials)
    except FileNotFoundError:
        print(f"❌ ERROR: Could not find {SERVICE_ACCOUNT_FILE}.")
        print("Please follow the instructions to download your JSON key and place it in this folder.")
        return
    except Exception as e:
        print(f"❌ ERROR authenticating: {e}")
        return

    print(f"Successfully authenticated. Pushing {len(urls)} URLs to the Indexing API...")
    
    success_count = 0
    error_count = 0
    
    for url in urls:
        endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
        payload = {
            "url": url,
            "type": "URL_UPDATED"
        }
        
        response = session.post(endpoint, json=payload)
        
        if response.status_code == 200:
            print(f"✅ SUCCESS: Requested indexing for {url}")
            success_count += 1
        else:
            print(f"❌ ERROR: Failed for {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            error_count += 1
            
            # If we get a 403, it usually means the service account wasn't added to Search Console
            if response.status_code == 403:
                print("\n⚠️  403 FORBIDDEN ERROR: This means your Service Account does not have 'Owner' permissions in Google Search Console.")
                print("Please go to Search Console -> Settings -> Users -> Add User, paste the client_email from your JSON file, and set role to 'Owner'.\n")
                break

    print(f"\n--- API PUSH COMPLETE ---")
    print(f"Successfully pushed: {success_count} URLs")
    print(f"Errors encountered: {error_count} URLs")

if __name__ == "__main__":
    urls = get_urls_from_sitemap(SITEMAP_FILE)
    if not urls:
        print("No URLs found. Exiting.")
    else:
        push_urls_to_api(urls)
