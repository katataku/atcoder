import math

n = int(input())

list_pos = []
sum_x = []
sum_y = []
for i in range(n):
    x, y = map(int, input().split())
    sum_x.append(x)
    sum_y.append(y)
    list_pos.append((x, y))


sum_x.sort()
sum_y.sort()
pos_x = sum_x[n // 2]
pos_y = sum_y[n // 2]

ans = 0
for tar_x, tar_y in list_pos:
    ans += abs(pos_x - tar_x) + abs(pos_y - tar_y)

print(int(ans))