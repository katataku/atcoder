n, k = map(int, input().split())


def base10int(value, base):
    if value // base:
        return base10int((value // base), base) + str(value % base)
    return str(value % base)


for i in range(k):
    tmp = int(str(n), 8)
    n = int(base10int(tmp, 9).replace("8", "5"))
print(n)
