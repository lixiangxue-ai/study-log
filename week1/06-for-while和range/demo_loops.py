# -*- coding: utf-8 -*-
# 循环演示：奇数累加 与 阶乘
total = 0
for i in range(1, 101, 2):
    total += i
print("1~100奇数和:", total)   # 2500

n = int(input())
r = 1
for i in range(1, n + 1):
    r *= i
print(n, "! =", r)
