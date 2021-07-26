    import copy
    n = int(input())

    x = []
    y = []
    for i in range(n):
        x_in, y_in = map(int, input().split())
        x.append(x_in)
        y.append(y_in)
    x_org = copy.deepcopy(x)
    y_org = copy.deepcopy(y)
    x.sort()
    y.sort()

    tar = [
        abs(x[0] - x[-1]),
        abs(x[1] - x[-1]),
        abs(x[0] - x[-2]),
        abs(y[0] - y[-1]),
        abs(y[1] - y[-1]),
        abs(y[0] - y[-2]),
    ]
    tar.sort()
    ans = -2
    if x_org.index(x[0]) == y_org.index(y[0]) and x_org.index(x[-1]) == y_org.index(y[-1]):
        ans -= 1

    print(tar[ans])