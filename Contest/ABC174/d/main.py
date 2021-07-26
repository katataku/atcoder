# -*- coding: utf-8 -*-
# 整数の入力

n = int(input())
c = input()
# c = list(map(int, input().split()))


r_max = 0
w_min = n - 1

cnt = 0

while r_max < w_min:
    if c[r_max] == "R":
        r_max += 1
        continue
    elif c[w_min] == "W":
        w_min -= 1
        continue
    else:
        cnt += 1
        r_max += 1
        w_min -= 1


print("{}".format(cnt))
