from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())

arr = [[0 for j in range(n)] for i in range(n)]

k = int(input())

for i in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

l = int(input())

direc = []

for i in range(l):
    t, d = input().split()
    if d == "D":
        direc.append((int(t), 0))
    else:
        direc.append((int(t), 1))

time = 1
d = 1
cx = 0
cy = 0

q = deque()
q.append((0, 0))

arr[0][0] = 2

flag = False

for i in range(l):
    t = direc[i][0]

    while time <= t:
        nx = cx + dx[d]
        ny = cy + dy[d]


        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if arr[nx][ny] == 0:
                cx = nx
                cy = ny
                arr[nx][ny] = 2
                q.append((nx, ny))
                ex, ey = q.popleft()
                arr[ex][ey] = 0
            elif arr[nx][ny] == 1:
                cx = nx
                cy = ny
                arr[nx][ny] = 2
                q.append((nx, ny))
            else:
                flag = True
                break

        else:
            flag = True
            break

        time += 1

    if direc[i][1] == 0:
        d = (d+1)%4
    else:
        d = (d - 1+ 4) % 4


    if flag:
        break

if flag == False:

    while True:
        nx = cx + dx[d]
        ny = cy + dy[d]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if arr[nx][ny] == 0:
                cx = nx
                cy = ny
                arr[nx][ny] = 2
                q.append((nx, ny))
                ex, ey = q.popleft()
                arr[ex][ey] = 0
            elif arr[nx][ny] == 1:
                cx = nx
                cy = ny
                arr[nx][ny] = 2
                q.append((nx, ny))
            else:
                flag = True
                break

        else:
            flag = True
            break

        time += 1


print(time)


