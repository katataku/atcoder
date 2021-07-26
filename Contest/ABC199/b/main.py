# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())

n = int(input())
# n, x = map(int, input().split())
a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# h, w = map(int, input().split())
# a_list = []
# b_list = []
bucket = [[] for _ in range(200)]

bucket[a[0] % 200] = [1]

ans = "No"
ans1 = 0
ans2 = 0

for i in range(n)[1:]:
    tar = a[i] % 200
    i += 1
    bucket_tmp = bucket.copy()
    if bucket[tar] == []:
        bucket_tmp[tar] = [i]
    else:
        ans = "Yes"
        ans1 = bucket[(tar) % 200]
        ans2 = [i]
    if ans == "yes":
        break

    for j in range(200):
        if bucket[j] == []:
            continue
        else:
            if bucket[(j + tar) % 200] != []:
                ans = "Yes"
                anstar = tar
                ans1 = bucket[(j + tar) % 200]
                ans2 = bucket[j] + [i]
            bucket_tmp[(tar + j) % 200] = bucket[j] + [i]
    bucket = bucket_tmp.copy()
    if ans == "yes":
        break


print(ans)
if ans == "Yes":
    ans1.insert(0, len(ans1))
    ans2.insert(0, len(ans2))
    print(" ".join(map(str, ans1)))
    print(" ".join(map(str, ans2)))
