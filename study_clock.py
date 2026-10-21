# -*- coding: utf-8 -*-
"""
study_clock.py —— 学习打卡小工具
用法：每天学完习，运行它记一笔，自动追加到 study_log.txt
"""
import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "study_log.txt")


def add_record(subject: str, minutes: int, note: str = "") -> None:
    """写入一条打卡记录"""
    now = datetime.datetime.now()
    line = f"{now:%Y-%m-%d %H:%M} | {subject:<10} | {minutes:>4} 分钟 | {note}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print("✅ 打卡成功：", line)


def show_records() -> None:
    """查看全部打卡记录和总时长"""
    if not os.path.exists(LOG_FILE):
        print("还没有打卡记录，快开始今天的学习吧！")
        return
    total = 0
    print("-" * 60)
    with open(LOG_FILE, encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())
            try:
                total += int(line.split("|")[2].strip().split()[0])
            except (IndexError, ValueError):
                pass
    print("-" * 60)
    print(f"📚 累计学习时长：{total} 分钟（约 {total / 60:.1f} 小时）")


if __name__ == "__main__":
    print("=== 学习打卡工具 ===")
    print("1. 打卡  2. 查看记录")
    choice = input("请选择：").strip()
    if choice == "1":
        subject = input("今天学了什么：").strip()
        minutes = int(input("学了多少分钟：").strip())
        note = input("一句话备注（可回车跳过）：").strip()
        add_record(subject, minutes, note)
    elif choice == "2":
        show_records()
    else:
        print("输入无效，下次见～")
