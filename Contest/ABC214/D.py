import sys
import itertools
from collections import deque
import heapq

INF = 10 ** 10
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n = int(input())

d = {}
cnt = {}


def find(a):
    if a in d:
        if d[a] != d[d[a]]:
            d[a] = find(d[a])
    else:
        d[a] = a
    return d[a]


def union(a, b):
    if find(a) != find(b):
        if find(a) > find(b):
            a, b = b, a
        d[find(b)] = find(a)


h_q = []
heapq.heapify(h_q)
d_path = {}
for i in range(n - 1):
    u, v, w = map(int, input().split())
    cnt[u] = 1
    cnt[v] = 1
    heapq.heappush(h_q, w)
    d_path[w] = d_path.get(w, [])
    d_path[w].append((u, v))

ans = 0
while len(h_q) > 0:
    w = heapq.heappop(h_q)
    u, v = d_path[w].pop(0)
    ans += w * (cnt[find(u)]) * (cnt[find(v)])
    tmp = cnt[find(u)] + cnt[find(v)]
    union(u, v)
    cnt[find(u)] = tmp

print(ans)