# -*- coding: utf-8 -*-
import math

# Input#
n = int(input())
# a = list(map(int, input().split()))

a = 1
b = 1

while 5 ** b < n:
    tar = n - (5 ** b)

    a = 1
    while (3 ** a) <= tar:
        if (3 ** a) == tar:
            print("{} {}".format(a, b))
            exit(0)
        a += 1
    b += 1


print("{}".format(-1))
