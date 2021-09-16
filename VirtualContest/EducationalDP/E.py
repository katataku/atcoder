n, w = map(int, input().split())

w_list = [0]
v_list = [0]
for i in range(n):
    w_in, v_in = map(int, input().split())
    w_list.append(w_in)
    v_list.append(v_in)

INF = 10 ** 10
ValueMAX = 10 ** 5 + 1
dp = [[INF for j in range(ValueMAX)] for i in range(n + 1)]

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(ValueMAX):
        if j - v_list[i] >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v_list[i]] + w_list[i])
        else:
            dp[i][j] = dp[i - 1][j]

ans = ValueMAX - 1
while dp[n][ans] > w:
    ans -= 1
print(ans)