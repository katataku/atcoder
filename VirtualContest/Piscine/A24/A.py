n = int(input())

a = list(map(int, input().split()))
a.sort()
q = int(input())

for i in range(q):
    b = int(input())
    left = 0
    right = n
    tar = (left + right) // 2
    while left + 1 != right:
        tar = (left + right) // 2
        if a[tar] <= b:
            left = tar
        else:
            right = tar
    if left == n - 1:
        ans = abs(a[left] - b)
    else:
        ans = min(abs(a[left] - b), abs(a[left + 1] - b))
    print(ans)
