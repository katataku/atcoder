h, w = map(int, input().split())

a = []
b = []
h_list = []
w_list = [0 for i in range(w)]
for i in range(h):
    a_in = list(map(int, input().split()))
    a.append(a_in)
    b.append([])
    h_list.append(sum(a_in))
    w_list = [a + b for a, b in zip(w_list, a_in)]

for i in range(h):
    print(" ".join(map(lambda j: str(h_list[i] + w_list[j] - a[i][j]), range(w))))
