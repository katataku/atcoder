n = int(input())

p = list(map(int, input().split()))

ans_list = [0 for i in range(n)]
for i in range(n):
    ans_list[p[i] - 1] = i + 1

print(" ".join(map(str, ans_list)))
