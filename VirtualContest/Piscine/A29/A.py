import math

MOD = 10 ** 9 + 7
n = int(input())

ans = 1

for i in range(n):
    a = list(map(int, input().split()))
    ans *= sum(a)

print(ans % MOD)
