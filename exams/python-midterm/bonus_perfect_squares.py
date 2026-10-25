# -*- coding: utf-8 -*-
"""期中卷附加题：完全平方数分解的最少数量（多重循环枚举）
测试：4/4 通过"""
n = int(input())
squares = [0] + [i * i for i in range(1, 11)]
ans = 4
for a in squares:
    for b in squares:
        for c in squares:
            for d in squares:
                if a + b + c + d == n:
                    ans = min(ans, (a > 0) + (b > 0) + (c > 0) + (d > 0))
print(ans)
