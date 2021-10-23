import math
import heapq
import sys
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


n, m = map(int, input().split())
alist = []
blist = []

for i in range(m):
    a, b = map(int, input().split())
    alist.append(a)
    blist.append(b)


def compress(a):
    if a != parent[a]:
        parent[a] = compress(parent[a])
    return parent[a]


def find(a, b):
    if parent[a] == parent[b]:
        return True
    else:
        return False


def union(a, b):
    compress(a)
    compress(b)
    if parent[a] > parent[b]:
        a, b = b, a
    parent[parent[b]] = parent[a]
    compress(a)
    compress(b)


ans = 0

for bridge in range(m):
    parent = [i + 1 for i in range(n)]
    parent.insert(0, 1)
    for query in range(m):
        if bridge == query:
            continue
        else:
            union(alist[query], blist[query])
    for i in range(len(parent)):
        compress(i)

    if parent.count(1) != n + 1:
        ans += 1

print(ans)
