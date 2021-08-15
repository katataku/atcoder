n, k = map(int, input().split())

a = list(map(int, input().split()))
ans = 0
tmp = 0
d = {}
left = 0
right = 0
while right < n:
    if len(d) < k:
        if a[right] in d:
            d[a[right]] += 1
        else:
            d[a[right]] = 1
        right += 1
        ans = max(ans, right - left)
    elif len(d) == k:
        if a[right] in d:
            d[a[right]] += 1
            right += 1
            ans = max(ans, right - left)
        else:
            tmp = d.pop(a[left])
            if tmp == 1:
                d[a[right]] = 1
                left += 1
                right += 1
            else:
                d[a[left]] = tmp - 1
                left += 1
    else:
        tmp = d.pop[a[left]]
        if tmp > 1:
            d[a[left]] = tmp - 1
        left += 1
print(ans)
