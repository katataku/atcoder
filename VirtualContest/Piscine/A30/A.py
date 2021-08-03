n, q = map(int, input().split())


a = list(map(int, input().split()))
b = [0]
acc = 0
for i in range(n - 1):
    b.append(a[i + 1] - a[i])
    acc += abs(a[i + 1] - a[i])

for i in range(q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    if l > 0:
        acc -= abs(b[l])
        b[l] += v
        acc += abs(b[l])
    if r < n - 1:
        acc -= abs(b[r + 1])
        b[r + 1] -= v
        acc += abs(b[r + 1])
    print(acc)