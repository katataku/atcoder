s = input()
q = int(input())

flag = False
s_head = ""
s_tail = ""
for i in range(q):
    q_in = input()
    if q_in[0] == "1":
        flag = not flag
    else:
        f = q_in[2]
        if (f == "1" and not flag) or (f == "2" and flag):
            s_head = q_in[-1] + s_head
        else:
            s_tail = s_tail + q_in[-1]

s = s_head + s + s_tail
if flag:
    print(s[::-1])
else:
    print(s)
