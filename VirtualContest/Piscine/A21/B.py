s = input()
flag = True
ans = 0
cnt_w = 0
cnt_b = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == "W":
        cnt_w += 1
    else:
        cnt_b += 1
        ans += cnt_w

print(ans)
