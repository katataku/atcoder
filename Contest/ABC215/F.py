n = int(input())

x, y = map(int, input().split())
edges = [[(x, y)], [(x, y)], [(x, y)], [(x, y)]]

ans = 0
for i in range(n - 1):
    x, y = map(int, input().split())
    for edgess in edges:
        for edge in edgess:
            tar_x, tar_y = edge
            ans = max(ans, min(abs(x - tar_x), abs(y - tar_y)))

    tar_x, tar_y = edges[0][0]
    if tar_x > x:
        edges[0] = [(x, y)]
    elif tar_x == x:
        edges[0].append((x, y))

    tar_x, tar_y = edges[1][0]
    if tar_x < x:
        edges[1] = [(x, y)]
    elif tar_x == x:
        edges[1].append((x, y))

    tar_x, tar_y = edges[2][0]
    if tar_y > y:
        edges[2] = [(x, y)]
    elif tar_y == y:
        edges[2].append((x, y))

    tar_x, tar_y = edges[3][0]
    if tar_y < y:
        edges[3] = [(x, y)]
    elif tar_y == y:
        edges[3].append((x, y))

print(ans)