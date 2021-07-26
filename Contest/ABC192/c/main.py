# -*- coding: utf-8 -*-
from functools import reduce

# Input#
# N = int(input())
n, k = map(int, input().split())


# memo = [-1 for i in range(10 ** len(n) + 1)]


def func(n):
    #    if memo[n] == -1:
    sortedn = sorted(str(n))
    g2 = reduce(lambda x, y: int(x) * 10 + (int(y)), sortedn)
    g1 = reduce(lambda x, y: int(x) * 10 + (int(y)), reversed(sortedn))
    return int(g1) - int(g2)


#        memo[n] = g1 - g2
#   return memo[n]


ans = n
for i in range(k):
    ansold = ans
    ans = func(ans)
    if ansold == ans:
        break

print("{}".format(ans))
