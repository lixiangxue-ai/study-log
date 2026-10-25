# -*- coding: utf-8 -*-
"""期中卷编程题6：最小元素换到首位（不使用排序函数）
测试：1/1 通过"""
nums = [int(x) for x in input().split()]
mi = 0
for i in range(1, len(nums)):
    if nums[i] < nums[mi]:
        mi = i
nums[0], nums[mi] = nums[mi], nums[0]
print(nums)
