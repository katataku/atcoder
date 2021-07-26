# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, m = map(int, input().split())

s = input()
t = input()


ans = n * m // math.gcd(n, m)

for i in range(math.gcd(n, m)):
    if s[i * n // math.gcd(n, m)] != t[i * m // math.gcd(n, m)]:
        ans = -1
        break
print(ans)