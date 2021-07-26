n, m = map(int, input().split())

parentlist = [i for i in range(n)]


def parent(a):
    if a != parentlist[a]:
        parentlist[a] = parent(parentlist[a])
    return parentlist[a]


def find(a):
    return parent(a)


def union(a, b):
    if parent(a) == parent(b):
        pass
    else:
        if parent(a) > parent(b):
            a, b = b, a
        parentlist[parent(b)] = parent(a)


for i in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

ans = 0
for i in range(n):
    if parent(0) != parent(i):
        union(0, i)
        ans += 1

print(ans)
