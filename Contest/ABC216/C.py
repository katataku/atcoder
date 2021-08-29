n = int(input())

ans = ""
tar = n

while tar > 0:
    if tar % 2 == 0:
        ans = "B" + ans
        tar = tar // 2
    else:
        ans = "A" + ans
        tar -= 1
print(ans)
