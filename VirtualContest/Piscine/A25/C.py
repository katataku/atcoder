import math

a, b, c = map(int, input().split())

l = math.gcd(math.gcd(a, b), c)

ans = 0
ans += (a // l) - 1
ans += (b // l) - 1
ans += (c // l) - 1
print(ans)