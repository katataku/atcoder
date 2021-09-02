n, m = map(int, input().split())

path = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a] += 1
    path[b] += 1

for i in range(n):
    print(path[i])