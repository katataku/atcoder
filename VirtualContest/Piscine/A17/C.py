import decimal

a, b = map(decimal.Decimal, input().split())

ans = a * b

print(int(ans))
