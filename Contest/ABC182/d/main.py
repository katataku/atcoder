# -*- coding: utf-8 -*-
import itertools

f_inf = float("inf")

# Input#
n = int(input())

# n, k = map(int, input().split())
# h, w = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
b = []
c = []

accum = 0
a_max = 0
a_neg = -1
for i in range(len(a)):
    if a_neg == -1 and a[i] < a_max:
        a_neg = i
    accum += a[i]
    b.append(accum)

accum = 0
b_neg = -1
for i in range(len(b)):
    if b_neg == -1 and b[i] < 0:
        b_neg = i
    accum += b[i]
    c.append(accum)

epoc = c[1:].index(max(c[1:])) + 1
if epoc == len(c) - 1:
    ans = max(max(c), max(c[:-1]) + max(b[: (epoc + 1)]))
else:
    ans = max(c) + max(b[: (epoc + 1)])


print("{}".format(max(0, ans)))
