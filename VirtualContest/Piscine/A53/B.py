n, k = map(int, input().split())


c = [0 for i in range(n + 1)]
ans = 0
for i in range(2, n + 1):
    if c[i] == 0:
        j = i
        while j <= n:
            c[j] += 1
            if c[j] == k:
                ans += 1
            j += i


print(ans)