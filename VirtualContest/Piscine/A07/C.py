n = int(input())

d = {}
ans = 0
a = list(map(int, input().split()))
for i in a:
    ans += i
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    if b in d:
        ans += (c - b) * d[b]
        if c in d:
            d[c] += d[b]
        else:
            d[c] = d[b]
        d[b] = 0
    print(ans)
