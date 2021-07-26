a, b, c, k = map(int, input().split())

ans = 0
if a > k:
    ans += k
else:
    ans += a
    k -= a
    k -= b
    if k > 0:
        ans -= k

print(ans)
