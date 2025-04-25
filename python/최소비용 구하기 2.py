import heapq
from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [float("inf") for i in range(n+1)]
prev_node = [0 for i in range(n+1)]

q = []
heapq.heappush(q, (0, start))
dist[start] = 0
while q:
    weight, node = heapq.heappop(q)

    if dist[node] < weight:
        continue

    for nextNode, cost in graph[node]:
        if dist[nextNode] > weight + cost:
            dist[nextNode] = weight + cost
            prev_node[nextNode] = node
            heapq.heappush(q, (weight+ cost, nextNode))

print(dist[end])

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))