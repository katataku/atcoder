# -*- coding: utf-8 -*-
from functools import reduce
import math

# Input#
s = input()

c_o = s.count("o")
c_x = s.count("x")
c_q = s.count("?")

ans = 0







if c_o > 4:
    ans = 0
elif c_o==4:
    ans = 1
elif c_o ==3:
    ans = 72+(48*c_q)
else c_o ==2:
    for i in range(3):
        ans += (4-2+1)*(c_q**i) * 

    ans =14 + (23*c_q)+(2*c_q*c_q*36)
else c_o == 1:
    ans = 1+4*c_q+()

print("{}".format(s))
