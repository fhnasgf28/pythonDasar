import asyncio
from playwright.async_api import async_playwright

async def capture_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        await page.goto("https://cahayamomentum.com/reni-and-panji?to=Tamu%20Undangan")
        await page.wait_for_timeout(5000)  # tunggu animasi selesai
        await page.screenshot(path="output.png")
        await browser.close()

asyncio.run(capture_screenshots())
