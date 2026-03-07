
import asyncio
import csv
import os
from playwright.async_api import async_playwright

CSV_PATH = '/Users/mba2024/Documents/Obsidian/Dai DB/00_Projects/JAL/JALカード/JAL_Card_Special_Stores_DoubleMiles_List.csv'
BASE_URL = "https://partner.jal.co.jp/"

async def scrape_jal_special_stores():
    print("Starting JAL Special Store Scraping (All Categories)...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = await context.new_page()

        # The categories based on JAL Partner site structure
        # These are tp (tracking point) or category IDs.
        # Based on manual inspection or common patterns, we need to find the category list page.
        # Often https://partner.jal.co.jp/jct/ is the top page for JAL Card Special Stores.
        
        await page.goto("https://partner.jal.co.jp/jct/", timeout=60000)
        await page.wait_for_selector('.partnertop_cat_nav a', timeout=10000)

        # Get all category links
        category_links = await page.locator('.partnertop_cat_nav a').all()
        categories = []
        for link in category_links:
            href = await link.get_attribute('href')
            text = await link.inner_text()
            if href and 'shop' in href: # Ensure it goes to a shop list
                full_url = BASE_URL + href if href.startswith('/') else href
                categories.append({'name': text.strip(), 'url': full_url})
        
        print(f"Found {len(categories)} categories: {[c['name'] for c in categories]}")

        all_stores = []
        
        for cat in categories:
            print(f"Scraping Category: {cat['name']}...")
            await page.goto(cat['url'], timeout=60000)
            
            # Pagination loop
            while True:
                # Wait for list to load
                try:
                    await page.wait_for_selector('.shop_list_cassette', timeout=5000)
                except Exception:
                    print(f"No stores found for {cat['name']} or timed out.")
                    break

                shops = await page.locator('.shop_list_cassette').all()
                for shop in shops:
                    try:
                        name_el = shop.locator('.shop_name a')
                        if await name_el.count() > 0:
                            name = await name_el.inner_text()
                            url = await name_el.get_attribute('href')
                            # Normalize URL
                            full_shop_url = BASE_URL + url if url.startswith('/') else url
                            
                            all_stores.append({
                                'Store Name': name.strip(),
                                'Shop URL': full_shop_url,
                                'Category': cat['name']
                            })
                    except Exception as e:
                        print(f"Error parsing shop: {e}")
                
                # Check for "Next" button
                # Usually .pager_next a
                next_btn = page.locator('.pager_next a')
                if await next_btn.count() > 0 and await next_btn.is_visible():
                    url = await next_btn.get_attribute('href')
                    await page.goto(BASE_URL + url if url.startswith('/') else url)
                else:
                    break
        
        await browser.close()
        
        # Save to CSV
        if all_stores:
            # Check existing to append or overwrite? User implies adding missing.
            # But "Combine all" suggests a fresh complete list is better to avoid dupes easily.
            # Let's write a new FRESH list to ensure cleanliness.
            
            keys = ['Store Name', 'Shop URL', 'Category']
            with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(all_stores)
            
            print(f"Successfully scraped {len(all_stores)} stores across all categories.")
        else:
            print("No stores were scraped. Check selectors.")

if __name__ == "__main__":
    asyncio.run(scrape_jal_special_stores())
