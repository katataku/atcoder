# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

h, w = map(int, input().split())

q = int(input())

d = {}


def find(a):
    if a in d:
        if d[a] != d[d[a]]:
            d[a] = find(d[a])
        return d[a]
    else:
        return -1


def union(a, b):
    if find(a) != find(b):
        if find(a) < find(b):
            a, b = b, a
        d[find(b)] = find(a)


def calc(r, c):
    global w
    return r * w + c


for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        r = a[1]
        c = a[2]
        d[calc(r, c)] = calc(r, c)
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in dir:
            if 1 <= c + dx <= w and calc(r + dy, c + dx) in d:
                union(calc(r, c), calc(r + dy, c + dx))
    if a[0] == 2:
        r1 = a[1]
        c1 = a[2]
        r2 = a[3]
        c2 = a[4]
        if (
            calc(r1, c1) in d
            and calc(r2, c2) in d
            and find(calc(r1, c1)) == find(calc(r2, c2))
        ):
            print("Yes")
        else:
            print("No")
