from collections import defaultdict
from collections import deque

n = int(input())
m = int(input())

dic = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

ans = 0

visited = [0 for i in range(n+1)]
visited[1]=1
q = deque()
q.append(1)
while q:
    v = q.popleft()
    for i in dic[v]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            ans += 1

print(ans)    