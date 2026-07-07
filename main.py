from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import json


keyword = input("请输入研究主题：")


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # 搜索
    page.goto("https://www.bing.com")

    page.wait_for_timeout(3000)

    page.locator('input[name="q"]').fill(keyword)

    page.keyboard.press("Enter")

    page.wait_for_timeout(5000)


    # 获取搜索结果
    results = page.locator("li.b_algo")

    articles = []


    for r in results.all()[:5]:

        try:
            title = r.locator("h2").inner_text()
            url = r.locator("h2 a").get_attribute("href")


            if title and url:

                print("\n正在读取：")
                print(title)
                print(url)


                headers = {
                    "User-Agent": "Mozilla/5.0"
                }


                response = requests.get(
                    url,
                    headers=headers,
                    timeout=10
                )


                soup = BeautifulSoup(
                    response.text,
                    "html.parser"
                )


                content = soup.get_text(
                    "\n",
                    strip=True
                )


                articles.append(
                    {
                        "title": title,
                        "url": url,
                        "content": content[:3000]
                    }
                )


        except Exception as e:
            print("跳过：", e)


    # 保存JSON

    with open(
        "research.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            articles,
            f,
            ensure_ascii=False,
            indent=2
        )


    print("\n完成！保存 research.json")


    browser.close()