n = int(input())

if n < 126:
    ans = 4
elif n > 211:
    ans = 8
else:
    ans = 6
print(ans)