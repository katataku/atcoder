import math
import heapq
import sys
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


n, k, l = map(int, input().split())
parentlist = [i for i in range(n)]
sizelist = [1 for i in range(n)]


def size(a):
    return sizelist[parent(a)]


def parent(a):
    if a != parentlist[a]:
        parentlist[a] = parent(parentlist[a])
    return parentlist[a]


def find(a, b):
    if parent(a) == parent(b):
        return True
    else:
        return False


def union(a, b):
    global ans
    if parent(a) == parent(b):
        pass
    else:
        if parent(a) > parent(b):
            a, b = b, a
        sizelist[parent(a)] += size(parent(b))
        parentlist[parent(b)] = parent(a)


roadlist = []

for i in range(k):
    a, b = map(int, input().split())
    roadlist.append((a, b))


for i in range(l):
    a, b = map(int, input().split())
    if (a, b) in roadlist:
        union(a - 1, b - 1)

ans = []
for i in range(n):
    ans.append(size(i))
print(" ".join(map(str, ans)))
