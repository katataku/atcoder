s = input()

ans = "Yes"
for i in range(len(s)):
    if i == 3 and s[i] != "-":
        ans = "No"
    if i != 3 and s[i] == "-":
        ans = "No"
print(ans)