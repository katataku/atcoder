n, k = map(int, input().split())

p = list(map(int, input().split()))
ans = sum(map(lambda x: (x + 1) / 2, p[:k]))

tmp = ans
for i in range(k, n):
    tmp += (p[i] + 1) / 2
    tmp -= (p[i - k] + 1) / 2
    ans = max(ans, tmp)
print(ans)
