# -*- coding: utf-8 -*-
# 运算符行为观察
print(10 / 3)    # 3.3333333333333335
print(10 // 3)   # 3
print(10 % 3)    # 1
print(9 ** 0.5)  # 3.0（注意是浮点数！）
print(7 // 2 + 7 % 2)      # 4
print(3 > 2 and 2 > 1)     # True
print(0 < 5 < 10)          # True（链式比较）
print(1 == 1.0)            # True（值相等，类型不同）
