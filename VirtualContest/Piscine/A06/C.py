# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n, p = map(int, input().split())


def prime_f_multi(n, num):
    ans = 1
    divisors = {}
    for i in range(2, num):
        k = 0
        while (num % i) == 0:
            k += 1
            num //= i
        if k != 0 and k // n > 0:
            ans *= i * (k // n)
    if not divisors and num != 1:
        divisors[num] = 1
    return ans


print(prime_f_multi(n, p))
