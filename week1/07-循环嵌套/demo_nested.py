# -*- coding: utf-8 -*-
# 循环嵌套演示：下三角九九乘法表
for i in range(1, 10):
    row = []
    for j in range(1, i + 1):
        row.append("%d*%d=%d" % (j, i, i * j))
    print(" ".join(row))
