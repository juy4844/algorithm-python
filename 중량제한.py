from collections import defaultdict
import heapq

n, m = map(int, input().split())

graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

maxweight = [0 for i in range(n+1)]
visited = [False for i in range(n+1)]
visited[start] = True
maxweight[start] = float("inf")

heap = []
heap.append((-float("inf"), start))

while heap:
    weight, v = heapq.heappop(heap)
    weight *= -1

    if v == end:
        break

    for a, c in graph[v]:
        temp = 0
        if c >= weight:
            temp = weight
        else:
            temp = c
        
        if maxweight[a] < temp:
            maxweight[a] = temp
            heapq.heappush(heap, (temp * -1, a))

print(maxweight[end])