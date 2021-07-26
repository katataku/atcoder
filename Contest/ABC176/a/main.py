# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())
n, x, t = map(int, input().split())
# a = list(map(int, input().split()))

ans = math.ceil(n / x) * t

print("{}".format(ans))
