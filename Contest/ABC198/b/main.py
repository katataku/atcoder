# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n = input()
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# h, w = map(int, input().split())
# a_list = []
# b_list = []


while int(n) % 10 == 0 and int(n) > 0:
    n = n[0:-1]


ans = "Yes"
while len(n) > 0:
    if len(n) == 1:
        break
    if n[0] != n[-1]:
        ans = "No"
        break
    n = n[1:-1]


print(ans)
