n, k, s = map(int, input().split())

ans = []
for i in range(k):
    ans.append(s)

for i in range(n - k):
    ans.append((s + 1) % 10 ** 9)

print(" ".join(map(str, ans)))
