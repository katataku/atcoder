# -*- coding: utf-8 -*-

# Input#
# n = list(input())
# n, s = input().split()
h, w = map(int, input().split())
# a = list(map(int, input().split()))

s = [" "] * (h + 2)

for i in range(h):
    s[i] = input()

ans = 0


for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            if i < h - 1:
                if s[i + 1][j] == ".":
                    ans += 1
            if j < w - 1:
                if s[i][j + 1] == ".":
                    ans += 1


print("{}".format(ans))
