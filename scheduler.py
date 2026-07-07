import time
import subprocess
import sys
from datetime import datetime


while True:

    now = datetime.now()

    print(
        "当前时间：",
        now.strftime("%Y-%m-%d %H:%M:%S")
    )


    # 测试时使用 True
    # 正式运行改回：
    # if now.hour == 9 and now.minute == 0:

    if now.hour == 9 and now.minute == 0:

        print("开始自动研究任务")


        # 运行搜索任务
        subprocess.run(
            [
                sys.executable,
                "main.py",
                "AI自动化赚钱项目"
            ]
        )


        # 生成报告
        subprocess.run(
            [
                sys.executable,
                "generate_report.py"
            ]
        )


        # 项目评分
        subprocess.run(
            [
                sys.executable,
                "score_projects.py"
            ]
        )


        print(
            "任务完成"
        )


        # 防止一直重复运行
        time.sleep(70)


    time.sleep(30)