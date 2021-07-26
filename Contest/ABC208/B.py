# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


n = int(input())
ans = 0
tar = 10
current_coin = 0
rest = n
while True:
    if rest == 0:
        break
    if math.factorial(tar) > rest or current_coin == 10:
        tar -= 1
        current_coin = 0
        continue
    ans += 1
    current_coin += 1
    rest -= math.factorial(tar)
print(ans)
