n = int(input())

ans_list = [0 for i in range(n + 1)]

MAX = 100
for x in range(1, MAX):
    for y in range(1, MAX):
        for z in range(1, MAX):
            tar = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if tar <= n:
                ans_list[tar] += 1
            else:
                break

for i in range(n):
    print(ans_list[i + 1])
