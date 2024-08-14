from collections import defaultdict
import heapq

n, m = map(int, input().split())
k = int(input())

dic = defaultdict(list)

for i in range(m):
    u, v, w = map(int, input().split())
    dic[u].append((v, w))

arr = [float("inf") for i in range(n+1)]
arr[k] = 0

heap = []
heapq.heappush(heap, (0,k))
while heap:
    d, p = heapq.heappop(heap)
    if arr[p] < d:
        continue
    for v, w in dic[p]:
        if arr[v] > d + w:
            arr[v] = d+w
            heapq.heappush(heap, (d+w, v))

for i in range(1, n+1):
    if arr[i] == float("inf"):
        print("INF")
    print(arr[i])

