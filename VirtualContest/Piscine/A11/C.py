n = int(input())

words = [[], []]
ans = "DRAW"
for i in range(n):
    s = input()
    if i == 0:
        words[i % 2].append(s)
        continue
    if (
        s in words[i % 2]
        or s in words[(i + 1) % 2]
        or s[0] != words[(i + 1) % 2][-1][-1]
    ):
        if i % 2 == 0:
            ans = "LOSE"
        else:
            ans = "WIN"
        break
    words[i % 2].append(s)

print(ans)