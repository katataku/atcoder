n = int(input())

s = input()
d = {}


def solve(index, last):
    ans = 0
    res_d = d.get(s[index], 0)
    if index == n - 1:
        if res_d == 0 or s[index] == last:
            ans = 2
        else:
            ans = 0
    else:
        if res_d == 0:
            ans = solve(index + 1, last)
            d[s[index]] = 1
            if s[index] != last:
                tmp = solve(index + 1, s[index])
                if tmp != 0:
                    ans *= tmp
        else:
            if s[index] != last:
                ans = solve(index + 1, last)
            else:
                ans = 2 * solve(index + 1, last)
    return ans


print(solve(0, ""))
