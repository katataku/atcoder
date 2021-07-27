n = int(input())
list1 = [0]
list2 = [0]

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        list1.append(list1[-1] + p)
        list2.append(list2[-1])
    else:
        list1.append(list1[-1])
        list2.append(list2[-1] + p)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    ans1 = list1[r] - list1[l - 1]
    ans2 = list2[r] - list2[l - 1]
    print(ans1, ans2)
