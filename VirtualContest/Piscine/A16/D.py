n, k, m, r = map(int, input().split())
s = []
for i in range(n - 1):
    s_in = int(input())
    s.append(s_in)
s.sort(reverse=True)

border = k * r

current = sum(s[:k])

ans = 0
if border <= current:
    ans = 0
elif border > sum(s[: k - 1]) + m:
    ans = -1
else:
    ans = border - sum(s[: k - 1])

print(ans)