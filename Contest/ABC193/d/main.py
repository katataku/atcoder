# -*- coding: utf-8 -*-
# Input#
import math
from functools import reduce

x = input()
m = int(input())

d = 9
while d > 0:
    if str(d) in x:
        break
    else:
        d -= 1


def base(d, n):
    return int(reduce(lambda x, y: int(x) * d + (int(y)), str(n)))


ans = 0
mi = d
ma = max(int(x) + 1, m + 1)

if int(x) < 10:
    if int(x) <= m:
        ans += 1
else:
    while mi + 1 != ma:
        tar = (mi + ma) // 2
        if base(tar, x) <= m:
            mi = tar
        else:
            ma = tar
    ans = mi - d

print("{}".format(ans))

