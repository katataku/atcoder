alp_list = "abcdefghijklmnopqrstuvwxyz"

a = list(map(int, input().split()))

ans = ""
for i in a:
    ans += alp_list[i - 1]
print(ans)