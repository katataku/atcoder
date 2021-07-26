# -*- coding: utf-8 -*-

f_inf = float("inf")

# Input#
T = int(input())

for case in range(T):
    ans = 0
    n, a, b = map(int, input().split())

    if a < b:
        tmp = a
        a = b
        b = tmp

    a_pattern = (n - a + 1) ** 2
    b_pattern = (n - b + 1) ** 2

    # base pattern
    base_pattern = a_pattern * b_pattern

    # inside pattern
    if a == b:
        inside_pattern = 1
    else:
        inside_pattern = (a - b + 1) ** 2

    inside_pattern *= a_pattern

    # complex pattern
    complex_pattern = 0
    if b > 1:
        complex_pattern = (a + b - 1) ** 2

    ans = base_pattern - inside_pattern - complex_pattern

    print("{}".format(ans % 1000000007))
