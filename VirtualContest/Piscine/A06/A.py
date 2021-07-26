import math

n = int(input())

ans = 1
for i in range(n):
    if i * i > n:
        break
    ans = i * i

print(ans)