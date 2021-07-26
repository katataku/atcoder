# -*- coding: utf-8 -*-
# Input#
# n = int(input())
n, k = map(int, input().split())
h = list(map(int, input().split()))

h = [-1] + h

ans = 0

memo = [-1] * (n + 1)
memo[1] = 0


def dp(i):
    if memo[i] != -1:
        return memo[i]
    else:
        for j in range(k):
            if i - (j + 1) < 1:
                continue
            hop = dp(i - j - 1) + abs(h[i] - h[i - j - 1])
            if memo[i] == -1:
                memo[i] = hop
            else:
                memo[i] = min(hop, memo[i])
        return memo[i]


for i in range(n):
    memo[i] = dp(i)

ans = dp(n)

print("{}".format(ans))
