from collections import defaultdict
from collections import deque

n, m = map(int, input().split())

graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

left = 1
right = 1000000001
while left < right:
    mid = (left + right) //2

    q = deque()
    q.append(start)

    visited = [False for i in range(n+1)]
    visited[start] = True

    while q:
        v = q.popleft()
        for a, c in graph[v]:
            if visited[a] == False and c >= mid:
                visited[a] = True
                q.append(a)

    if visited[end] == True:
        left = mid + 1
    else:
        right = mid

print(right-1)




