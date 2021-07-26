c = []
c.append(list(map(int, input().split())))
c.append(list(map(int, input().split())))
c.append(list(map(int, input().split())))

ans = "Yes"
for i in range(2):
    for j in range(2):
        if (
            c[i][j] - c[i][(j + 1) % 3]
            != c[(i + 1) % 3][j] - c[(i + 1) % 3][(j + 1) % 3]
        ):
            ans = "No"

print(ans)