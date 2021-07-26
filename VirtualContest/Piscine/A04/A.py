n = int(input())
a = list(map(int, input().split()))
ans = "APPROVED"
for i in a:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        ans = "DENIED"
        break

print(ans)