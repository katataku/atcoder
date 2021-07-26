# -*- coding: utf-8 -*-
# Input#
n = int(input())
# n, k = map(int, input().split())
h = list(map(int, input().split()))

h = [-1] + h

ans = 0

memo = [-1] * (n + 1)
memo[1] = 0
memo[2] = abs(h[2] - h[1])


def dp(i):
    if memo[i] != -1:
        return memo[i]
    else:
        hop1 = dp(i - 1) + abs(h[i] - h[i - 1])
        hop2 = dp(i - 2) + abs(h[i] - h[i - 2])
        memo[i] = min(hop1, hop2)
        return memo[i]


for i in range(n):
    if i == 0 or i == 1 or i == 2:
        continue
    hop1 = memo[i - 1] + abs(h[i] - h[i - 1])
    hop2 = memo[i - 2] + abs(h[i] - h[i - 2])
    memo[i] = min(hop1, hop2)

ans = dp(n)

print("{}".format(ans))
