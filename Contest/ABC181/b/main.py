# -*- coding: utf-8 -*-
import math

# Input#
n = int(input())
# n, k = map(int, input().split())
# h, w = map(int, input().split())
# x = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    x_in, y_in = map(int, input().split())
    x.append(x_in)
    y.append(y_in)

ans = "No"
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (x[k] - x[i]) * (y[j] - y[i]) == (x[j] - x[i]) * (y[k] - y[i]):
                ans = "Yes"
                print("{}".format(ans))
                exit(0)

print("{}".format(ans))
