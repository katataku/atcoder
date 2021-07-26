# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n, m, t = map(int, input().split())
# h, w = map(int, input().split())
p = n
ans = "Yes"
time = 0
for i in range(m):
    a_in, b_in = map(int, input().split())
    walk_time = a_in - time
    if p <= (walk_time):
        ans = "No"
        break
    cafe_time = b_in - a_in
    p = min(p - walk_time + cafe_time, n)
    time += walk_time + cafe_time

walk_time = t - time
if p <= (walk_time):
    ans = "No"

print("{}".format(ans))
