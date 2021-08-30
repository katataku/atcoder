n, q = map(int, input().split())

a = list(map(int, input().split()))

b = []
for i in range(n):
    if i == 0:
        b.append(a[0] - 1)
    else:
        b.append(b[-1] + (a[i] - a[i - 1] - 1))


for i in range(q):
    k = int(input())
    ans = k
    if k >= a[0]:
        left = 0
        right = n
        while right - left > 1:
            mid = (right + left) // 2
            if b[mid] >= k:
                right = mid
            else:
                left = mid
        rest = k - b[left]
        ans = a[left] + rest

    print(ans)
