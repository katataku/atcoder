n, m = map(int, input().split())

x = list(map(int, input().split()))
x.sort()

dist = []
for i in range(m - 1):
    dist.append(x[i + 1] - x[i])

dist.sort()
ans = 0

if n < m:
    if n == 1:
        ans = sum(dist)
    else:
        ans = sum(dist[: -n + 1])

print(ans)