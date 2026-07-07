from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


# 输入研究主题
keyword = input("请输入研究主题：")


results = []


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    # 搜索
    page.goto(
        f"https://www.bing.com/search?q={keyword}"
    )

    page.wait_for_timeout(5000)


    # 获取搜索结果
    items = page.locator("li.b_algo")


    for i in range(min(items.count(), 5)):

        item = items.nth(i)

        try:
            title = item.locator("h2").inner_text()

            url = item.locator("a").first.get_attribute(
                "href"
            )

            if url:

                results.append(
                    {
                        "title": title,
                        "url": url
                    }
                )

        except Exception:
            pass


    browser.close()



articles = []


# 读取网页内容

for item in results:

    print("\n正在读取：")
    print(item["title"])
    print(item["url"])


    try:

        r = requests.get(
            item["url"],
            timeout=10,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )


        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )


        text = soup.get_text(
            "\n",
            strip=True
        )


        articles.append(
            {
                "title": item["title"],
                "url": item["url"],
                "content": text[:3000]
            }
        )


    except Exception as e:

        print(
            "跳过:",
            e
        )



# 保存最新 research.json

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



# 保存历史数据

os.makedirs(
    "data",
    exist_ok=True
)


filename = datetime.now().strftime(
    "data/%Y-%m-%d_%H-%M.json"
)


with open(
    filename,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        articles,
        f,
        ensure_ascii=False,
        indent=2
    )



print("\n完成！")

print(
    "最新文件：research.json"
)

print(
    "历史文件：",
    filename
)