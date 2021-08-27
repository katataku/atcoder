n, q = map(int, input().split())


x = []
y = []
x_min = 10 ** 10
y_min = 10 ** 10

x_max = 10 ** 10 * (-1)
y_max = 10 ** 10 * (-1)

for _ in range(n):
    x_in, y_in = map(int, input().split())
    x45 = x_in - y_in
    y45 = x_in + y_in

    x.append(x45)
    y.append(y45)

    x_min = min(x_min, x45)
    x_max = max(x_max, x45)
    y_min = min(y_min, y45)
    y_max = max(y_max, y45)


for _ in range(q):
    index = int(input())
    index -= 1
    tar_x = x[index]
    tar_y = y[index]

    ans = max(
        abs(tar_x - x_min), abs(tar_x - x_max), abs(tar_y - y_min), abs(tar_y - y_max)
    )
    print(ans)
