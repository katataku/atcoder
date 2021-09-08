n, k = map(int, input().split())
MAX = 5001
ab_list = []
for i in range(n):
    a, b = map(int, input().split())
    MAX = max(a, b, MAX)
    ab_list.append((a, b))

MAX += 1
mp = [[0 for i in range(MAX)] for j in range(MAX)]

for a, b in ab_list:
    mp[a][b] += 1


for i in range(MAX):
    for j in range(1, MAX):
        mp[i][j] += mp[i][j - 1]

for i in range(1, MAX):
    for j in range(MAX):
        mp[i][j] += mp[i - 1][j]

ans = 0
for i in range(1, MAX):
    ry = i + k
    if ry >= MAX:
        break
    for j in range(1, MAX):
        rx = j + k
        lx = j - 1
        ly = i - 1
        if rx >= MAX:
            break
        cur = mp[ry][rx] - mp[ly][rx] - mp[ry][lx] + mp[ly][lx]
        ans = max(ans, cur)
print(ans)
