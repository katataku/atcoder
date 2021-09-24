# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10


d = deque()

n = int(input())
s = input()

for i in range(n):
    if s[i] == "L":
        d.appendleft(i + 1)
    if s[i] == "R":
        d.append(i + 1)
    if s[i] == "A":
        if len(d) < 1:
            print("ERROR")
        else:
            print(d.popleft())
    if s[i] == "D":
        if len(d) < 1:
            print("ERROR")
        else:
            print(d.pop())
    if s[i] == "B":
        if len(d) < 2:
            print("ERROR")
        else:
            tmp = d.popleft()
            print(d.popleft())
            d.appendleft(tmp)
    if s[i] == "E":
        if len(d) < 2:
            print("ERROR")
        else:
            tmp = d.pop()
            print(d.pop())
            d.append(tmp)
    if s[i] == "C":
        if len(d) < 3:
            print("ERROR")
        else:
            tmp1 = d.popleft()
            tmp2 = d.popleft()
            print(d.popleft())
            d.appendleft(tmp2)
            d.appendleft(tmp1)
    if s[i] == "F":
        if len(d) < 3:
            print("ERROR")
        else:
            tmp1 = d.pop()
            tmp2 = d.pop()
            print(d.pop())
            d.append(tmp2)
            d.append(tmp1)