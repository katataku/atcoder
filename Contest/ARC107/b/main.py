# -*- coding: utf-8 -*-
import math

# Input#
# n = list(input())
n, k = map(int, input().split())
# h, w = map(int, input().split())
# x = list(map(int, input().split()))

memo = [-1] * (4 * (n + 2))


def calc_pat(tar):
    if memo[tar] == -1:
        cnt = 0
        if tar <= n:
            cnt = tar - 1
        else:
            for i in range(n + 1)[1:]:
                local_tar_plus = i
                local_tar_minus = tar - local_tar_plus
                if local_tar_minus < 1:
                    break
                if local_tar_minus <= (n) and local_tar_minus >= 1:
                    cnt += 1
        memo[tar] = cnt
    return memo[tar]


ans = 0
maxi = max(2 * n - k, 2 * n)
mini = max(2, k + 2)

tar_plus = mini

while tar_plus <= maxi:
    tar_minus = tar_plus - k
    if tar_minus > (2 * n):
        break
    if tar_minus >= 2:
        ans += calc_pat(tar_plus) * calc_pat(tar_minus)
    tar_plus += 1

print("{}".format(ans))
