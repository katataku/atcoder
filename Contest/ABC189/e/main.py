# -*- coding: utf-8 -*-
# Input#

N = int(input())
x = []
y = []
for i in range(N):
    x_in, y_in = map(int, input().split())
    x.append(x_in)
    y.append(y_in)

M = int(input())
op = []
for i in range(M):
    op_in = input()
    op.append(op_in)

memo = [[-1] * (N) for i in range(M + 1)]


def query(num, tar):
    if memo[num][tar] != -1:
        return memo[num][tar]
    if num == 0:
        memo[num][tar] = (x[tar], y[tar])
        return (x[tar], y[tar])
    else:
        tar_x, tar_y = query(num - 1, tar)
        i = num - 1
        if op[i] == "1":
            tar_x, tar_y = tar_y, tar_x * -1
        elif op[i] == "2":
            tar_x, tar_y = tar_y * -1, tar_x
        else:
            operand, p = map(int, op[i].split())
            if operand == 3:
                tar_x = 2 * p - tar_x
            else:
                tar_y = 2 * p - tar_y
        memo[num][tar] = (tar_x, tar_y)
        return (tar_x, tar_y)


Q = int(input())
for i in range(Q):
    query_num, query_tar = map(int, input().split())
    tar_x, tar_y = query(query_num, query_tar - 1)
    print("{} {}".format(tar_x, tar_y))

