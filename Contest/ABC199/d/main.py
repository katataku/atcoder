# -*- coding: utf-8 -*-
# Input#
import math
from functools import reduce


s1 = input()
s2 = input()
s3 = input()

used_list = []

# for i in range(len(s1)):
#    used_list[ord(s1[i]) - 97] = 1

for i in range(len(s1)):
    if not s1[i] in used_list:
        used_list.append(s1[i])

for i in range(len(s2)):
    if not s2[i] in used_list:
        used_list.append(s2[i])

for i in range(len(s3)):
    if not s3[i] in used_list:
        used_list.append(s3[i])


ans_list = [[-1 for i in range(10)] for j in range(len(used_list))]

flag = 0

fixed_ans_list = []


def assign_check(s1, s2, s3, used_list, ans_list):
    for i in range(len(used_list)):
        tar_c = used_list[i]
        tar_n = str(ans_list[i].index(1))
        s1 = s1.replace(tar_c, tar_n)
        s2 = s2.replace(tar_c, tar_n)
        s3 = s3.replace(tar_c, tar_n)
    return int(s1) + int(s2) == s3


def check_unique(tar_num, used_list, ans_list):
    for i in range(len(used_list)):
        if ans_list[i][tar_num] == 1:
            return False
    return True


def assign(s1, s2, s3, used_list, ans_list):
    global fixed_ans_list
    for i in range(len(ans_list)):
        if not 1 in ans_list[i]:
            assume_num = ans_list[i].index(-1)
            if check_unique(assume_num, used_list, ans_list):
                ans_list[i][assume_num] = 1
                if assign(s1, s2, s3, used_list, ans_list):
                    fixed_ans_list = ans_list
                    return True
                else:
                    ans_list[i][assume_num] = -2
                    return False

    return assign_check(s1, s2, s3, used_list, ans_list)


print(used_list)
print(ans_list)
print(assign(s1, s2, s3, used_list, ans_list))
print(fixed_ans_list)
