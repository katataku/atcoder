# -*- coding: utf-8 -*-
import math

# Input#
n = int(input())
# n, k = map(int, input().split())
# p = list(map(int, input().split()))


ans_list = []


for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print("{}".format(i))
        if int(n / i) != i:
            ans_list.insert(0, int(n / i))


for i in range(len(ans_list)):
    print("{}".format(ans_list[i]))

