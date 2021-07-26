# -*- coding: utf-8 -*-
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(1000000)


INF = float("inf")

d = deque()
# ---Input---#
# n = int(input())
h, w = map(int, input().split())

a = [["#" for _ in [INF] * (w + 1)] for _ in [INF] * ((h + 1))]
memo = [[0 for _ in [INF] * (w + 1)] for _ in [INF] * ((h + 1))]

for i in range(h + 1)[1:]:
    a[i] = list("#" + input())

memo[1][1] = 1
d = deque()
if a[2][1] == ".":
    d.append((2, 1))
if a[1][2] == ".":
    d.append((1, 2))


def dp(x, y):
    tmp = 0
    if a[x - 1][y] == ".":
        tmp = tmp + memo[x - 1][y]
    if a[x][y - 1] == ".":
        tmp = tmp + memo[x][y - 1]
    tmp = tmp % (10 ** 9 + 7)
    memo[x][y] = tmp
    return tmp


while len(d) > 0:
    x, y = d.popleft()
    if memo[x][y] == 0:
        dp(x, y)
        if x < h:
            if a[x + 1][y] == ".":
                d.append((x + 1, y))
        if y < w:
            if a[x][y + 1] == ".":
                d.append((x, y + 1))


ans = memo[h][w]

print("{}".format(ans))
