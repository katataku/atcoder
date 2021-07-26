n, k = map(int, input().split())

a = list(map(int, input().split()))

left = 0
right = 0
ans = 0
acc = a[0]
while True:
    if acc >= k and right - left >= 0:
        ans += n - right
        acc -= a[left]
        left += 1
    else:
        right += 1
        if right == n:
            break
        acc += a[right]

print(ans)