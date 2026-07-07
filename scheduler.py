import time
import subprocess
import sys
import os
from datetime import datetime


os.makedirs(
    "logs",
    exist_ok=True
)


def write_log(message):

    filename = datetime.now().strftime(
        "logs/%Y-%m-%d.log"
    )

    with open(
        filename,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"{datetime.now()} - {message}\n"
        )


while True:

    now = datetime.now()

    print(
        "当前时间：",
        now.strftime("%Y-%m-%d %H:%M:%S")
    )


    # 测试阶段
    # 完成测试后改回每天9点
    if True:


        print("开始自动研究任务")

        write_log(
            "开始自动研究任务"
        )


        try:

            subprocess.run(
                [
                    sys.executable,
                    "main.py",
                    "AI自动化赚钱项目"
                ]
            )


            subprocess.run(
                [
                    sys.executable,
                    "generate_report.py"
                ]
            )


            subprocess.run(
                [
                    sys.executable,
                    "score_projects.py"
                ]
            )


            write_log(
                "任务完成"
            )


            print(
                "任务完成"
            )


        except Exception as e:

            write_log(
                f"错误: {e}"
            )

            print(
                "发生错误:",
                e
            )


        time.sleep(70)


    time.sleep(30)