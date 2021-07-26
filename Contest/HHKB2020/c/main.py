# -*- coding: utf-8 -*-

# Input#
n = int(input())
# n, k = map(int, input().split())
p = list(map(int, input().split()))


min = 0
tar_low = []
tar_high = []

for i in range(n):
    if p[i] > min:
        tar_high.append(p[i])

    if p[i] == min:
        min += 1
        tmp_tar_high = []
        tar_high.sort()
        for j in range(len(tar_high)):
            if tar_high[j] == min:
                min += 1

            if tar_high[j] > min:
                tmp_tar_high.append(tar_high[j])
        tar_high = tmp_tar_high
    print("{}".format(min))
