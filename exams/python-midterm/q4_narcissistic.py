# -*- coding: utf-8 -*-
"""期中卷编程题4：三位水仙花数
测试：1/1 通过"""
for n in range(100, 1000):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if a**3 + b**3 + c**3 == n:
        print(n)
