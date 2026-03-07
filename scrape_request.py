import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_ana_tameru():
    url = "https://www.ana.co.jp/ja/jp/amc/tameru/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    
    print(f"Fetching {url}...")
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        return

    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Check for categories in the page content
    # Look for "Details" or "tameru" sections
    
    all_stores = []
    
    # Try to find store containers (cards, lists)
    # Based on observation, they might be in sections
    
    # Find all elements that might be store entries
    # Heuristic: look for '100円' text
    elements = soup.find_all(string=re.compile("100円"))
    print(f"Found {len(elements)} elements with '100円'.")
    
    for el in elements:
        # Traverse up to find the container
        container = el.find_parent('div') # Try div first
        if not container:
            continue
            
        text = container.get_text(strip=True)
        
        # Check if it has '1マイル' rate
        if "100円" in text and "1マイル" in text:
            # Extract store name - usually finding a heading or bold text
            name_el = container.find(['h3', 'h4', 'strong', 'b'])
            if name_el:
                name = name_el.get_text(strip=True)
            else:
                # Fallback: extract substring before rate text
                parts = text.split('100円')
                name = parts[0][-30:] # Last 30 chars
            
            # Extract link
            link_el = container.find('a')
            if not link_el:
                link_el = container.find_parent('a')
            link = link_el['href'] if link_el else "N/A"
            if link.startswith('/'):
                link = "https://www.ana.co.jp" + link
                
            # Filter duplicates or generic text
            if len(name) < 2 or "ごとに" in name or "利用" in name:
                continue
                
            # Try to identify category based on section headers?
            # Find preceding h2/h3
            category = "General"
            prev = container.find_previous(['h2', 'h3'])
            if prev:
                category = prev.get_text(strip=True)

            all_stores.append({
                "Category": category,
                "Store Name": name,
                "URL": link,
                "Rate": "100円=1マイル"
            })
            
    # Deduplicate
    df = pd.DataFrame(all_stores)
    if not df.empty:
        df.drop_duplicates(subset=['Store Name', 'URL'], inplace=True)
        df.to_excel('ana_mile_tameru.xlsx', index=False)
        print(f"Saved {len(df)} stores to ana_mile_tameru.xlsx")
    else:
        print("No stores found via static scrape.")

if __name__ == "__main__":
    scrape_ana_tameru()
