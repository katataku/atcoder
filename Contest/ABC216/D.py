# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(1000000)
n, m = map(int, input().split())

path = {}

for i in range(m):
    k = int(input())
    a = list(map(int, input().split()))
    a[0] -= 1
    for i in range(1, k):
        a[i] -= 1
        path[a[i]] = path.get(a[i], [])
        path[a[i]].append(a[i - 1])


def dfs(v, start):
    ret = False
    for next in path.get(v, []):
        if next not in visited:
            visited[next] = True
            if next == start:
                return True
            else:
                if dfs(next, start):
                    ret = True
    return ret


visited = {}


ans = "Yes"
for i in range(n):
    if dfs(i, i):
        ans = "No"
print(ans)