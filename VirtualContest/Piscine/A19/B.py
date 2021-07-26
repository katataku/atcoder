n = int(input())
t = input()

s = "110" * (n)


if t in s:
    if t == "1":
        print((10 ** 10) * 2)
    elif t == "11":
        print((10 ** 10))
    else:
        k = t.count("0")
        if t[-1] == "0":
            print(10 ** 10 - k + 1)
        else:
            print(10 ** 10 - k)

else:
    print(0)
