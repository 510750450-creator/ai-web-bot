import os
import json
from collections import Counter


data_dir = "data"


keywords = [
    "客服",
    "视频生成",
    "自动剪辑",
    "内容生成",
    "营销自动化",
    "SaaS",
    "Agent",
    "智能助手",
    "电商",
    "教育",
    "办公自动化",
    "企业服务",
    "机器人",
]


weights = {
    "客服": 30,
    "Agent": 30,
    "SaaS": 25,
    "企业服务": 25,
    "营销自动化": 25,
    "智能助手": 20,
    "机器人": 20,
    "电商": 15,
    "教育": 15,
    "视频生成": 15,
}


counter = Counter()


files = os.listdir(data_dir)


for file in files:

    if file.endswith(".json"):

        path = os.path.join(
            data_dir,
            file
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        for item in data:

            text = (
                item.get("title", "")
                +
                item.get("content", "")
            )


            for word in keywords:

                if word.lower() in text.lower():

                    counter[word] += 1



with open(
    "opportunity_report.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "# AI机会排行榜\n\n"
    )

    f.write(
        f"统计历史文件：{len(files)}\n\n"
    )


    for i, (word, count) in enumerate(
        counter.most_common(10),
        1
    ):

        score = min(
            count * 10 + weights.get(word, 0),
            100
        )


        f.write(
            f"## {i}. {word}\n\n"
        )

        f.write(
            f"- 出现次数：{count}\n"
        )

        f.write(
            f"- 热度评分：{score}/100\n\n"
        )

        f.write(
            "---\n\n"
        )


print(
    "机会排行榜生成完成：opportunity_report.md"
)