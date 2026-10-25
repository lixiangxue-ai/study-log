# -*- coding: utf-8 -*-
"""期中卷编程题1：输入两个整数，输出较大数与两数之和
测试：3/3 通过"""
a, b = map(int, input().split())
print("较大数:%d" % max(a, b))
print("和:%d" % (a + b))
