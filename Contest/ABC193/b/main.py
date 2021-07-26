# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n = int(input())
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# h, w = map(int, input().split())

ans = 10 ** 10
for i in range(n):
    a, p, x = map(int, input().split())
    if x - a > 0:
        ans = min(ans, p)

if ans == 10 ** 10:
    ans = -1

print(ans)
