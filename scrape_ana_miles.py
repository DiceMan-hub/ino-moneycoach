import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import json
import os

async def scrape_ana_miles():
    output_file = 'ana_mile_stores.xlsx'
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        page = await context.new_page()
        
        url = "https://www.ana.co.jp/ja/jp/amc/anacard/cardmileplus/"
        try:
            await page.goto(url, wait_until='domcontentloaded', timeout=30000)
        except:
            print("Initial load timeout, proceeding...")

        categories = [
            'グルメ', '食品・飲料・お酒', '総合通販', 'スーパー・コンビニ・ドラッグストア',
            '百貨店・ショッピングモール', '書籍・雑誌・新聞・CD・DVD', 'ファッション・小物・アイウェア',
            'インテリア・日用品・雑貨', 'フラワーギフト', '家電・AV機器', 'スポーツ用品',
            'モバイル・Wi-Fiルーター', 'ゴルフ場', '美容・健康', '引越', '住宅', '学習・資格',
            '公共料金', 'ハウスキーピング', 'ウェディング', 'ペットサービス', 'エンターテインメント',
            'ホテル', '空港アクセス', 'お土産・免税店', '空港施設', '交通', 'アクティビティ'
        ]
        
        all_stores = []
        
        for category in categories:
            print(f"Processing: {category}")
            try:
                # Refresh page to ensure clean state
                await page.goto(url, wait_until='domcontentloaded')
                await page.wait_for_timeout(1000)

                # Open Category
                await page.click('#largeBtn', force=True)
                # Wait for modal - use a specialized check
                try:
                    await page.wait_for_selector('.modal-text li span', state='attached', timeout=3000)
                except:
                    print(f"Modal failed for {category}")
                    continue
                
                # Select correct category
                cat_locator = page.locator(f".modal-text li span:has-text('{category}')")
                if await cat_locator.count() > 0:
                    await cat_locator.first.click(force=True)
                else:
                    print(f"Category {category} missing")
                    continue
                await page.wait_for_timeout(500)

                # Open Mile Rate
                await page.click('#smallBtn', force=True)
                await page.wait_for_timeout(500)

                # Select 'ANAカード決済で貯める'
                ana_pay = page.locator(".modal-text li span:has-text('ANAカード決済で貯める')")
                if await ana_pay.count() > 0:
                    await ana_pay.first.click(force=True)
                
                await page.wait_for_timeout(500)

                # Click Search
                await page.click('#searchBtn', force=True)
                
                # Wait for results
                try:
                    await page.wait_for_selector('.asw-tag-card', timeout=5000)
                except:
                    print(f"No results found for {category} immediately.")
                    # Fallback wait
                    await page.wait_for_timeout(2000)

                # Force Scroll to load lazy items
                for _ in range(5):
                    await page.mouse.wheel(0, 5000)
                    await page.wait_for_timeout(500)
                
                # Extract
                cards = page.locator('.asw-tag-card')
                count = await cards.count()
                print(f"Found {count} cards for {category}")

                for i in range(count):
                    card = cards.nth(i)
                    title = await card.locator('.asw-tag-card__title').inner_text()
                    try:
                        rate_text = await card.locator('.asw-tag-card__price').inner_text()
                    except:
                        rate_text = await card.inner_text() # backup
                    
                    link = await card.get_attribute('href')
                    
                    # Filter for 100 yen = 1 mile
                    if '100円' in rate_text and '1マイル' in rate_text:
                        all_stores.append({
                            'カテゴリ': category,
                            '店舗名': title,
                            'URL': link,
                            'マイル積算率': rate_text.replace('\n', ' ').strip()
                        })
            
            except Exception as e:
                print(f"Failed {category}: {e}")

        await browser.close()
        
        # Save Final Excel
        if all_stores:
            df = pd.DataFrame(all_stores)
            df.drop_duplicates(subset=['店舗名', 'URL'], inplace=True)
            df.to_excel(output_file, index=False)
            print(f"SUCCESS: Saved {len(df)} stores to {output_file}")
        else:
            print("No stores found.")

if __name__ == "__main__":
    asyncio.run(scrape_ana_miles())
