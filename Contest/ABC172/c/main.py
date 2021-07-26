# -*- coding: utf-8 -*-
# 整数の入力

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1] * (m + 1) for i in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    dp[i + 1][0] = dp[i][0] + a[i]

for i in range(m):
    dp[0][i + 1] = dp[0][i] + b[i]

ans = 0

j = m + 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i][0] + dp[0][j]
        if dp[i][j] > k:
            break
        else:
            ans = max(ans, i + j)


print("{}".format(ans))
