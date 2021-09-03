s = input()
t = input()

s = list(s)
t = list(t)
s.sort()
t.sort(reverse=True)


ans = "No"

n = len(s)
m = len(t)
index = 0


def gt(s, t):
    if len(t) == 0:
        return False
    if len(s) == 0:
        return True

    if s[0] == t[0]:
        return gt(s[1:], t[1:])
    else:
        return s[0] < t[0]


if gt(s, t):
    ans = "Yes"
print(ans)