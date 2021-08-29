n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if i < j:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
b_acc = []

for i in range(n):
    if i == 0:
        b_acc.append(b[i])
    else:
        b_acc.append(b[i] + b[i - 1])


ans = 0
index = 0
acc = 0
while a[index] >= b_acc[index]:
    index += 1
    if index == n:
        break
    ans += 2 ** (index - 1)
    ans %= 998244353
print(ans)
