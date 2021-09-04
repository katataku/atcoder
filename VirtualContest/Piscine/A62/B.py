n = int(input())

a_list = []
for i in range(n):
    l, r = map(int, input().split())
    a_list.append((l, r))


ans = 0
for i in range(n):
    li, ri = a_list[i]
    for j in range(i + 1, n):
        lj, rj = a_list[j]
        cnt = 0
        for tmp in range(lj, rj + 1):
            cnt += max(0, ri - max(li - 1, tmp))
        ans += (cnt) / ((ri - li + 1) * (rj - lj + 1))

print(ans)