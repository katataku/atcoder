n, m = map(int, input().split())


s = []
c = []
for i in range(m):
    s_in, c_in = map(int, input().split())
    s.append(s_in)
    c.append(c_in)

start = 10 ** (n - 1)
end = 10 ** n
if start == 1:
    start = 0


tar = start
ans = -1
while tar < end:
    flag = True
    for i in range(m):
        if int(str(tar)[s[i] - 1]) != c[i]:
            flag = False
            break
    if flag == True:
        ans = tar
        break
    else:
        tar += 1

print(ans)
