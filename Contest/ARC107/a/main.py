# -*- coding: utf-8 -*-
import math

# Input#
a, b, c = map(int, input().split())
# a = list(map(int, input().split()))
ans = 0
sum_a1 = int(a * (a + 1) / 2) % 998244353
sum_a2 = int(a * (a + 1) // 2) % 998244353

sum_a1 = a * (a + 1) / 2
sum_a2 = a * (a + 1) // 2


sum_b1 = b * (b + 1) / 2
sum_b2 = b * (b + 1) // 2


sum_b1 = int(b * (b + 1) / 2) % 998244353
sum_b2 = int(b * (b + 1) // 2) % 998244353
sum_c1 = int(c * (c + 1) / 2) % 998244353
sum_c2 = int(c * (c + 1) // 2) % 998244353
ans = sum_a * sum_b * sum_c

print("{}".format(ans % 998244353))

