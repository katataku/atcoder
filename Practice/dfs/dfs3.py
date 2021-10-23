import math
import heapq
import sys
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n, m = map(int, input().split())

d_path = {}
d_unvisited = []
for i in range(n):
    d_path[i + 1] = []
    d_unvisited.append(i + 1)


for i in range(m):
    u, v = map(int, input().split())
    d_path[u].append(v)
    d_path[v].append(u)


ans = 0
while len(d_unvisited) > 0:
    tar_node = d_unvisited[0]
    d = deque()
    d.append((tar_node, -1))
    flag = True
    cur_tree_list = []
    while len(d) > 0:
        tar_node, prev_node = d.pop()
        cur_tree_list.append(tar_node)
        if tar_node in d_unvisited:
            d_unvisited.remove(tar_node)
        if tar_node in d_path.keys():
            next_nodes = d_path[tar_node]
            for next_node in next_nodes:
                if prev_node == next_node:
                    continue
                else:
                    if next_node in cur_tree_list:
                        flag = False
                        break
                    else:
                        d.append((next_node, tar_node))
    if flag:
        ans += 1


print(ans)
