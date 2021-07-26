n, m = map(int, input().split())

flag_even = False
flag_odd = False
odd_min = 10 ** 10
even_min = 10 ** 10

for i in range(m):
    a_in, c_in = map(int, input().split())
    if a_in % 2 == 0:
        flag_even = True
        even_min = min(even_min, c_in)
    else:
        flag_odd = True
        odd_min = min(odd_min, c_in)

if flag_even and flag_odd:
    ans = even_min * (n - 2) + odd_min
    print(ans)
else:
    print(-1)