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

    # 获取搜索结果标题
    titles = page.locator("li.b_algo h2").all_inner_texts()

    print("\n搜索结果：")
    for i, title in enumerate(titles[:5], 1):
        print(f"{i}. {title}")

    # 保存结果
    with open("result.txt", "w", encoding="utf-8") as f:
        for i, title in enumerate(titles[:5], 1):
            f.write(f"{i}. {title}\n")

    browser.close()