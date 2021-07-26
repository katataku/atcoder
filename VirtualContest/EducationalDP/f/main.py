# -*- coding: utf-8 -*-

# Input#
# n = int(input())
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

s = input()
t = input()

memo = [[-1 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

for i in range(len(s) + 1):
    memo[i][0] = 0

for i in range(len(t) + 1):
    memo[0][i] = 0


def dp(i, j):
    if memo[i][j] == -1:
        if s[i - 1] == t[j - 1]:
            memo[i][j] = dp(i - 1, j - 1) + 1
        else:
            memo[i][j] = max(dp(i - 1, j), dp(i, j - 1))

    return memo[i][j]


for i in range(max(len(s), len(t))):
    if i > 0:
        for j in range(i):
            tmp = dp(min(abs(i - j), len(s)), min(abs(j - i), len(t)))


max = dp(len(s), len(t))

ans = ""

i = len(s)
j = len(t)

while i > 0 and j > 0:
    if memo[i][j] == memo[i - 1][j - 1] + 1:
        ans = s[i - 1] + ans
        i -= 1
        j -= 1
    elif memo[i][j] == memo[i - 1][j]:
        i -= 1
    else:
        j -= 1

print("{}".format(ans))
