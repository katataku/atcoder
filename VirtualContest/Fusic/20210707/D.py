# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(1000000)

h, w = map(int, input().split())

s = []

s.append(["#" for i in range(w + 2)])

start_pos = (-1, -1)
for i in range(h):
    s.append(list(input()))
    s[i + 1].insert(0, "#")
    s[i + 1] += "#"
s.append(["#" for i in range(w + 2)])


directions = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
memo = {0: {}, 1: {}, 2: {}, 3: {}}


# memo = [[[-1 for _ in range(w + 2)] for _ in range(h + 2)] for _ in range(4)]


def search_count(x, y, direction):
    if y not in memo[direction].keys():
        memo[direction][y] = {}

    if x in memo[direction][y].keys():
        return memo[direction][y][x]

    if s[y][x] == "#":
        memo[direction][y][x] = 0
    else:
        dx, dy = directions[direction]
        memo[direction][y][x] = 1 + search_count(x + dx, y + dy, direction)
    return memo[direction][y][x]


for i in range(4):
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if s[y][x] == ".":
                search_count(x, y, i)

ans = 0

for y in range(1, h + 1):
    for x in range(1, w + 1):
        if s[y][x] == ".":
            count = 0
            for i in range(4):
                count += search_count(x, y, i)
            count -= 3
            ans = max(ans, count)


print(ans)
