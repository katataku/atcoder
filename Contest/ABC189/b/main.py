# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n, x = map(int, input().split())
# h, w = map(int, input().split())

x *= 100
drunk = 0
for i in range(n):
    v_in, p_in = map(int, input().split())
    alc = v_in * p_in
    x -= alc

    if x < 0:
        drunk = i + 1
        break


if x >= 0:
    print("{}".format(-1))
else:
    print("{}".format(drunk))

