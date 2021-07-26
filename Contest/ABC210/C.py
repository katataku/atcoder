n, k = map(int, input().split())

c = list(map(int, input().split()))

d = {}
ans = 0
for i in range(k):
    tar = c[i]
    if tar in d.keys():
        d[tar] += 1
    else:
        d[tar] = 1
        ans += 1
tmp = ans
for i in range(k, n):
    if d[c[i - k]] == 1:
        d.pop(c[i - k])
        tmp -= 1
    else:
        d[c[i - k]] -= 1

    if c[i] in d.keys():
        d[c[i]] += 1
    else:
        d[c[i]] = 1
        tmp += 1
    ans = max(tmp, ans)
print(ans)