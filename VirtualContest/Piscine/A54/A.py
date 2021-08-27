a, b, c = map(int, input().split())


ans = b
if b < c:
    ans += b
    c -= b
else:
    ans += c
    c = 0

if c > 0:
    ans += min(c, a + 1)
print(ans)
