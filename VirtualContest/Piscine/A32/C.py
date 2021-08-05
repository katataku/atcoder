n = int(input())

s = input()

d = {"o": 0, "x": 0}

start = 0
end = 0
ans = 0
d[s[end]] += 1
while end < n:
    if d["o"] == 0 or d["x"] == 0:
        end += 1
        if end < n:
            d[s[end]] += 1
    else:
        ans += n - end
        d[s[start]] -= 1
        start += 1

print(ans)