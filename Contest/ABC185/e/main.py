# -*- coding: utf-8 -*-
# Input#
import math

# n = int(input())
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
INF = 100000000000
ans = 0


def check(a, b):
    ans = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1
    return ans


def diffcheck(a, b):
    ans = INF
    diff = len(a) - len(b)
    if diff == 1:
        for i in range(len(a)):
            ans = min(check(a[0:i] + a[i + 1 :], b), ans)
    else:
        for i in range(len(a)):
            ans = min(diffcheck(a[0:i] + a[i + 1 :], b), ans)
    return ans + 1


if len(a) == len(b):
    ans = check(a, b)
else:
    if len(a) < len(b):
        tmp = a
        a = b
        b = tmp
    ans = diffcheck(a, b)

print("{}".format(ans))
