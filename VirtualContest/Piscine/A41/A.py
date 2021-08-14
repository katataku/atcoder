n = int(input())

m = [[0 for i in range(1002)] for j in range(1002)]
cnt = {}
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    m[ly][lx] += 1
    m[ly][rx] -= 1
    m[ry][lx] -= 1
    m[ry][rx] += 1

ans = {}

for i in range(1001):
    for j in range(1, 1001):
        m[i][j] += m[i][j - 1]

for i in range(1001):
    for j in range(1001):
        if i > 0:
            m[i][j] += m[i - 1][j]
        if m[i][j] not in ans:
            ans[m[i][j]] = 0
        ans[m[i][j]] += 1

for i in range(n):
    print(ans.get(i + 1, 0))
