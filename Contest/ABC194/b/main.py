# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n = int(input())
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# h, w = map(int, input().split())
a_list = []
b_list = []

for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

s_a_list = sorted(a_list)
s_b_list = sorted(b_list)

min_a = s_a_list[0]
min_b = s_b_list[0]

if a_list.index(min_a) == b_list.index(min_b):
    ans = min(
        min_a + min_b, max(s_a_list[1], s_b_list[0]), max(s_a_list[0], s_b_list[1])
    )

else:
    ans = max(min_a, min_b)


print(ans)
