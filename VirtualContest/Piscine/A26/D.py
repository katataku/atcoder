n = int(input())

d = {}
for i in range(n):
    s = input()
    if s not in d.keys():
        print(i + 1)
        d[s] = 0
