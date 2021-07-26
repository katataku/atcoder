# -*- coding: utf-8 -*-
# 整数の入力

n = int(input())
a = list(map(int, input().split()))

a.sort()
cnt = 0

while 0 != len(a):
    if len(a) == 1:
        cnt += 1
        break

    tmp = []
    if a[0] < a[1]:
        cnt += 1

    for i in range(len(a)):
        if a[i] % a[0] != 0:
            tmp.append(a[i])

    a = tmp[:]

print("{}".format(cnt))
