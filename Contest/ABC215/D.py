import math

n, m = map(int, input().split())
a = list(map(int, input().split()))


def lcm(x, y):
    return x * y // math.gcd(x, y)


def make_divisors(N):
    divisors = []
    for i in range(1, int(N ** 0.5) + 1):  # ポイント①
        if N % i == 0:  # ポイント②
            divisors.append(i)
            if i != N // i:  # ポイント③
                divisors.append(N // i)
    return divisors


d = {}
for item in a:
    for divitem in make_divisors(item):
        if divitem not in d and divitem != 1:
            d[divitem] = True
            acc = divitem
            while acc < m:
                acc += divitem
                d[acc] = True
ans = []
for i in range(m):
    i = i + 1
    if i not in d:
        ans.append(i)

print(len(ans))
for item in ans:
    print(item)