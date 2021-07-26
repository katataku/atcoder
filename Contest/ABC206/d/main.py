# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))

x = 0
y = 0
d = {}
ans = 0


def find(n):
    global d
    if d[n] == n:
        return n
    else:
        d[n] = find(d[n])
        return d[n]


for i in range(n // 2):
    if a[i] != a[-1 - i]:
        x = min(a[i], a[-1 - i])
        y = max(a[i], a[-1 - i])
        if x in d.keys() and y in d.keys():
            if find(x) < find(y):
                d[find(y)] = find(x)
            else:
                d[find(x)] = find(y)
        elif x in d.keys() and y not in d.keys():
            d[y] = find(x)
        elif y in d.keys() and x not in d.keys():
            d[x] = find(y)
        else:
            d[x] = x
            d[y] = x

d_cnt = {}
for key in d.keys():
    if find(key) in d_cnt.keys():
        d_cnt[find(key)] += 1
    else:
        d_cnt[find(key)] = 1
ans = 0
for key in d_cnt.keys():
    ans += d_cnt[key] - 1


print(ans)
