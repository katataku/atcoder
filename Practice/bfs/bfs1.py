# -*- coding: utf-8 -*-
import math
import heapq
from collections import deque
import itertools

r, c = map(int, input().split())

sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

c = []
c.append(["#"])

for i in range(r):
    s = input()
    s = list("#" + s)
    c.append(s)


d = deque()
d.append((sy, sx))
ans = 0
c[sy][sx] = "0"

while True:
    tary, tarx = d.popleft()
    if tary == gy and tarx == gx:
        print(c[gy][gx])
        break
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if c[tary + dy][tarx + dx] == ".":
            c[tary + dy][tarx + dx] = str(int(c[tary][tarx]) + 1)
            d.append((tary + dy, tarx + dx))
