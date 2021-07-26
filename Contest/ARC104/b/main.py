# -*- coding: utf-8 -*-

# Input#
# n = list(input())
n, s = input().split()
# n, s = map(int, input().split())
# a = list(map(int, input().split()))

n = int(n)
ans = 0

memo = [[-1] * (n + 1) for i in range(n + 1)]


def check(x, y):
    tar = s[x:y]
    num_a = tar.count("A")
    num_t = tar.count("T")
    if num_a != num_t:
        return 0

    num_c = tar.count("C")
    num_g = tar.count("G")
    if num_g != num_c:
        return 0
    else:
        global ans
        ans += 1
        return 1


def dp(x, y):
    if memo[x][y] == -1:
        memo[x][y] = check(x, y)
    return memo[x][y]


tar_len = 2
for i in range(n - tar_len + 1):
    memo[i][i + tar_len] = check(i, i + tar_len)

tar_len = 4
while (tar_len) <= n:
    for i in range(n - tar_len + 1):
        dp(i, i + tar_len)
    tar_len += 2


print("{}".format(ans))
