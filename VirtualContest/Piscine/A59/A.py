n = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


d = {}
ans = [1]
for i in range(1, n):
    i += 1
    cnt = 0
    for item in factorization(i):
        cnt += item[1]
    ans.append(cnt + 1)

print(" ".join(map(str, ans)))
