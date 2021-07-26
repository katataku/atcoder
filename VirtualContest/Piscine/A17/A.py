n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = " ".join(map(str, list(filter(lambda i: i != x, a))))

print(ans)
