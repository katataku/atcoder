# -*- coding: utf-8 -*-
import math

# Input#
n = int(input())

# n, k = map(int, input().split())
# h, w = map(int, input().split())
a = list(map(int, input().split()))

ans = 2
max_cnt = 0
for i in range(2, max(a) + 1):
    tar_cnt = 0
    for item in a:
        if item % i == 0:
            tar_cnt += 1
    if max_cnt <= tar_cnt:
        ans = i
        max_cnt = tar_cnt


print("{}".format(ans))
