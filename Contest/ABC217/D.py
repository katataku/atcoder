import bisect
import array


l, q = list(map(int, input().split()))

a = array.array("i", [0, l])
for i in range(q):
    c, x = map(int, input().split())

    z = bisect.bisect_left(a, x)
    if c == 1:
        a.insert(z, x)
    else:
        print(a[z] - a[z - 1])
