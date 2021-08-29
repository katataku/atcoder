n = int(input())

s = []
t = []

ans = "No"
for i in range(n):
    s_in, t_in = map(str, input().split())
    if s_in in s and t_in in t:
        if s.index(s_in) == t.index(t_in):
            ans = "Yes"
            break
    s.append(s_in)
    t.append(t_in)
print(ans)