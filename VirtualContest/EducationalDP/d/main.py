# -*- coding: utf-8 -*-

# Input#
# n = int(input())
n, tar_w = map(int, input().split())

w = [-1]
v = [-1]

memo = [[-1] * (tar_w + 1) for i in range(n + 1)]

for i in range(tar_w + 1):
    memo[0][i] = 0


def dp(n, tar_w):
    if memo[n][tar_w] == -1:
        if tar_w < w[n]:
            memo[n][tar_w] = dp(n - 1, tar_w)
        else:
            memo[n][tar_w] = max(dp(n - 1, tar_w), dp(n - 1, tar_w - w[n]) + v[n])
    return memo[n][tar_w]


for i in range(n):
    w_in, v_in = list(map(int, input().split()))
    w.append(w_in)
    v.append(v_in)

for i in range(n):
    ans = dp(i, tar_w)

ans = dp(n, tar_w)

print("{}".format(ans))
