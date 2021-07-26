# -*- coding: utf-8 -*-
import math

# Input#
s = input()
ans = ""
if s[0] == s[1] and s[1] == s[2]:
    ans = "Won"
else:
    ans = "Lost"

print(ans)

