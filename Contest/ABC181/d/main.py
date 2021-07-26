# -*- coding: utf-8 -*-
import itertools

f_inf = float("inf")

# Input#
s = input()
hist = [0] * 10

new_s = ""


def check(s):
    if len(s) >= 3:
        for a, b, c in itertools.permutations(s[-3:], r=3):
            if int(a + b + c) % 8 == 0:
                return True
        return False
    elif len(s) == 2:
        return int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0
    else:
        return int(s) % 8 == 0


for i in range(len(s)):
    tar = int(s[i])
    if hist[tar] < 3:
        hist[tar] += 1
        new_s += s[i]

s = new_s
if len(s) > 3:
    for a, b, c in itertools.permutations(s, r=3):
        if check(a + b + c):
            print("{}".format("Yes"))
            exit(0)
else:
    if check(s):
        print("{}".format("Yes"))
        exit(0)

print("{}".format("No"))
