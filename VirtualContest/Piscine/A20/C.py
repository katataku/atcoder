n = int(input())

s = input()

e_list = []
w_list = []

if s[0] == "W":
    e_list.append(1)
else:
    e_list.append(0)

if s[-1] == "E":
    w_list.append(1)
else:
    w_list.append(0)

for i in range(1, n):
    if s[i] == "W":
        e_list.append(e_list[-1] + 1)
    else:
        e_list.append(e_list[-1])

    if s[-i - 1] == "E":
        w_list.append(w_list[-1] + 1)
    else:
        w_list.append(w_list[-1])

w_list.append(0)
w_list.insert(0, 0)
e_list.append(0)
e_list.insert(0, 0)

w_list.reverse()
ans = 10 ** 10
for i in range(1, n + 1):
    tmp = e_list[i - 1] + w_list[i + 1]
    ans = min(ans, tmp)

print(ans)
