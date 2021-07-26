# -*- coding: utf-8 -*-

# Input#
L = int(input())
# n, k = map(int, input().split())
# p = list(map(int, input().split()))


memo = [[-1] * (12 + 1) for i in range(L + 1)]


def check(length, count):
    if memo[length][count] == -1:
        if count == 1:
            memo[length][count] = 1
            return 1

        if length == count:
            memo[length][count] = 1
            return 1

        ans = 0
        for i in range(1, length - count + 2):
            ans += check(length - i, count - 1)
        memo[length][count] = ans
    return memo[length][count]


ans = check(L, 12)

print("{}".format(ans))

