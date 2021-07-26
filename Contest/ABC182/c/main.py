# -*- coding: utf-8 -*-

# Input#
s = input()
# n, k = map(int, input().split())
# p = list(map(int, input().split()))


def check(cnt, accum, s):
    if len(s) < 1:
        if (accum) % 3 == 0 and accum != 0:
            return cnt
        else:
            return -1

    if (accum + int(s)) % 3 == 0:
        return cnt

    ans1 = check(cnt + 1, accum, s[1:])
    ans2 = check(cnt, accum + int(s[0]), s[1:])

    if ans1 != -1 and ans2 != -1:
        return min(ans1, ans2)

    if ans1 == -1 and ans2 == -1:
        return -1

    return max(ans1, ans2)


ans = check(0, 0, str(s))

print("{}".format(ans))

