# -*- coding: utf-8 -*-
import math

# Input#
# n = list(input())
n = int(input())
# h, w = map(int, input().split())
x = list(map(int, input().split()))


man = 0
euc = 0
cheb = 0
for i in range(len(x)):
    tar = x[i]
    man += abs(tar)
    euc += abs(tar) * abs(tar)
    if cheb < abs(tar):
        cheb = abs(tar)

euc = math.sqrt(euc)
print("{}".format(man))
print("{}".format(euc))
print("{}".format(cheb))
