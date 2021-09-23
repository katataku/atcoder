n, k = map(int, input().split())

a = list(map(int, input().split()))

ans = sum(a[0:k])
for i in range(n - k + 1):
    print(ans)
    if i + k < n:
        ans -= a[i]
        ans += a[i + k]
