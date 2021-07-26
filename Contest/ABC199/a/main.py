# -*- coding: utf-8 -*-
import math

# Input#
a, b, c = map(int, input().split())
# n = int(input())
# a = a + b
# n, s,d = map(int, input().split())
# h, w = map(int, input().split())

ans = "No"
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

if c - b == b - a:
    ans = "Yes"

print(ans)
