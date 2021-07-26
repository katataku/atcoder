# -*- coding: utf-8 -*-
# Input#
# n = int(input())
A, B, C = map(int, input().split())

memo = [[[-1] * 101 for i in range(101)] for i in range(101)]


def dp(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0
    if memo[a][b][c] == -1:
        mother = a + b + c
        memo[a][b][c] = 0
        if a > 0:
            p_a = (1 + dp(a + 1, b, c)) * a / mother
            memo[a][b][c] += p_a
        if b > 0:
            p_b = (1 + dp(a, b + 1, c)) * b / mother
            memo[a][b][c] += p_b
        if c > 0:
            p_c = (1 + dp(a, b, c + 1)) * c / mother
            memo[a][b][c] += p_c

    # print("memo {} {} {}={}".format(a, b, c, memo[a][b][c]))
    return memo[a][b][c]


ans = dp(A, B, C)

print("{}".format(ans))
