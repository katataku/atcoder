# -*- coding: utf-8 -*-
# Input#
import math
from functools import reduce


h, w = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# h, w = map(int, input().split())
# a_list = []
# b_list = []

a = []
for i in range(h):
    a_in = list(input().split())
    a.append(a_in)

memo1 = [[-1 for _ in range(w)] for _ in range(h)]
memo2 = [[-1 for _ in range(w)] for _ in range(h)]

memo1[h - 1][w - 1] = 0
memo2[h - 1][w - 1] = 0

player = 1
ans = "takahashi"


def cell(x, y):
    if a[x][0][y] == "+":
        return 1
    else:
        return -1


if (h + 2) % 2 == 0:
    player = 2

for i in range(h + w):
    for j in range(min(i, h + w - i)):
        x = j
        y = i - j

        if player == 1:
            if x + 1 == h:
                memo1[x][y] = max(memo1[x][y + 1]) + cell(x, y)
                memo2[x][y] = max(memo1[x][y + 1])
            elif y + 1 == w:
                memo1[x][y] = max(memo1[x + 1][y]) + cell(x, y)
                memo2[x][y] = max(memo1[x + 1][y])
            else:
                memo1[x][y] = max(memo1[x + 1][y], memo1[x][y + 1]) + cell(x, y)
                memo2[x][y] = max(memo1[x + 1][y], memo1[x][y + 1])

        if player == 2:
            memo2[x][y] = max(memo1[x + 1][y], memo1[x][y + 1]) + cell(x, y)
            memo1[x][y] = max(memo1[x + 1][y], memo1[x][y + 1])

print(ans)
