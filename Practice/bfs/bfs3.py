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

d = []
d.append(deque())
d.append(deque())
d.append(deque())
ans = "NO"


for i in range(h):
    s = input()
    ind = 0
    if s.find("s") != -1:
        tar = s.find("s", ind)
        sy, sx = (i + 1, tar + 1)
        d[0].append((i + 1, tar + 1))
    if s.find("g") != -1:
        tar = s.find("g", ind)
        gy, gx = (i + 1, tar + 1)

    s = list(("#" + s + "#"))
    c.append(s)
c.append(["#" for i in range(w + 2)])

c[sy][sx] = 0
breakblock = 0
while len(d[breakblock]) > 0 or breakblock < 2:
    if len(d[breakblock]) == 0:
        breakblock += 1
        continue
    else:
        tary, tarx = d[breakblock].popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if tary + dy == gy and tarx + dx == gx:
                ans = "YES"
                break
            if tary + dy >= 1 and tary + dy <= h and tarx + dx >= 1 and tarx + dx <= w:
                if c[tary + dy][tarx + dx] == ".":
                    c[tary + dy][tarx + dx] = str(int(c[tary][tarx]) + 1)
                    d[breakblock].append((tary + dy, tarx + dx))

                if c[tary + dy][tarx + dx] == "#" and breakblock < 2:
                    c[tary + dy][tarx + dx] = str(int(c[tary][tarx]) + 1)
                    d[breakblock + 1].append((tary + dy, tarx + dx))


print(ans)