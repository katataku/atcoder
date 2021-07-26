a, b = map(int, input().split())

count = 100
diff = max(9 - int(str(a)[0]), int(str(b)[0]) - 1)
if diff == 0:
    count = 10
    diff = max(9 - int(str(a)[1]), int(str(b)[1]) - 0)
if diff == 0:
    count = 1
    diff = max(9 - int(str(a)[2]), int(str(b)[2]) - 0)


print(a - b + (diff * count))
