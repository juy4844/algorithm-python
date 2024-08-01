from collections import deque

r, c = map(int, input().split())

arr = [0 for i in range(r)]

fx, fy, jx, jy = 0, 0, 0, 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = -1
q = deque()
fire = [[-1 for j in range(c)] for i in range(r)]

for i in range(r):
    arr[i] = input()

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'F':
            q.append((i,j,0))
            fire[i][j] = 0
        elif arr[i][j] == 'J':
            jx = i
            jy = j

# 불 퍼지는 최단 거리를 미리 구한다            

while q:
    px, py, cost = q.popleft()
    for d in range(4):
        nx = px + dx[d]
        ny = py + dy[d]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if fire[nx][ny] == -1 and arr[nx][ny] != '#':
                fire[nx][ny] = cost+1
                q.append((nx, ny, cost+1))


jihon = [[-1 for j in range(c)] for i in range(r)]
jq = deque()
jq.append((jx, jy, 0))
jihon[jx][jy] = 0
bo = False
while jq:
    px, py, cost = jq.popleft()
    if px == 0 or px == r-1 or py == 0 or py == c-1:
        ans = cost
        bo = True
    for d in range(4):
        nx = px + dx[d]
        ny = py + dy[d]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if jihon[nx][ny] == -1 and arr[nx][ny] != '#':
                if fire[nx][ny] > cost+1 or fire[nx][ny] == -1:
                    jihon[nx][ny] = cost+1
                    jq.append((nx, ny, cost+1))
    
    if bo == True:
        break

if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans+1)
