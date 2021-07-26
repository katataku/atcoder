n, m = map(int, input().split())

INF = 10 ** 10
memo_now = [[INF for j in range(n)] for k in range(n)]
ans = 0

for i in range(m):
    a, b, c = map(int, input().split())
    memo_now[a - 1][b - 1] = c

for i in range(1, n + 1):
    memo_next = [[INF for j in range(n)] for k in range(n)]
    for j in range(n):
        for k in range(n):
            if k == j:
                memo_next[k][j] = 0
                continue
            memo_next[k][j] = min(
                memo_now[k][j], memo_now[k][i - 1] + memo_now[i - 1][j]
            )
            if memo_next[k][j] != INF:
                ans += memo_next[k][j]
    memo_now = memo_next


print(ans)
