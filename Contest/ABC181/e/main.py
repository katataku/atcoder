# -*- coding: utf-8 -*-
# Input#
# n = int(input())
INF = float("inf")

n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))


h.sort()
w.sort()

minimum = 0


def calc(tar, x):
    global minimum
    global ans
    while minimum < len(tar):
        if tar[minimum] > x:
            break
        else:
            minimum += 1
    tar.insert(minimum, x)

    sum = 0
    for i in range(len(tar) // 2):
        sum += abs(tar[2 * i] - tar[(2 * i) + 1])
        if sum > ans:
            break
    return sum


ans = INF

for i in range(len(w)):
    tmp = calc(h.copy(), w[i])
    ans = min(ans, tmp)
    if w[i] > h[n - 1]:
        break


print("{}".format(ans))
