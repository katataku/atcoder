# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

n = int(input())

ans = (1000 - (n % 1000)) % 1000

print(ans)