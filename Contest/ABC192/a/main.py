# -*- coding: utf-8 -*-
import math

# Input#
# v, t, s, d = map(int, input().split())
n = int(input())

# n, s,d = map(int, input().split())
# h, w = map(int, input().split())
ans = ""
if n % 100 == 0:
    ans = 100
else:
    ans = 100 - (n % 100)
print(ans)
