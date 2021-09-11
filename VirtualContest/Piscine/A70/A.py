n = int(input())

d = {}
for i in range(n):
    d_in = int(input())
    if d_in not in d:
        d[d_in] = True

print(len(d))