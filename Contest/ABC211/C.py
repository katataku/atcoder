# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

s = input()
chokudai = "chokudai"

ans = 0


def solve(s, index):
    if index == 8:
        return 1
    if len(s) == 0:
        return 0
    ret = 0
    if chokudai[index] in s:
        if s[0] == chokudai[index]:
            ret += solve(s[1:], index + 1)
        ret += solve(s[s.find(chokudai[index]) :], index)
    return ret


ans = solve(s, 0)

print(ans % MOD)