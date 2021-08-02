q = int(input())

a = []
for i in range(q):
    t, x = map(int, input().split())

    if t == 1:
        a.insert(0, x)
    if t == 2:
        a.append(x)
    if t == 3:
        print(a[x - 1])
