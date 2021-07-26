# -*- coding: utf-8 -*-
import math

# Input#
# n = list(input())
# n = int(input())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
d = []

for i in range(m):
    c_in, d_in = map(int, input().split())
    c.append(c_in)
    d.append(d_in)

tar_minus = 0
tar_plus = 0

memo = [[-1] * (n) for i in range(n)]


def is_con(src, dst):
    if memo[src,dst]==1:
        return True
    elif memo[src,dst]==0:
        return False
    else:
        for i in range(m):
            if src
            if (c[i] == src and d[i] == dst) or (c[i] == dst and d[i] == dst):
                return True
        return False


ans = "No"

if sum(a) == sum(b):
    ans = "undef"
    while ans == "undef":
        ans = "Yes"
        for i in range(n):
            if a[i] <= b[i]:
                continue
            else:
                tar_minus = i
                ans = "undef"
                break

        if ans == "Yes":
            break
        else:
            ans = "No"
            for i in range(m):
                if a[i] > b[i]:
                    tar_plus = i
                    if is_con(tar_minus, tar_plus):
                        a[tar_minus] += 1
                        a[tar_plus] -= 1
                        ans = "undef"
                        break


print("{}".format(ans))
