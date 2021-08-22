k = int(input())


def prime_f_multi(num):
    divisors = {}
    for i in range(2, num):
        k = 0
        while (num % i) == 0:
            k += 1
            num //= i
        if k != 0:
            divisors[i] = k
    if not divisors and num != 1:
        divisors[num] = 1
    return divisors


ans_list = {}


def solve(rest, dic, a, b, c):
    global ans_list
    if len(dic) == 0:
        if a <= b and b <= c and (a, b, c) not in ans_list:
            ans_list[(a, b, c)] = True
            return 1
        else:
            return 0
    else:
        key, value = dic.popitem()
        if value > 1:
            dic[key] = value - 1
        ans = 0
        rest = rest // key
        if a <= b * rest:
            ans += solve(rest, dic.copy(), a * key, b, c)
            ans += solve(rest, dic.copy(), a, b * key, c)
        if b <= c * rest:
            ans += solve(rest, dic.copy(), a, b, c * key)
        return ans


print(solve(k, prime_f_multi(k).copy(), 1, 1, 1))