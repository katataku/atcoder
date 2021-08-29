s = input()
ans = s[:-2]
if int(s[-1]) <= 2:
    ans += "-"
if int(s[-1]) >= 7:
    ans += "+"
print(ans)
