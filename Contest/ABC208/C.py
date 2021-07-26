n, k = map(int, input().split())

a = list(map(int, input().split()))

ans = k // n

if k % n != 0:
    add_num = (k % n) - 1
    a_sorted = sorted(a)
    for i in a:
        if i <= a_sorted[add_num]:
            print(ans + 1)
        else:
            print(ans)
else:
    for i in a:
        print(ans)