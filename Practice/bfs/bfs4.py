# -*- coding: utf-8 -*-
import math
import heapq
from collections import deque
import itertools


n, q = map(int, input().split())
d_path = {}

anslist = [0 for i in range(n)]
for i in range(n):
    d_path[i + 1] = []


for i in range(n - 1):
    a, b = map(int, input().split())
    d_path[a].append(b)
    d_path[b].append(a)

for i in range(q):
    p, x = map(int, input().split())
    anslist[p - 1] += x

d = deque()

d.append((1, -1))
while len(d) > 0:
    tar_node, prev_node = d.popleft()
    next_nodes = d_path[tar_node]
    for next_node in [n for n in next_nodes if n != prev_node]:
        d.append((next_node, tar_node))
        anslist[next_node - 1] += anslist[tar_node - 1]

print(" ".join(map(str, anslist)))
