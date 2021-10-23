import math
import heapq
import sys
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, m = map(int, input().split())

parentlist = [i for i in range(n)]


def parent(a):
    if a != parentlist[a]:
        parentlist[a] = parent(parentlist[a])
    return parentlist[a]


def find(a):
    return parent(a)


def union(a, b):
    if parent(a) == parent(b):
        pass
    else:
        if parent(a) > parent(b):
            a, b = b, a
        parentlist[parent(b)] = parent(a)


plist = list(map(int, input().split()))

for i in range(m):
    x, y = map(int, input().split())
    union(x - 1, y - 1)

ans = 0
for i in range(n):
    tar = plist[i]
    if find(tar - 1) == find(i):
        ans += 1

print(ans)
