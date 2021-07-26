n = int(input())

d = {}

a = list(map(int, input().split()))

max1 = 0
max2 = 0

for i in a:
    if i in d.keys():
        d[i] += 1
        if i > max1 and d[i] % 2 == 0:
            max2 = max1
            max1 = i
        elif i > max2 and d[i] % 2 == 0:
            max2 = i

    else:
        d[i] = 1

print(max1 * max2)
