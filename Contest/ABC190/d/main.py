# -*- coding: utf-8 -*-
# Input#
import math

n = int(input())
#s = []

ans = 0
for i in range(1,int(math.sqrt(n))+2):
    if i %2 == 0:
        if n%i == i//2:
            ans +=1
    else:
        if n % i == 0:
            ans +=1        


print("{}".format(ans*2))
