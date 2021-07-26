# -*- coding: utf-8 -*-
from functools import reduce
import math

# Input#
n = int(input())
# n, k = map(int, input().split())
a = list(map(int, input().split()))
# memo = [-1 for i in range(10 ** len(n) + 1)]
memo = [0 for i in range(401)]

ans = 0
for i in range(n):
    memo[a[i] + 200] += 1

for i in range(401):
    if memo[i] == 0:
        continue
    else:
        j = i + 1
        while j <= 400:
            if memo[j] != 0:
                tmp = ((i - 200) - (j - 200)) ** 2
                ans += tmp * memo[i] * memo[j]
            j += 1

print("{}".format(ans))
