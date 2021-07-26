# -*- coding: utf-8 -*-
from functools import reduce
import math

# Input#
n = int(input())
# n, k = map(int, input().split())
# memo = [-1 for i in range(10 ** len(n) + 1)]

cnt = 0
a = 2
b = int(math.log(n, a)) + 2

base_list = list(range(int(math.sqrt(n)) + 1, 1, -1))

while 0 < len(base_list):
    a = base_list.pop()
    if a ** 2 > n:
        break
    while b > 1:
        if a ** b <= n:
            cnt += b - 1
            break
        else:
            b -= 1
    for i in range(2, b + 1):
        if a ** i in base_list:
            base_list.remove(a ** i)

print("{}".format(n - cnt))
