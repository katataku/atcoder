import math

n, start = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

ans = abs(start - x[0])


for i in range(1, len(x)):
    ans = math.gcd(ans, abs(x[i] - x[i - 1]))

print(ans)
