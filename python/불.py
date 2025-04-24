from collections import deque

t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(arr, h, w):
    fireVisited = [[-1 for j in range(w)] for i in range(h)]
    fireQ = deque()

    sangVisited = [[-1 for j in range(w)] for i in range(h)]
    sangQ = deque()

    for i in range(h):
        for j in range(w):
            if arr[i][j] == "*":
                fireVisited[i][j] = 0
                fireQ.append((i, j))
            if arr[i][j] == "@":
                sangVisited[i][j] = 0
                sangQ.append((i, j))

    while fireQ:
        x, y = fireQ.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if arr[nx][ny] != "#" and fireVisited[nx][ny] == -1:
                    fireVisited[nx][ny] = fireVisited[x][y] + 1
                    fireQ.append((nx, ny))

    flag = False
    answer = 0

    while sangQ:
        x, y = sangQ.popleft()

        if x == 0 or y == 0 or x == h - 1 or y == w - 1:
            flag = True
            answer = sangVisited[x][y] + 1
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if arr[nx][ny] != "#" and sangVisited[nx][ny] == -1 and (fireVisited[nx][ny] > sangVisited[x][y] + 1 or fireVisited[nx][ny] == -1):

                    sangVisited[nx][ny] = sangVisited[x][y] + 1
                    sangQ.append((nx, ny))


    if flag:
        return answer
    else:
        return 0




while t > 0:
    w, h = map(int, input().split())

    arr = [[] for i in range(h)]

    for i in range(h):
        arr[i] = list(input())

    answer = bfs(arr, h, w)

    if answer == 0:
        print("IMPOSSIBLE")
    else:
        print(answer)

    t = t-1




