# -*- coding: utf-8 -*-
# Input#
import math
from functools import reduce


n = int(input())

ans = 1
for i in range(1, n):
    t1 = ans * i / n
    t2 = (n - i) / n * (n / (i) + ans)
    ans = t1 + t2
print("{}".format(ans))
