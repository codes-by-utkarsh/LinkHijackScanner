import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

def check_link(link):
    try:
        resp = requests.get(link, headers=HEADERS, timeout=10, allow_redirects=True)
        if "Page Not Found" in resp.text or resp.status_code in [404, 410]:
            return "❌ Invalid or Not Available"
        if resp.status_code in [200, 301, 302]:
            return "✅ Valid"
        else:
            return f"⚠️ Unusual Response ({resp.status_code})"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def extract_links(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            if any(social in href for social in ["linkedin.com", "instagram.com", "youtube.com", "twitter.com"]):
                if href.startswith("/"):
                    href = url + href
                links.append(href.strip())

        return list(set(links))
    except Exception as e:
        print(f"[!] Failed to fetch: {str(e)}")
        return []

def main():
    site = input("Enter website URL: ").strip()
    if not site.startswith("http"):
        site = "https://" + site

    print(f"\nChecking social media links found on: {site}\n")
    links = extract_links(site)

    if not links:
        print("⚠️  No social media links found.")
        return

    for link in links:
        print(f"Checking: {link}")
        status = check_link(link)
        print(status)

    print("\n✅ Done checking all links.")

if __name__ == "__main__":
    main()
