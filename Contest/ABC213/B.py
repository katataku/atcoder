n = int(input())
a = list(map(int, input().split()))
asort = sorted(a)
print(a.index(asort[-2]) + 1)
