n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

acc = 0
for i in range(n):
    acc += abs(a[i] - b[i])

if acc <= k and acc % 2 == k % 2:
    print("Yes")
else:
    print("No")