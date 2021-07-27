n = int(input())


def solve(n, cnt):
    if n == 0:
        return [""]
    else:
        ans = []
        if n > cnt:
            cnt0_list = solve(n - 1, cnt + 1)
            ans += list(map(lambda s: "(" + s, cnt0_list))

        if cnt > 0:
            cnt1_list = solve(n - 1, cnt - 1)
            ans += list(map(lambda s: ")" + s, cnt1_list))

        return ans


if n % 2 == 0 and n > 1:
    ans = solve(n, 0)
    for i in ans:
        print(i)
