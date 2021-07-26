n, m = map(int, input().split())

ans = 0
count = 1
while count < m:
    count += n - 1
    ans += 1


print(ans)
