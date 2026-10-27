# -*- coding: utf-8 -*-
# 实验（三）：研究期末考试前行为 —— 朴素贝叶斯分类（纯 Python 实现）
# 任务：根据学生期末考试前的行为特征（是否制定复习计划、是否熬夜、是否刷题），
#       预测其考前状态（"准备充分" 或 "焦虑临考"）。

import math

# ---------------- 1. 构造训练数据集 ----------------
# 特征顺序: (制定复习计划, 熬夜, 刷题)  取值: 是/否
# 标签: 充分 / 焦虑
train = [
    (("是", "否", "是"), "充分"),
    (("是", "否", "是"), "充分"),
    (("是", "是", "是"), "充分"),
    (("是", "否", "否"), "充分"),
    (("否", "是", "否"), "焦虑"),
    (("否", "是", "否"), "焦虑"),
    (("否", "是", "是"), "焦虑"),
    (("否", "否", "否"), "焦虑"),
    (("是", "是", "否"), "焦虑"),
    (("是", "否", "是"), "充分"),
]

features = ["复习计划", "熬夜", "刷题"]
labels = ["充分", "焦虑"]

# ---------------- 2. 统计先验概率与条件概率 ----------------
label_count = {y: 0 for y in labels}
cond_count = {y: [{}, {}, {}] for y in labels}  # 每个标签下每个特征各取值的计数

for x, y in train:
    label_count[y] += 1
    for j, v in enumerate(x):
        d = cond_count[y][j]
        d[v] = d.get(v, 0) + 1

N = len(train)
prior = {y: label_count[y] / N for y in labels}          # 先验概率 P(Y)
print("=== 训练数据统计 ===")
print("样本总数:", N)
for y in labels:
    print(f"先验概率 P({y}) = {label_count[y]}/{N} = {prior[y]:.3f}")

# 拉普拉斯平滑: P(Xi=xi|Y) = (count+1) / (label_count + 该特征取值数)
values = ["是", "否"]
def cond_prob(y, j, v):
    cnt = cond_count[y][j].get(v, 0)
    return (cnt + 1) / (label_count[y] + len(values))    # 平滑后条件概率

# ---------------- 3. 朴素贝叶斯预测 ----------------
def predict(x):
    print(f"\n=== 预测样本 {x} ===")
    scores = {}
    for y in labels:
        p = prior[y]
        terms = [f"P({y})={p:.3f}"]
        for j, v in enumerate(x):
            pc = cond_prob(y, j, v)
            p *= pc
            terms.append(f"P({features[j]}={v}|{y})={pc:.3f}")
        scores[y] = p
        print("  " + " × ".join(terms) + f"  =>  {p:.5f}")
    best = max(scores, key=scores.get)
    print(f"判定：P({best}) 最大，该学生考前状态预测为【{best}】")
    return best

# ---------------- 4. 对三类典型学生进行预测 ----------------
cases = [
    ("是", "否", "是"),   # 制定了计划、不熬夜、坚持刷题
    ("否", "是", "否"),   # 没计划、熬夜、不刷题
    ("否", "否", "是"),   # 没计划、不熬夜、刷题
]
for c in cases:
    predict(c)
