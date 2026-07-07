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


files = []

for file in os.listdir(data_dir):

    if file.endswith(".json"):

        files.append(file)


# 按文件名时间排序
files.sort()


if len(files) < 2:

    print("历史数据不足，需要更多记录")

    exit()


old_files = files[:len(files)//2]

new_files = files[len(files)//2:]


def count_keywords(file_list):

    counter = Counter()


    for file in file_list:

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


    return counter



old_count = count_keywords(old_files)

new_count = count_keywords(new_files)



with open(
    "trend_report.md",
    "w",
    encoding="utf-8"
) as f:


    f.write(
        "# AI机会趋势分析\n\n"
    )


    f.write(
        f"历史样本：{len(files)} 个\n\n"
    )


    trends = []


    for word in keywords:

        old = old_count[word]

        new = new_count[word]


        growth = new - old


        trends.append(
            (
                word,
                old,
                new,
                growth
            )
        )


    trends.sort(
        key=lambda x:x[3],
        reverse=True
    )


    for i, item in enumerate(
        trends[:10],
        1
    ):

        word, old, new, growth = item


        f.write(
            f"## {i}. {word}\n\n"
        )


        f.write(
            f"- 前期出现：{old}\n"
        )

        f.write(
            f"- 后期出现：{new}\n"
        )

        f.write(
            f"- 变化：{growth:+d}\n\n"
        )


        if growth > 0:

            f.write(
                "🔥 上升趋势\n\n"
            )

        elif growth == 0:

            f.write(
                "➡ 稳定\n\n"
            )

        else:

            f.write(
                "⬇ 下降\n\n"
            )


        f.write(
            "---\n\n"
        )


print(
    "趋势分析完成：trend_report.md"
)