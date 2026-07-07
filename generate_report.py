import json


with open(
    "research.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)


with open(
    "report.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# AI项目研究报告\n\n")

    for i, item in enumerate(data, 1):

        f.write(f"## {i}. {item['title']}\n\n")

        f.write("网址：\n")
        f.write(item["url"])
        f.write("\n\n")

        f.write("内容：\n")
        f.write(item["content"][:1000])
        f.write("\n\n---\n\n")


print("报告生成完成：report.md")