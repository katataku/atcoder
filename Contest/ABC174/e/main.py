# -*- coding: utf-8 -*-
# 整数の入力
import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

b = a[:]
vote = [0] * n
ans = 0


for i in range(k):
    tar = b.index(max(b))
    vote[tar] += 1
    b[tar] = a[tar] / (vote[tar] + 1)

print("{}".format(int(math.ceil(max(b)))))
