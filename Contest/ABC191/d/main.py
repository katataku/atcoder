# -*- coding: utf-8 -*-
# Input#
import math

x, y, r = map(float, input().split())
# s = []

base_x = math.ceil(x - r)
base_y = math.ceil(y - r)
ans = 0
for i in range(math.ceil(r * 2) + 1):
    flag = False
    d_x = abs(x - (base_x + i))
    if d_x > r:
        continue
    d_y = math.sqrt((r ** 2) - (d_x ** 2))
    ans += int(d_y * 2)
    if y == int(y):
        ans += 1
    # for j in range(math.floor(y - base_y - d_y), math.ceil(r * 2) + 1):
    #     tar_x = base_x + i
    #     tar_y = base_y + j
    #     if (tar_x - x) ** 2 + (tar_y - y) ** 2 <= r ** 2:
    #         flag = True
    #         ans += 1
    #     else:
    #         if flag:
    #             break

print("{}".format(ans))

