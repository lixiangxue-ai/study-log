# -*- coding: utf-8 -*-
"""期中卷编程题2：成绩等级判断
测试：5/5 通过"""
score = int(input())
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")
