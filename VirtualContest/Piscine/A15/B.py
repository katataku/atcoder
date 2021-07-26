s = input()

keyence = "keyence"
is_Head = True
ans = "YES"
for i in range(len(keyence)):
    if is_Head:
        if s[i] == keyence[i]:
            continue
        else:
            is_Head = False

    if not is_Head:
        if s[-7 + i] == keyence[i]:
            continue
        else:
            ans = "NO"

print(ans)