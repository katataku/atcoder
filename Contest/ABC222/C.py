# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, m = map(int, input().split())
a = []
for i in range(2 * n):
    a_in = input()
    a.append(a_in)


def is_win(a, b):
    if a == "G" and b == "C":
        return True
    if a == "C" and b == "P":
        return True
    if a == "P" and b == "G":
        return True
    return False


def set_num(cnt, node):
    return (cnt * 1000 * (-1)) + node


def get_num(num):
    node = num % 1000
    num *= -1
    num += node
    cnt = num // 1000
    return (cnt, node)


h = [set_num(0, i) for i in range(2 * n)]
heapq.heapify(h)

next_h = []
heapq.heapify(next_h)


for i in range(m):
    while len(h) > 0:
        tar_1 = heapq.heappop(h)
        tar_2 = heapq.heappop(h)
        tar1_cnt, tar_1 = get_num(tar_1)
        tar2_cnt, tar_2 = get_num(tar_2)
        if is_win(a[tar_1][i], a[tar_2][i]):
            tar1_cnt += 1
        if is_win(a[tar_2][i], a[tar_1][i]):
            tar2_cnt += 1

        heapq.heappush(next_h, set_num(tar1_cnt, tar_1))
        heapq.heappush(next_h, set_num(tar2_cnt, tar_2))
    h, next_h = next_h, h

for i in range(2 * n):
    tar_1 = heapq.heappop(h)
    cnt, node = get_num(tar_1)
    print(node + 1)
