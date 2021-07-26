h, w, c = map(int, input().split())

a = []
for i in range(h):
    a_in = list(map(int, input().split()))
    a.append(a_in)
ans = 10 ** 20

for i in range(h):
    for j in range(w):
        if a[i][j] >= ans:
            continue
        for i2 in range(i, h):
            if a[i][j] + c * abs(i - i2) >= ans:
                break
            for j2 in range(w):
                if a[i][j] + c * (abs(i - i2) + abs(j - j2)) >= ans and j < j2:
                    break
                if i != i2 or j != j2:
                    tmp = a[i][j] + a[i2][j2] + c * (abs(i - i2) + abs(j - j2))
                    ans = min(ans, tmp)

print(ans)
