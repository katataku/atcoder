s = input()
ans = 0

tar = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ans += 1
        if i < len(s) - 1:
            if s[i] == "0":
                s = s[:i] + "1" + s[i + 1 :]
            else:
                s = s[:i] + "0" + s[i + 1 :]

print(ans)