# -*- coding: utf-8 -*-
import math

# Input#
r_1, c_1 = map(int, input().split())
r_2, c_2 = map(int, input().split())


# a = list(map(int, input().split()))


def calc_crosspoint(a, b, c, d):
    b1 = a - b
    b2 = c - d

    y = ()
    return (x, y)


def check(a, b, c, d):
    if a + b == c + d:
        return True
    if a - b == c - d:
        return True
    if abs(a - c) + abs(b - d) <= 3:
        return True
    return False


ans = 0
if not (r_1 == r_2 and c_1 == c_2):
    for i in range(3):
        if check(r_1, c_1, r_2, c_2):
            ans = i + 1
            break
        else:
            break


print("{}".format(ans))
