# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
INF = 10 ** 10


# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))


def solve(n, m, a, b):
    if sum(a) != sum(b):
        print("0")
        exit()

    def cmb(n, r, MOD):
        A = 1
        B = 1
        for i in range(1, r + 1):
            A = A * (n - i + 1) % MOD
            B = B * i % MOD
        return (A * pow(B, MOD - 2, MOD)) % MOD

    ans = 0
    cur = 0
    left_num_total = 0
    right_num_total = 0
    pow_2_total = 0
    for item in a:
        # item = 3
        cnt = 0
        prev = cur
        base = -1
        while cur < m and cnt < item:
            if b[cur] > 1:
                if base != -1:
                    print("0")
                    exit()
                base = cur
            cnt += b[cur]
            if cnt > item:
                print("0")
                exit()
            cur += 1
        if cnt != item:
            print("0")
            exit()
        if base != -1:
            left_num_total += base - prev
            right_num_total += cur - base - 1
        if base == -1:
            pow_2_total += cur - prev - 1

    for i in range(0, pow_2_total + 1):
        # i回左
        tar = cmb(
            left_num_total + right_num_total + pow_2_total,
            left_num_total + i,
            998244353,
        )
        ans += tar
        print("cmb:" + str(tar))
    if cur <= m - 1:
        print("0")
        exit()

    print(ans % 998244353)


n, m = 2, 6
a = [4, 3]
b = [1, 2, 1, 1, 1, 1]
print(n, m, a, b)
solve(n, m, a, b)


n, m = 1, 5
a = [5]
b = [1, 1, 1, 1, 1]
print(n, m, a, b)
solve(n, m, a, b)
