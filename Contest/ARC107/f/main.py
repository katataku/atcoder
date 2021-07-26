# -*- coding: utf-8 -*-

# Input
n = int(input())
# n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = dp(0, a[0], a[1])
memo[]

def dp(i, x, y):
    if i == n - 1:
        if x == y and y == a[n - 1]:
            return 1
        else:
            return 0
    else:
        p = a[i * 3]
        q = a[i * 3 + 1]
        r = a[i * 3 + 2]
        if p == q and q == r:
            return dp(i + 1, x, y) + 1
        elif p == q or q == r or p == r:
            return 0



print("{}".format(ans))
