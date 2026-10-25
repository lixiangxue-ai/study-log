# -*- coding: utf-8 -*-
# 常见报错复现集：逐个取消注释即可复现对应错误（学习用，默认全部注释）

# 1. SyntaxError —— if 后面少冒号
# if 1 > 0
#     print("ok")

# 2. NameError —— 变量名拼写错误
# score = 90
# print(sorce)

# 3. TypeError —— 字符串与整数相加
# print("abc" + 1)

# 4. ValueError —— int() 转换非法内容
# n = int("abc")

# 5. IndexError —— 下标越界
# s = "ab"
# print(s[5])

# 6. IndentationError —— 缩进不一致
# for i in range(3):
# print(i)
