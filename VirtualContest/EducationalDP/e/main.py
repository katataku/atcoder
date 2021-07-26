# -*- coding: utf-8 -*-
INF = float("inf")
# Input#
# n = int(input())
n, tar_w = map(int, input().split())

w = [-1]
v = [-1]
value_max = 0
for i in range(n):
    w_in, v_in = list(map(int, input().split()))
    w.append(w_in)
    v.append(v_in)
    value_max += v_in


memo = [[-1] * (value_max + 1) for i in range(n + 1)]

for i in range(n + 1):
    memo[i][0] = v[i]

for i in range(value_max + 1):
    memo[0][i] = INF


def dp(i, value):
    if memo[i][value] == -1:
        if value > v[i]:
            rest = dp(i - 1, value - v[i])
            if rest == INF:
                tar = INF
            else:
                tar = rest + w[i]
            memo[i][value] = min(dp(i - 1, value), tar)
        else:
            memo[i][value] = min(dp(i - 1, value), w[i])
    return memo[i][value]


ans = -1
OK_MAX = 0
NG_MIN = value_max + 1

while OK_MAX + 1 != NG_MIN:
    i = int((OK_MAX + NG_MIN) / 2)
    ans_tmp = dp(n, i)
    if ans_tmp <= tar_w:
        OK_MAX = i
    else:
        NG_MIN = i

ans = OK_MAX

print("{}".format(ans))
