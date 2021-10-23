# -*- coding: utf-8 -*-
import math
import heapq
from collections import deque
import itertools
import copy

h, w = (10, 10)


c = []
c.append([""])
cnt_white = 0

for i in range(h):
    s = list("x" + input())
    cnt_white += s.count("o")
    c.append(s)
c_org = copy.deepcopy(c)

ans = "NO"

for i in range(h):
    for j in range(w):
        c = copy.deepcopy(c_org)
        tar_cnt = 0
        if c[i + 1][j + 1] == "o":
            tar_cnt += 1
            c[i + 1][j + 1] = "x"
        d = deque()
        d.append((i + 1, j + 1, 0))
        while len(d) > 0:
            tary, tarx, tar_step = d.popleft()
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (
                    tary + dy >= 1
                    and tary + dy <= h
                    and tarx + dx >= 1
                    and tarx + dx <= w
                ):
                    if c[tary + dy][tarx + dx] == "o":
                        c[tary + dy][tarx + dx] = "x"
                        d.appendleft((tary + dy, tarx + dx, tar_step))
                        tar_cnt += 1
            if tar_cnt == cnt_white:
                ans = "YES"
                break


print(ans)