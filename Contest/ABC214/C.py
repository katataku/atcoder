n = int(input())

s = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = []
for i in range(n):
    if i == 0:
        ans.append(t[i])
    else:
        ans.append(min(t[i], ans[i - 1] + s[i - 1]))

for i in range(n):
    ans[i] = min(t[i], ans[(i - 1)] + s[i - 1])


for i in range(n):
    print(ans[i])