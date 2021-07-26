import statistics
import math

n = int(input())

a = list(map(int, input().split()))

x = statistics.median(a) / 2

ans = 0
for i in a:
    ans += x + i - min(i, x * 2)

print(ans / n)
