# -*- coding: utf-8 -*-
import math
import heapq
from collections import deque
import itertools

h, w = map(int, input().split())

sy, sx = (1, 1)
gy, gx = (h, w)

c = []
c.append(["#" for i in range(w + 2)])
black_cnt = 0
white_cnt = 0

for i in range(h):
    s = input()
    black_cnt += s.count("#")
    white_cnt += s.count(".")
    s = list("#" + s + "#")
    c.append(s)
c.append(["#" for i in range(w + 2)])


d = deque()
d.append((sy, sx))
ans = -1
c[sy][sx] = "0"

while len(d) > 0:
    tary, tarx = d.popleft()
    if tary == gy and tarx == gx:
        ans = white_cnt - int(c[gy][gx]) - 1
        break
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if tary + dy <= h and tarx + dx <= w and c[tary + dy][tarx + dx] == ".":
            c[tary + dy][tarx + dx] = str(int(c[tary][tarx]) + 1)
            d.append((tary + dy, tarx + dx))


print(ans)