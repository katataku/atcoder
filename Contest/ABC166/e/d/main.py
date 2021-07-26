# -*- coding: utf-8 -*-
# 整数の入力

n = int(input())
a = list(map(int, input().split()))


cnt = 0

for i in range(n - 1):
    if a[i] < 200000:
        for j in range(i + 1, n):
            if j - i == a[i] + a[j]:
                cnt += 1

print("{}".format(cnt))
