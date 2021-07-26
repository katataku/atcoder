a, b = map(int, input().split())

s = input()

ans = "Yes"
for i in range(len(s)):
    if i == a:
        if s[i] != "-":
            ans = "No"
    else:
        if not s[i].isnumeric():
            ans = "No"

print(ans)