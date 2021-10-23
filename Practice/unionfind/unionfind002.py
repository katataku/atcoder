import math
import heapq
import sys
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


n, q = map(int, input().split())
parent = [i for i in range(n)]


def find(a, b):
    if parent[a] == parent[b]:
        return True
    else:
        return False


def union(a, b):
    if parent[a] > parent[b]:
        a, b = b, a
    parent[b] = parent[a]


ans = []
for i in range(q):
    p, a, b = map(int, input().split())
    if p == 0:
        union(a, b)
    else:
        if find(a, b):
            ans.append("Yes")
        else:
            ans.append("No")


print("\n".join(ans))
