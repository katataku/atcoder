MOD = 10 ** 9 + 7
n = int(input())

s = input()

ATCODER = "atcoder"


def solve(tar, index):
    if index == 6:
        return s.count("r", tar) % MOD
    if tar == n:
        return 0
    if s[tar] != ATCODER[index]:
        ans = 0
        tmp = s[tar + 1 :].find(ATCODER[index + 1])
        if tmp != -1:
            ans += solve(tar + 1 + tmp, index + 1) % MOD
        return ans
    else:
        ans = (solve(tar + 1, index + 1)) % MOD
        tmp = s[tar + 1 :].find(ATCODER[index])
        if tmp != -1:
            ans += solve(tar + 1 + tmp, index) % MOD
        return ans % MOD


print(solve(0, 0))

