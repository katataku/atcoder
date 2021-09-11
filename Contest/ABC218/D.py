n = int(input())

xy_list = {}
xy_list_rev = {}
for i in range(n):
    x, y = map(int, input().split())
    xy_list[i] = (x, y)
    xy_list_rev[(x, y)] = True
ans = 0

for i in range(n - 1):
    x1, y1 = xy_list[i]
    for j in range(i + 1, n):
        x2, y2 = xy_list[j]
        if x1 == x2 or y1 == y2:
            continue
        if (x1, y2) in xy_list_rev and (x2, y1) in xy_list_rev:
            ans += 1
print(ans // 2)
