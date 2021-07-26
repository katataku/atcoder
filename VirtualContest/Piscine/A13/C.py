a, b, c = map(int, input().split())


# b %= 10
# c %= 10
# c %= 4
# if c == 0:
#     c = 4


bc = 0
if b % 4 == 2 and c % 2 == 1:
    if c == 1:
        bc = 2
    else:
        bc = 0
else:
    bc = b ** ((c % 2) + 2)

bc %= 4
if bc == 0:
    bc = 4


a %= 10
ans = a ** (bc)
print(ans % 10)
