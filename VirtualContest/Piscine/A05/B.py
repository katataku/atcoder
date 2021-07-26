n = int(input())

ans = 0
s_now = input()
ans += s_now.count("x")
for i in range(len(s_now)):
    if s_now[i] == "o":
        ans += 1

for _ in range(n - 1):
    s_prev = s_now
    s_now = input()
    ans += s_now.count("x")
    for i in range(len(s_now)):
        if s_now[i] == "o" and s_prev[i] != "o":
            ans += 1


print(ans)
