s = input()

n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    s = s[0:l] + s[r : min(l - 1, 0) : -1] + s[r + 1 :]

print(s)
