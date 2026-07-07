from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests


keyword = input("请输入搜索内容：")


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

    links = []

    for r in results.all()[:5]:

        try:
            title = r.locator("h2").inner_text()
            link = r.locator("a").first.get_attribute("href")

            if title and link:
                print(title)
                print(link)
                print()

                links.append(link)

        except:
            pass


    # 打开第一个网页
    if links:

        url = links[0]

        print("正在读取：")
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


        text = soup.get_text(
            "\n",
            strip=True
        )


        # 保存文章内容
        with open(
            "article.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)


        print("文章已保存 article.txt")


    browser.close()