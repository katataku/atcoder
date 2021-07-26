n = int(input())

cnt = 0
for i in range(n):
    n, m = map(int, input().split())
    if n == m:
        cnt += 1
        if cnt == 3:
            break
    else:
        cnt = 0

if cnt == 3:
    print("Yes")
else:
    print("No")
