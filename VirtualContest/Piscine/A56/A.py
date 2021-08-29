n = int(input())

for i in range(n):
    tar = int(input())
    ans = ""
    if tar % 2 == 0:
        if tar % 4 == 0:
            ans = "Even"
        else:
            ans = "Same"
    else:
        ans = "Odd"
    print(ans)