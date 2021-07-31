import itertools

n = int(input())

a = []
for i in range(n):
    a_in = list(map(int, input().split()))
    a.append(a_in)

d = {}
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x not in d.keys():
        d[x] = [y]
    else:
        d[x].append(y)
    if y not in d.keys():
        d[y] = [x]
    else:
        d[y].append(x)

ans = 10 ** 10
for perm in itertools.permutations(range(n), n):
    perm = list(perm)
    flag = False
    for i in range(len(perm) - 1):
        if perm[i] in d and perm[i + 1] in d[perm[i]]:
            flag = True
            break
    if flag:
        continue
    tmp = 0
    for i in range(n):
        tmp += a[perm[i]][i]
    ans = min(ans, tmp)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
