import heapq
from collections import defaultdict

n, m, x = map(int, input().split())

dist = [[float("inf") for j in range(n+1)] for i in range(n+1)]
graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n+1):
    dist[i][i] = 0

def distra(s):
    q = [(0, s)]
    
    while q:
        d, v = heapq.heappop(q)
        if dist[s][v] < d:
            continue
        for next, c in graph[v]:
            if dist[s][next] > d + c:
                dist[s][next] = d + c
                heapq.heappush(q, (d+c, next))

for i in range(1, n+1):
    distra(i)

max = 0
for i in range(1, n+1):
    if max < dist[i][x] + dist[x][i]:
        max = dist[i][x] + dist[x][i]

print(max)