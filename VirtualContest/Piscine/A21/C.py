s = input()
ans = [1 for i in range(len(s))]
index = 0


while index < len(s) - 2:
    if s[index] == "R":
        if s[index + 1] == "R":
            ans[index + 2] += ans[index]
            ans[index] = 0
    index += 1

index = len(s) - 1
while index > 0:
    if s[index] == "L":
        if s[index - 1] == "L":
            ans[index - 2] += ans[index]
            ans[index] = 0
    index -= 1


print(" ".join(map(str, ans)))
