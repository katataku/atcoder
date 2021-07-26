# -*- coding: utf-8 -*-
import math

# Input#
v, t, s, d = map(int, input().split())
# n = int(input())

# n, s,d = map(int, input().split())
# h, w = map(int, input().split())
# ans = ""

if v * t <= d and v * s >= d:
    ans = "No"
else:
    ans = "Yes"

print(ans)
