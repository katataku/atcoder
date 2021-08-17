# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

h, w = map(int, input().split())

m = []

start_r, start_c = map(int, input().split())
goal_r, goal_c = map(int, input().split())
m.append(["#" for i in range(w + 2)])
for i in range(h):
    a = list(input())
    a.insert(0, "#")
    a.append("#")
    m.append(a)
m.append(["#" for i in range(w + 2)])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d = deque()
m[start_r][start_c] = -1
d.append((start_r, start_c))
while m[goal_r][goal_c] == ".":
    tar_r, tar_c = d.popleft()
    for d_r, d_c in directions:
        cnt = 1
        while True:
            if m[tar_r + (d_r * cnt)][tar_c + (d_c * cnt)] != "#":
                if m[tar_r + (d_r * cnt)][tar_c + (d_c * cnt)] == ".":
                    m[tar_r + (d_r * cnt)][tar_c + (d_c * cnt)] = m[tar_r][tar_c] + 1
                    d.append((tar_r + (d_r * cnt), tar_c + (d_c * cnt)))
                if m[tar_r + (d_r * cnt)][tar_c + (d_c * cnt)] < m[tar_r][tar_c] + 1:
                    break
                cnt += 1
            else:
                break

print(m[goal_r][goal_c])