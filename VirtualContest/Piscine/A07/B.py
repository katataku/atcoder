n = int(input())
s = input()

ans = 0
if n % 2 == 0:
    for i in range(n // 2):
        if s[i] != s[i + (n // 2)]:
            ans += 1
else:
    ans = -1
print(ans)
