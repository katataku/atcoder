n = int(input())

ans = 1
cur = n
d = {}
while cur not in d:
    d[cur] = True
    ans += 1
    if cur % 2 == 0:
        cur = cur // 2
    else:
        cur = 3 * cur + 1
print(ans)
