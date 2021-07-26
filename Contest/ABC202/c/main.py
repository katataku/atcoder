# -*- coding: utf-8 -*-
from functools import reduce
import math

a, b, k = map(int, input().split())
ans = ""


def cmb(n, r):
    A = 1
    B = 1
    for i in range(1, r + 1):
        A = A * (n - i + 1)
        B = B * i
    return A // B


while (a + b) > 0:
    if b == 0:
        ans = ans + "a" * a
        break
    elif a == 0:
        ans = ans + "b" * b
        break
    else:
        c = cmb(a + b - 1, min(a - 1, b))
        if c < k:
            ans += "b"
            b -= 1
            k -= c
        else:
            ans += "a"
            a -= 1


print(ans)
