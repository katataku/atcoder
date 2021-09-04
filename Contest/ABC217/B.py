ans_list = ["ABC", "ARC", "AGC", "AHC"]
bit_list = [0, 0, 0, 0]

for i in range(3):
    s = input()
    bit_list[ans_list.index(s)] = 1

for i in range(4):
    if bit_list[i] == 0:
        ans = ans_list[i]
print(ans)