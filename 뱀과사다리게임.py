from collections import defaultdict
from collections import deque
import heapq

n, m = map(int, input().split())

lab = defaultdict(int)

for i in range(n+m):
    a, b = map(int, input().split())
    lab[a] = b

visited = [False] * 101

q = deque()
q.append((1, 0))
visited[1] = True

while q:
    loc, cnt = q.popleft()
    if loc == 100:
        print(cnt)
        break

    for i in range(1, 7):
        next = loc + i
        if 0 < next <= 100 and not visited[next]:
            if next in lab:
                next = lab[next]
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt + 1))
    