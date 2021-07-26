# -*- coding: utf-8 -*-
# 整数の入力

n = int(input())


cnt = 0

if n % 2 == 0:
    cnt = -1
else:
    for i in range(n):
        tar = int("7" * i)
        if tar % n == 0:
            cnt = i
            break

print("{}".format(cnt))
