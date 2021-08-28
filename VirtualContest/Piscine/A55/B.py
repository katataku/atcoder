w, n = map(int, input().split())

l_hight = {}
ans = 0
lr_list = []
comp_list = []
for i in range(n):
    l, r = map(int, input().split())
    lr_list.append((l, r))
    if l not in comp_list:
        comp_list.append(l)
    if r not in comp_list:
        comp_list.append(r)

comp_list.sort()

for l, r in lr_list:
    hight = 0
    l = comp_list.index(l)
    r = comp_list.index(r)
    for i in range(l, r + 1):
        hight = max(l_hight.get(i, 0), hight)

    for i in range(l, r + 1):
        l_hight[i] = hight + 1

    print(hight + 1)
