# -*- coding: utf-8 -*-
# 输入输出与类型转换演示：输入两个整数，输出和与平均值
a, b = map(int, input().split())
print("和:%d 平均值:%.2f" % (a + b, (a + b) / 2))
