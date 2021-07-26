# -*- coding: utf-8 -*-
import math

# Input#
a, b = map(int, input().split())
# n = int(input())
a = a + b
# n, s,d = map(int, input().split())
# h, w = map(int, input().split())
if a >= 15 and b >= 8:
    ans = 1
else:
    if a >= 10 and b >= 3:
        ans = 2
    else:
        if a >= 3:
            ans = 3
        else:
            ans = 4


print(ans)
