# -*- coding: utf-8 -*-
# Input#
import math

n = int(input())
s = []
for i in range(n):
    s.append(input())


def count(s):
    if len(s) == 0:
        return 1
    else:
        tar = s.pop()
        if tar == "OR":
            return (2 ** (len(s) + 1)) + (count(s))
        else:
            return count(s)


print("{}".format(count(s)))
