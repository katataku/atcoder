# -*- coding: utf-8 -*-

# Input#
n = list(input())
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
sum = 0
for i in n:
    sum += int(i)

if sum % 9 == 0:
    print("Yes")
else:
    print("No")


# print("{}".format(ans))
