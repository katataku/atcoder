# -*- coding: utf-8 -*-
import math
import heapq
from collections import deque
import itertools

h, w = map(int, input().split())

sy, sx = (0, 0)
gy, gx = (0, 0)

c = []

for i in range(h):
    s = list(input())
    if "s" in s:
        sy, sx = (i, s.index("s"))
    if "g" in s:
        gy, gx = (i, s.index("g"))
        s[gx] = "."
    c.append(s)


d = deque()
d.append((sy, sx))
ans = "No"
c[sy][sx] = "0"

while len(d) > 0:
    tary, tarx = d.popleft()
    if tary == gy and tarx == gx:
        ans = "Yes"
        break
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (
            tary + dy >= 0
            and tary + dy <= h - 1
            and tarx + dx >= 0
            and tarx + dx <= w - 1
        ):
            if c[tary + dy][tarx + dx] == ".":
                c[tary + dy][tarx + dx] = str(int(c[tary][tarx]) + 1)
                d.appendleft((tary + dy, tarx + dx))

print(ans)