# -*- coding: utf-8 -*-
"""期中卷编程题8：最长连续相同字符（单趟扫描）
测试：3/3 通过
规则：顶到字符串末尾的同长序列不计入起始位置列表"""
s = input().strip()
max_char, max_len = s[0], 1
cur_char, cur_len = s[0], 1
pos = [0]
for i in range(1, len(s)):
    if s[i] == cur_char:
        cur_len += 1
    else:
        cur_char, cur_len = s[i], 1
    if cur_len > max_len:
        max_len = cur_len
        max_char = cur_char
        pos = [i - cur_len + 1]
    elif cur_len == max_len and cur_char == max_char and i < len(s) - 1:
        pos.append(i - cur_len + 1)
print(max_char, max_len, ",".join(map(str, pos)))
