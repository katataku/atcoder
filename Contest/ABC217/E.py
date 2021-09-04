# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

q = int(input())

h = []
heapq.heapify(h)

queue = deque()

for i in range(q):
    s = input()
    if s[0] == "1":
        _, x = s.split()
        queue.append(int(x))
    elif s[0] == "2":
        if len(h) > 0:
            print(heapq.heappop(h))
        else:
            print(queue.popleft())
    else:
        while len(queue) > 0:
            heapq.heappush(h, queue.popleft())
