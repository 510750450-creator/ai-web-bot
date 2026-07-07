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


    # 获取搜索结果
    results = page.locator("li.b_algo")

    data = []

    for r in results.all()[:5]:

        try:
            title = r.locator("h2").inner_text()
            link = r.locator("a").first.get_attribute("href")

            if title:
                data.append({
                    "title": title,
                    "link": link
                })

        except:
            pass


    print("\n搜索结果：")

    for i, item in enumerate(data, 1):
        print(f"{i}. {item['title']}")
        print(item["link"])
        print()


    with open("result.txt", "w", encoding="utf-8") as f:

        for i, item in enumerate(data, 1):
            f.write(f"{i}. {item['title']}\n")
            f.write(f"{item['link']}\n\n")


    browser.close()