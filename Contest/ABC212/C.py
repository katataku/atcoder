n, m = map(int, input().split())

index1 = 0
index2 = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 10 ** 10
while index1 < n and index2 < m:
    tmp = abs(a[index1] - b[index2])
    ans = min(tmp, ans)
    if a[index1] < b[index2]:
        index1 += 1
    else:
        index2 += 1

print(ans)