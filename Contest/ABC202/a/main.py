# -*- coding: utf-8 -*-
import math
import heapq
from collections import deque
import itertools

s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "6":
        ans += "9"
    elif s[i] == "9":
        ans += "6"
    else:
        ans += s[i]


print(ans[::-1])
