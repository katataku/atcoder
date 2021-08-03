import math

n, k = map(int, input().split())
MOD = 10 ** 9 + 7


def power_func(a, n, p):
    bi = str(format(n, "b"))  # 2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res


ans = 0
if n == 1:
    ans = k
else:
    if k == 1:
        ans = 0
    elif k == 2:
        if n == 2:
            ans = 2
        else:
            ans = 0
    else:
        ans = k * (k - 1)
        ans %= MOD
        tmp = power_func((k - 2), (n - 2), MOD)
        tmp %= MOD
        ans *= tmp
        ans %= MOD

print(ans % MOD)
