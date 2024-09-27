n, k = map(int, input().split())

chess = []
for i in range(n):
    chess.append(list(map(int, input().split())))

location = []
for i in range(k):
    location.append(list(map(int, input().split())))
    location[i][0] -= 1
    location[i][1] -= 1

chessPiece = [[[] for j in range(n)] for i in range(n)]
for i in range(k):
    chessPiece[location[i][0]][location[i][1]].append(i)

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

ans = 0

while True:
    ans += 1
    if ans >= 1000:
        ans = -1
        break
    flag = False
    for i in range(k):
        r = location[i][0]
        c = location[i][1]
        d = location[i][2]
        start = 0
        for j in range(len(chessPiece[r][c])):
            if chessPiece[r][c][j] == i:
                start = j
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            # 다음이 흰색
            if chess[nx][ny] == 0:
                for a in range(start, len(chessPiece[r][c])):
                    move = chessPiece[r][c][a]
                    location[move][0] = nx
                    location[move][1] = ny
                    chessPiece[nx][ny].append(move)
                for a in range(start, len(chessPiece[r][c])):
                    chessPiece[r][c].pop()
                if len(chessPiece[nx][ny]) >= 4:
                    flag = True
                    break
            elif chess[nx][ny] == 1:
                for a in range(len(chessPiece[r][c]) - 1, start - 1, -1):
                    move = chessPiece[r][c][a]
                    location[move][0] = nx
                    location[move][1] = ny
                    chessPiece[nx][ny].append(move)
                for a in range(len(chessPiece[r][c]) - 1, start - 1, -1):
                    chessPiece[r][c].pop()
                if len(chessPiece[nx][ny]) >= 4:
                    flag = True
                    break
            else:
                # 방향 바꾸기
                if d == 1:
                    location[i][2] = 2
                elif d == 2:
                    location[i][2] = 1
                elif d == 3:
                    location[i][2] = 4
                elif d == 4:
                    location[i][2] = 3
                nx = r+dx[location[i][2]]
                ny = c+dy[location[i][2]]
                # again
                if 0 <= nx < n and 0 <= ny < n:
                    # 다음이 흰색
                    if chess[nx][ny] == 0:
                        for a in range(start, len(chessPiece[r][c])):
                            move = chessPiece[r][c][a]
                            location[move][0] = nx
                            location[move][1] = ny
                            chessPiece[nx][ny].append(move)
                        for a in range(start, len(chessPiece[r][c])):
                            chessPiece[r][c].pop()
                    elif chess[nx][ny] == 1:
                        for a in range(len(chessPiece[r][c]) - 1, start - 1, -1):
                            move = chessPiece[r][c][a]
                            location[move][0] = nx
                            location[move][1] = ny
                            chessPiece[nx][ny].append(move)
                        for a in range(len(chessPiece[r][c]) - 1, start - 1, -1):
                            chessPiece[r][c].pop()
                    if len(chessPiece[nx][ny]) >= 4:
                        flag = True
                        break


        else:
            if d == 1:
                location[i][2] = 2
            elif d == 2:
                location[i][2] = 1
            elif d == 3:
                location[i][2] = 4
            elif d == 4:
                location[i][2] = 3
            nx = r + dx[location[i][2]]
            ny = c + dy[location[i][2]]
            # again
            if 0 <= nx < n and 0 <= ny < n:
                # 다음이 흰색
                if chess[nx][ny] == 0:
                    for a in range(start, len(chessPiece[r][c])):
                        move = chessPiece[r][c][a]
                        location[move][0] = nx
                        location[move][1] = ny
                        chessPiece[nx][ny].append(move)
                    for a in range(start, len(chessPiece[r][c])):
                        chessPiece[r][c].pop()
                elif chess[nx][ny] == 1:
                    for a in range(len(chessPiece[r][c]) - 1, start - 1, -1):
                        move = chessPiece[r][c][a]
                        location[move][0] = nx
                        location[move][1] = ny
                        chessPiece[nx][ny].append(move)
                    for a in range(len(chessPiece[r][c]) - 1, start - 1, -1):
                        chessPiece[r][c].pop()

                if len(chessPiece[nx][ny]) >= 4:
                    flag = True
                    break



    if flag == True:
        break

print(ans)