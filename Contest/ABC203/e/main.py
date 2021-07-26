# -*- coding: utf-8 -*-
# Input#
import math
import heapq
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())
p = list(map(int, input().split()))

stepd = {1: 0}
listd = {1: []}
parentd = {1: 0}
maxdepth = 0

for i in range(n - 1):
    par = p[i]
    parentd[i + 2] = par

unchecklist = list(range(n, 1, -1))
while len(unchecklist) > 0:
    tar = unchecklist.pop()
    par = parentd[tar]
    if par in stepd.keys():
        stepd[tar] = stepd[par] + 1
        maxdepth = max(maxdepth, stepd[tar])
        listd[tar] = []
        listd[par].append(tar)
    else:
        unchecklist.insert(0, tar)


def findnode(cur, d):
    ans = 0
    if d == 0:
        ans = 1
    else:
        if cur in listd.keys() and d < maxdepth:
            for nextnode in listd[cur]:
                ans += findnode(nextnode, d - 1)
    return ans


q = int(input())
for i in range(q):
    u, d = map(int, input().split())
    ans = 0
    if not stepd[u] > d:
        ans = findnode(u, d - stepd[u])

    print(ans)
