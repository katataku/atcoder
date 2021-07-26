# -*- coding: utf-8 -*-
# Input#
n = int(input())
# n, k = map(int, input().split())

memo = [[-1] * 3 for i in range(n)]
a = []
b = []
c = []


def dp(i):
    if i != 0:
        memo[i][0] = max(memo[i - 1][1], memo[i - 1][2]) + a[i]
        memo[i][1] = max(memo[i - 1][0], memo[i - 1][2]) + b[i]
        memo[i][2] = max(memo[i - 1][0], memo[i - 1][1]) + c[i]
    return max(memo[i][0], memo[i][1], memo[i][2])


for i in range(n):
    a_in, b_in, c_in = map(int, input().split())
    a.append(a_in)
    b.append(b_in)
    c.append(c_in)
    if i == 0:
        memo[0][0] = a_in
        memo[0][1] = b_in
        memo[0][2] = c_in
    else:
        ans = dp(i)


ans = dp(n - 1)

print("{}".format(ans))
