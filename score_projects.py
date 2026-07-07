import json


# 读取研究数据
with open(
    "research.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)


# 关键词
ai_keywords = [
    "AI",
    "人工智能",
    "自动化",
    "Agent",
    "机器人",
    "SaaS"
]

money_keywords = [
    "赚钱",
    "收入",
    "商业",
    "创业",
    "项目",
    "服务"
]


with open(
    "score_report.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# AI项目评分报告\n\n")


    for i, item in enumerate(data, 1):

        text = (
            item["title"]
            +
            item["content"]
        )


        ai_score = 0
        money_score = 0


        for word in ai_keywords:
            if word.lower() in text.lower():
                ai_score += 1


        for word in money_keywords:
            if word in text:
                money_score += 1


        total = min(
            ai_score + money_score,
            10
        )


        f.write(
            f"## {i}. {item['title']}\n\n"
        )

        f.write(
            f"- AI相关度：{min(ai_score,10)}/10\n"
        )

        f.write(
            f"- 商业价值：{min(money_score,10)}/10\n"
        )

        f.write(
            f"- 综合评分：{total}/10\n\n"
        )

        f.write(
            f"来源：{item['url']}\n\n"
        )

        f.write("---\n\n")


print("评分完成：score_report.md")