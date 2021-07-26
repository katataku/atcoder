# -*- coding: utf-8 -*-

# Input#
n = int(input())
# n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
max = 0
for i in range(n):
    if i == 0:
        max = a[i]
        continue

    if a[i] < max:
        ans += max - a[i]
    else:
        max = a[i]


print("{}".format(ans))
