import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def fast_scrape():
    url = "https://www.ana.co.jp/ja/jp/amc/anacard/cardmileplus/"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=60000)
        
        cats = ['グルメ', '食品・飲料・お酒', '総合通販', 'スーパー・コンビニ・ドラッグストア',
                '百貨店・ショッピングモール', '書籍・雑誌・新聞・CD・DVD', 'ファッション・小物・アイウェア',
                'インテリア・日用品・雑貨', 'フラワーギフト', '家電・AV機器'] # Just top 10 for now
        
        all_data = []

        for cat in cats:
            print(f"Trying {cat}...")
            try:
                await page.reload()
                await page.wait_for_timeout(2000)
                
                # Category
                await page.click('#largeBtn', force=True)
                await page.wait_for_timeout(1000)
                await page.click(f"text='{cat}'", force=True)
                await page.wait_for_timeout(1000)
                
                # Search
                await page.click('#searchBtn', force=True)
                await page.wait_for_timeout(3000)
                
                # Check results
                cards = await page.locator('.asw-tag-card').all()
                print(f"Found {len(cards)} cards.")
                
                for card in cards:
                    text = await card.inner_text()
                    if "100円" in text and "1マイル" in text:
                        title = await card.locator('.asw-tag-card__title').inner_text()
                        link = await card.get_attribute('href')
                        all_data.append({"Category": cat, "Name": title, "URL": link})
                        
            except Exception as e:
                print(f"Error {cat}: {e}")
                
        await browser.close()
        
        if all_data:
            df = pd.DataFrame(all_data)
            df.to_excel("ana_fast_scrape.xlsx", index=False)
            print("Saved!")
        else:
            print("No data.")

if __name__ == "__main__":
    asyncio.run(fast_scrape())
