n = int(input())

s = []
t = []
for i in range(n):
    s_in, t_in = input().split()
    s.append(s_in)
    t.append(int(t_in))

x = input()
ans = sum(t[s.index(x) + 1 :])

print(ans)
