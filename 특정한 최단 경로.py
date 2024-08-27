from collections import defaultdict
import heapq

n, e = map(int, input().split())

dic = defaultdict(list)
for i in range(e):
    a, b, c = map(int, input().split())
    dic[a].append((b, c))
    dic[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = [float("inf") for i in range(n+1)]
distv1 = [float("inf") for i in range(n+1)]
distv2 = [float("inf") for i in range(n+1)]
dist1[1] = 0
distv1[v1] = 0
distv2[v2] = 0


q = [(0, 1)]
while q:
    c, v = heapq.heappop(q)
    if c > dist1[v]:
        continue
    for u, d in dic[v]:
        if dist1[u] > c + d:
            dist1[u] = c + d
            heapq.heappush(q, (c+d, u))

q = [(0, v1)]
while q:
    c, v = heapq.heappop(q)
    if c > distv1[v]:
        continue
    for u, d in dic[v]:
        if distv1[u] > c + d:
            distv1[u] = c + d
            heapq.heappush(q, (c+d, u))

q = [(0, v2)]
while q:
    c, v = heapq.heappop(q)
    if c > distv2[v]:
        continue
    for u, d in dic[v]:
        if distv2[u] > c + d:
            distv2[u] = c + d
            heapq.heappush(q, (c+d, u))


result = 0
if dist1[v1]+distv1[v2]+distv2[n] == float("inf") and dist1[v2]+distv2[v1]+distv1[n] == float("inf"):
    print(-1)
elif dist1[v1]+distv1[v2]+distv2[n] < dist1[v2]+distv2[v1]+distv1[n]:
    print(dist1[v1]+distv1[v2]+distv2[n])
else:
    print(dist1[v2]+distv2[v1]+distv1[n])


