# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

n = int(input())

n = int(n * 1.08)

ans = "so-so"

if n < 206:
    ans = "Yay!"
if n > 206:
    ans = ":("


print(ans)