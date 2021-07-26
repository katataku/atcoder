# -*- coding: utf-8 -*-
# Input#
import math

# n = int(input())
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = []
a.sort()
INF = 100000000000
min_length = INF

for i in range(M):
    length = 0
    if a[i] == 1:
        continue
    if i == 0:
        length = a[i] - 1
    else:
        length = a[i] - a[i - 1] - 1
    if length > 0:
        min_length = min(min_length, length)
        b.append(length)

if M == 0:
    ans = 1
else:
    ans = 0
    if N != a[M - 1]:
        length = N - a[M - 1]
        min_length = min(min_length, length)
        b.append(length)
    for i in range(len(b)):
        ans += math.ceil(b[i] / min_length)


print("{}".format(ans))
