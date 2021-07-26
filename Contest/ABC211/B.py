tar_list = ["H", "2B", "3B", "HR"]

ans_list = [0, 0, 0, 0]

for i in range(4):
    s = input()
    ans_list[tar_list.index(s)] = 1

if sum(ans_list) == 4:
    print("Yes")
else:
    print("No")
