import asyncio
from playwright.async_api import async_playwright

async def inspect_categories():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.ana.co.jp/ja/jp/amc/anacard/cardmileplus/")
        
        # Click largeBtn to open modal
        await page.click('#largeBtn')
        await page.wait_for_selector('.modal-text li')
        
        # Get all category texts and optional hrefs
        categories = await page.locator('.modal-text li').all()
        for cat in categories:
            text = await cat.inner_text()
            # Check for link
            link = await cat.locator('a').get_attribute('href') if await cat.locator('a').count() > 0 else "No Link"
            print(f"Category: {text.strip()} | Link: {link}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(inspect_categories())
