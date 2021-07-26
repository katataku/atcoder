# -*- coding: utf-8 -*-
from functools import reduce
import math

# Input#
# n = int(input())
r, x, y = map(int, input().split())
# a = list(map(int, input().split()))
# memo = [-1 for i in range(10 ** len(n) + 1)]
# memo = [0 for i in range(401)]

dist = (x ** 2 + y ** 2) ** 0.5
ans = int(dist // r)
if dist % r != 0:
    ans += 1

if dist < r:
    ans = 2

print("{}".format(ans))
