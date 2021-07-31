s = input()

x = [0, 0, 0, 0]
for i in range(4):
    x[i] = int(s[i])

ans1 = "Weak"

for i in range(3):
    if x[i] != x[i + 1]:
        ans1 = "Strong"

ans2 = "Weak"

for i in range(3):
    if x[i + 1] != (x[i] + 1) % 10:
        ans2 = "Strong"

ans = "Weak"
if ans1 == "Strong" and ans2 == "Strong":
    ans = "Strong"

print(ans)