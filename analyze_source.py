import requests
import re
import json

def analyze_source():
    url = "https://www.ana.co.jp/ja/jp/amc/anacard/cardmileplus/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        return

    content = r.text
    match = re.search(r'(.{100})Starbucks(.{100})', content, re.IGNORECASE | re.DOTALL)
    if match:
        print("Context around Starbucks:")
        print(match.group(0))
        
        # Check if it looks like JSON structure
        if "{" in match.group(0) or "[" in match.group(0):
            print("Likely JSON!")
            
    # Also check for large JSON objects
    json_blobs = re.findall(r'var\s+\w+\s*=\s*(\{.*?\});', content, re.DOTALL)
    print(f"Found {len(json_blobs)} JSON variables.")
    
    # Check for script tags with JSON
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    for s in scripts:
        if "Starbucks" in s:
            print("Found Starbucks inside script tag!")
            print(s[:200] + "...")

if __name__ == "__main__":
    analyze_source()
