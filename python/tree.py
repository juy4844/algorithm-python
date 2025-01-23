from collections import deque

n, m = map(int, input().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = input()

dist = [[0 for j in range(m)] for i in range(n)]
visited = [[0 for j in range(m)] for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ex = 0
ey = 0

q = deque()
ghost = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'G':
            ghost.append((i, j, 0))
        elif arr[i][j] == 'N':
            q.append((i, j, 0))
        elif arr[i][j] == 'D':
            ex = i
            ey = j

while len(ghost) > 0:
    r, c, d = ghost.popleft()
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < m:
            if dist[nx][ny] == 0:
                dist[nx][ny] = d+1
                ghost.append((nx, ny, d+1))

bo = False

while len(q) > 0:
    r, c, d = q.popleft()
    if r == ex and c == ey:
        if dist[r][c] > d:
            bo = True
            break
        else:
            break
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < m:
            if dist[nx][ny] > d + 1 and arr[nx][ny] != '#' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, d+1))

if bo == True:
    print("Yes")
else:
    print("No")