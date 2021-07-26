h, w = map(int, input().split())

s = []

s.append(["." for i in range(w + 2)])

for i in range(h):
    s.append(list(input()))
    s[i + 1].insert(0, ".")
    s[i + 1] += "."
s.append(["." for i in range(w + 2)])

ans = "Yes"
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if (
                s[i - 1][j] != "#"
                and s[i + 1][j] != "#"
                and s[i][j - 1] != "#"
                and s[i][j + 1] != "#"
            ):
                ans = "No"
                break

print(ans)