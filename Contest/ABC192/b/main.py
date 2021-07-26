# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

s = input()
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# h, w = map(int, input().split())

ans = "Yes"
tar = 0
while tar < len(s):
    l = s[tar]
    if (tar % 2 == 0 and l.islower()) or (tar % 2 == 1 and l.isupper()):
        tar += 1
    else:
        ans = "No"
        break


print(ans)

