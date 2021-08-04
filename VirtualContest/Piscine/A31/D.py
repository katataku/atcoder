h, w = map(int, input().split())
a = []
for i in range(h):
    a_in = list(map(int, input().split()))
    a.append(a_in)
b = []
for i in range(h):
    b_in = list(map(int, input().split()))
    b.append(b_in)

cnt = 0
for i in range(h):
    for j in range(w):
        cnt += abs(a[i][j] - b[i][j])
