import bisect

n = int(input())

INF = 10 ** 10
a = list(map(int, input().split()))

a_LIS = [INF for i in range(n)]
b_LIS = [INF for i in range(n)]

a_ans = []
b_ans = []
for i in range(n):
    tar = a[i]
    index = bisect.bisect_left(a_LIS, tar)
    a_LIS[index] = tar
    a_ans.append(index + 1)

for i in range(n - 1, -1, -1):
    tar = a[i]
    index = bisect.bisect_left(b_LIS, tar)
    b_LIS[index] = tar
    b_ans.append(index + 1)

b_ans = b_ans[::-1]

ans = 0
for i in range(n):
    ans = max(ans, a_ans[i] + b_ans[i] - 1)
print(ans)
