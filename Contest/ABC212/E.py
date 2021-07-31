# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(1000000)
MOD = 998244353
n, m, k = map(int, input().split())


d = {}
for i in range(n):
    d[i] = [i]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append(v)
    d[v].append(u)

memo = [{} for j in range(k + 1)]


def solve(k, pos):
    if pos in memo[k]:
        return memo[k][pos]
    if k == 1:
        if 0 not in d[pos]:
            memo[k][pos] = 1
        else:
            memo[k][pos] = 0
    else:
        ans = 0
        for i in range(n):
            if i not in d[pos]:
                ans += solve(k - 1, i)
        memo[k][pos] = ans % MOD
    return memo[k][pos]


ans = solve(k, 0)

print(ans % MOD)
