n, q = map(int, input().split())

a = list(map(int, input().split()))

rot = 0
for i in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if t == 1:
        x = (x - rot) % n
        y = (y - rot) % n
        a[x], a[y] = a[y], a[x]
    if t == 2:
        rot += 1
    if t == 3:
        tar = (x - rot) % n
        ans = a[tar]
        print(ans)
