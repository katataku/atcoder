# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())
a, b = map(int, input().split())
# a = list(map(int, input().split()))
x = int((a + b) / 2)
y = int(a - x)

ans = str(x) + " " + str(y)

print("{}".format(ans))
