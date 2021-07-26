n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = "No"
if x >= sum(a) - (n // 2):
    ans = "Yes"

print(ans)
