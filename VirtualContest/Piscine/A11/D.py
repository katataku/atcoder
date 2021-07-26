n = int(input())

a = list(map(int, input().split()))
b = [-1 for i in range(n)]

ans = 0
for i in range(n):
    tar = n - i - 1
    b[tar] = a[tar]

    j = 1
    cnt = 0
    tar += 1
    while tar * j < n:
        cnt += b[(tar - 1) * j]
        j += 1
    if a[tar - 1] != cnt % 2:
        ans = -1
        break

if ans == -1:
    print(ans)
else:
    print(" ".join(map(str, a)))
