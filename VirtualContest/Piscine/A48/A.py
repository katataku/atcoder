# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
h, w = map(int, input().split())

mp = []
mp.append(["#" for i in range(w + 2)])
for i in range(h):
    a = list(input())
    a.append("#")
    a.insert(0, "#")
    mp.append(a)
mp.append(["#" for i in range(w + 2)])


next_dest = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solve(start_y, start_x, cur_y, cur_x, acc):
    ret = -1
    mp[cur_y][cur_x] = "#"
    for dy, dx in next_dest:
        if cur_y + dy == start_y and cur_x + dx == start_x:
            ret = acc + 1
        else:
            if mp[cur_y + dy][cur_x + dx] == ".":
                ret = max(ret, solve(start_y, start_x, cur_y + dy, cur_x + dx, acc + 1))
    mp[cur_y][cur_x] = "."
    return ret


ans = -1
for y in range(h + 2):
    for x in range(w + 2):
        if mp[y][x] == ".":
            ans = max(ans, solve(y, x, y, x, 0))
if ans < 3:
    ans = -1

print(ans)
