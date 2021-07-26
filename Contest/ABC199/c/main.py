# -*- coding: utf-8 -*-
from functools import reduce
import math

# Input#
n = int(input())
s = input()
q = int(input())


for _ in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        a -= 1
        b -= 1
        if s[a] != s[b]:
            if len(s) > b + 1:
                if a == 0:
                    tmp = s[b] + s[1:b] + s[0] + s[b + 1 :]
                else:
                    tmp = s[0:a] + s[b] + s[a + 1 : b] + s[a] + s[b + 1 :]
            else:
                if a == 0:
                    tmp = s[b] + s[1:b] + s[0]
                else:
                    tmp = s[0:a] + s[b] + s[a + 1 : b] + s[a]
            s = tmp
    else:
        tmp = s[n:] + s[0:n]
        s = tmp

print("{}".format(s))
