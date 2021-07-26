# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n = int(input())
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# h, w = map(int, input().split())
# a_list = []
# b_list = []

name1 = ""
name2 = ""
tall1 = -1
tall2 = -1

for i in range(n):
    s, t = input().split()
    t = int(t)
    if tall2 < t:
        if tall1 < t:
            tall2 = tall1
            name2 = name1
            tall1 = t
            name1 = s
        else:
            tall2 = t
            name2 = s


print(name2)
