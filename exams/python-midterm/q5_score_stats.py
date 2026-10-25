# -*- coding: utf-8 -*-
"""期中卷编程题5：成绩统计（平均分/最高分/最低分/及格人数）
测试：1/1 通过"""
data = input().split()
scores = [int(x) for x in data]
print("平均分:%.2f" % (sum(scores) / len(scores)))
print("最高分:%d" % max(scores))
print("最低分:%d" % min(scores))
print("及格人数:%d" % len([x for x in scores if x >= 60]))
