# -*- coding: utf-8 -*-

f_inf = float("inf")

# Input#
x, y, a, b = map(int, input().split())
ans = 0

p = x

while (p * a) < y and p <= b / (a - 1):
    p *= a
    ans += 1

if p + b < y:
    tmp = (y - p) / b
    ans += tmp
    if b * tmp >= y - p - 1:
        ans -= 1


print("{}".format(ans))
