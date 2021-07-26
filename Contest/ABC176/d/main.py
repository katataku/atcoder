# -*- coding: utf-8 -*-
from collections import deque
import sys

f_inf = float("inf")

# Input#
# n = int(input())
h, w = map(int, input().split())
c_h, c_w = map(int, input().split())
d_h, d_w = map(int, input().split())

grid = []

d = deque()


for i in range(h + 1):
    if i == 0:
        array_tmp = "#" * w
    else:
        array_tmp = str(input().strip())
    array_tmp = "#" + array_tmp
    grid.append(list(array_tmp))


grid[c_h][c_w] = 0

d.append((c_h, c_w))


def check(tar_h, tar_w):
    if tar_h > h or tar_h < 1:
        return -1
    if tar_w > w or tar_w < 1:
        return -1
    if grid[tar_h][tar_w] == ".":
        return f_inf
    if grid[tar_h][tar_w] == "#":
        return -1
    else:
        return grid[tar_h][tar_w]


while len(d) != 0:
    tar_h, tar_w = d.popleft()
    tar_num = grid[tar_h][tar_w]
    if tar_num == "#":
        continue

    for i in range(5):
        for j in range(5):
            checknum = check(tar_h + i - 2, tar_w + j - 2)
            if checknum > tar_num:
                if (
                    (i == 2 and j == 1)
                    or (i == 2 and j == 3)
                    or (i == 1 and j == 2)
                    or (i == 3 and j == 2)
                ):
                    grid[tar_h + i - 2][tar_w + j - 2] = tar_num
                    d.appendleft((tar_h + i - 2, tar_w + j - 2))
                    if tar_h == d_h and tar_w == d_w:
                        print("{}".format(tar_num))
                        sys.exit()
                else:
                    if checknum > tar_num + 1:
                        grid[tar_h + i - 2][tar_w + j - 2] = tar_num + 1
                        d.append((tar_h + i - 2, tar_w + j - 2))

if check(d_h, d_w) == f_inf:
    ans = -1
else:
    ans = check(d_h, d_w)

print("{}".format(ans))
