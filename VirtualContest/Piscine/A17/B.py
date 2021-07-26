h, w = map(int, input().split())

s = []
for i in range(h):
    s_in = input()
    if "#" in s_in:
        s.append(s_in)

tar_width = 0
while tar_width < len(s[0]):
    flag = True
    for i in range(len(s)):
        if s[i][tar_width] == "#":
            flag = False
            break
    if flag:
        for i in range(len(s)):
            s[i] = s[i][:tar_width] + s[i][tar_width + 1 :]
    else:
        tar_width += 1

for i in range(len(s)):
    print("".join(s[i]))
