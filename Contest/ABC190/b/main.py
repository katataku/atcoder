# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n, s,d = map(int, input().split())
# h, w = map(int, input().split())

ans = "No"
for i in range(n):
    x_in, y_in = map(int, input().split())

    if x_in < s and y_in > d:
        ans = "Yes"
        break


print("{}".format(ans))

