# -*- coding: utf-8 -*-

# Input#
# N = int(input())
h, w = map(int, input().split())
a = []
first_h = -1
first_w = -1
for i in range(h):
    a_in = input()
    a.append(a_in)
    if "#" in a_in and first_h == -1:
        first_h = i
        first_w = a_in.index("#")

d = 0

d_h = [0, 1, 0, -1]
d_w = [1, 0, -1, 0]

tar_h = first_h
tar_w = first_w
ans = 1
while d != 3 or not (tar_h == first_h and tar_w == first_w):
    next_h = tar_h + d_h[(d - 1) % 4]
    next_w = tar_w + d_w[(d - 1) % 4]
    if a[next_h][next_w] == "#":
        ans += 1
        d = (d - 1) % 4
        tar_h = next_h
        tar_w = next_w
        continue

    next_h = tar_h + d_h[d]
    next_w = tar_w + d_w[d]

    if a[next_h][next_w] == "#":
        tar_h = next_h
        tar_w = next_w
        continue
    else:
        ans += 1
        d = (d + 1) % 4
        continue


print("{}".format(ans))
