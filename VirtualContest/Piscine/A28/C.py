import heapq

n, k = map(int, input().split())

h = []
heapq.heapify(h)


for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(h, b * -1)
    heapq.heappush(h, (a - b) * -1)

ans = 0
for i in range(k):
    ans += heapq.heappop(h) * -1

print(ans)