# -*- coding: utf-8 -*-
"""期中卷编程题7：元组综合（构造/最大值下标/元素计数）
测试：1/1 通过"""
nums = [int(x) for x in input().split()]
t = tuple(nums)
print(t)
m = max(t)
print("最大值:%d 首次下标:%d" % (m, t.index(m)))
print("3的次数:%d" % t.count(3))
