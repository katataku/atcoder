n = int(input())

s = input()

i = 0
ans = 0
for i in range(n):
    if s[i] == "1":
        ans = i
        break

if ans % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")