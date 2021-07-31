import heapq

q = int(input())

acc = 0
a = []
heapq.heapify(a)
for i in range(q):
    s = input()
    if s[0] == "1":
        x = int(s[2:])
        heapq.heappush(a, x - acc)
    if s[0] == "2":
        x = int(s[2:])
        acc += x
    if s[0] == "3":
        print(heapq.heappop(a) + acc)
