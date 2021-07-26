n, m = map(int, input().split())

ans = 0

if n == 1 and m == 1:
    ans += 400000

if n < 4:
    ans += (4 - n) * 100000
if m < 4:
    ans += (4 - m) * 100000

print(ans)