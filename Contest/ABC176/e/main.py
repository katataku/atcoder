# -*- coding: utf-8 -*-
# Input#
# n = int(input())
h, w, m = map(int, input().split())
tar_list = []

h_count = [0] * (h + 1)
w_count = [0] * (w + 1)

h_max = 0
w_max = 0

h_maxlist = []
w_maxlist = []

ans = 0
ans_tmp = 0

for i in range(m):
    h_in, w_in = map(int, input().split())

    h_count[h_in] += 1
    if h_count[h_in] > h_max:
        h_max = h_count[h_in]
        h_maxlist = []
    if h_count[h_in] == h_max:
        h_maxlist.append(h_in)
        tar_list.append((h_in, w_in))

    w_count[w_in] += 1
    if w_count[w_in] > w_max:
        w_max = w_count[w_in]
        w_maxlist = []
    if w_count[w_in] == w_max:
        w_maxlist.append(w_in)
        tar_list.append((h_in, w_in))


ans = h_max + w_max - 1
cnt = 0
for (tar_h, tar_w) in tar_list:
    if tar_h in h_maxlist:
        if tar_w in w_maxlist:
            cnt += 1

if cnt != len(h_maxlist) * len(w_maxlist):
    ans += 1


print("{}".format(ans))
