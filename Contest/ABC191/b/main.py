# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n, x = map(int, input().split())
a = list(map(int, input().split()))
# h, w = map(int, input().split())

ans = list(filter(lambda z: z != x, a))


print(*ans)

