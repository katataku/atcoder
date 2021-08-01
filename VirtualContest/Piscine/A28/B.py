n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = [{}, {}, {}]

for i in range(46):
    d[0][i] = 0
    d[1][i] = 0
    d[2][i] = 0

for i in range(n):
    d[0][a[i] % 46] += 1
    d[1][b[i] % 46] += 1
    d[2][c[i] % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += d[0][i] * d[1][j] * d[2][k]
print(ans)