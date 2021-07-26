# -*- coding: utf-8 -*-
import math

# Input#
a, b = map(int, input().split())
# n = int(input())

# n, s,d = map(int, input().split())
# h, w = map(int, input().split())
ans = 1 - (b / a)
print(ans * 100)
