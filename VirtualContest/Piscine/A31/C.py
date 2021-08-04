n, m = map(int, input().split())

d = {}
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    if b in d.keys():
        d[b].append(a)
    else:
        d[b] = [a]
ans = 0
for key, value in d.items():
    if len(value) == 1 and value[0] < key:
        ans += 1

print(ans)