x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

x_a -= x_c
x_b -= x_c

y_a -= y_c
y_b -= y_c

ans = abs(x_a * y_b - y_a * x_b) / 2

print(ans)
