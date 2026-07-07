from playwright.sync_api import sync_playwright

keyword = input("请输入搜索内容：")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.bing.com")

    page.wait_for_timeout(3000)

    page.locator('input[name="q"]').fill(keyword)

    page.keyboard.press("Enter")

    page.wait_for_timeout(5000)

    page.screenshot(path="result.png")

    browser.close()