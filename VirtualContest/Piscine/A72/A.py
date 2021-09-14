n = int(input())

d = {}
d[0] = 2
d[1] = 1


def solve(n):
    if n not in d:
        d[n] = solve(n - 1) + solve(n - 2)
    return d[n]


print(solve(n))