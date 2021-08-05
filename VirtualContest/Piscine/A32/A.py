h, w = map(int, input().split())
a = []
for i in range(h):
    a_in = list(map(int, input().split()))
    a.append(a_in)
b = []
for i in range(h):
    b_in = list(map(int, input().split()))
    b.append(b_in)

cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        tar = a[i][j] - b[i][j]
        cnt += abs(tar)
        b[i][j + 1] += tar
        b[i + 1][j] += tar
        b[i + 1][j + 1] += tar

ans = "Yes"
for i in range(h - 1):
    if a[i][w - 1] != b[i][w - 1]:
        ans = "No"
        break
for j in range(w - 1):
    if a[h - 1][j] != b[h - 1][j]:
        ans = "No"
        break

if ans == "Yes":
    print(ans)
    print(cnt)
else:
    print(ans)
