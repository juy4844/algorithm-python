from collections import deque

n, m = map(int, input().split())

arr = [0 for i in range(n)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    arr[i] = list(map(int, input().split()))


cnt = 0
while True:
    piece = 0
    visited = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visited[i][j] == 0:
                piece += 1
                if piece == 2:
                    print(cnt)
                    exit()
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    px, py = q.popleft()
                    for d in range(4):
                        nx = px + dx[d]
                        ny = py + dy[d]
                        if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                            if arr[px][py] != 0:
                                arr[px][py] -= 1
                        if arr[nx][ny] != 0 and visited[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
    cnt += 1
    
    if piece == 0:
        print(0)
        break
            


