# -*- coding: utf-8 -*-
# 整数の入力

n, ｄ = map(int, input().split())

cnt = 0
for i in range(n):
    x, y = map(int, input().split())
    if x * x + y * y <= d + d:
        cnt += 1


print("{}".format(cnt))
