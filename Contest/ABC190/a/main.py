# -*- coding: utf-8 -*-
import math

# Input#
a,b,c  = map(int, input().split())

ans = ""

if c== 0:
    if a > b:
        ans = "Takahashi"
    else:
        ans = "Aoki"
else:
    if a >= b:
        ans = "Takahashi"
    else:
        ans = "Aoki"

print(ans)

