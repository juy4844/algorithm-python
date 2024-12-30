n, m, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

shark = [0 for i in range(m+1)]
sharkNDir = list(map(int, input().split()))

sharkDir = [[] for i in range(m+1)]
for i in range(1, m+1):
    for j in range(4):
        sharkDir[i].append(list(map(int, input().split())))
        for l in range(4):
            sharkDir[i][j][l] -= 1

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            index = arr[i][j]
            shark[index] = [index, i, j, sharkNDir[index-1] - 1, 1]

smell = [[0 for j in range(n)] for i in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

while True:
    if ans > 999:
        break
    ans += 1
    for i in range(1, len(shark)):

        num = shark[i][0]
        r = shark[i][1]
        c = shark[i][2]
        d = shark[i][3]
        live = shark[i][4]
        if live == 0:
            break
        nd = d
        nr = r
        nc = c
        flag = False
        for j in range(4):
            nd = sharkDir[num][d][j]
            nr = r + dx[nd]
            nc = c + dy[nd]
            if 0 <= nr < n and 0 <= nc < n:
                if isinstance(smell[nr][nc], list):
                    continue
                if arr[nr][nc] == 0:
                    flag = True
                    arr[nr][nc] = num
                    arr[r][c] = 0
                    smell[r][c] = [num, k]
                    shark[num] = [num, nr, nc, nd, 1]
                    break
                elif 0 < arr[nr][nc] <= m:
                    flag = True
                    arr[r][c] = 0
                    smell[r][c] = [num, k]
                    shark[num][4] = 0
                    break
        if flag == False:
            for j in range(4):
                nd = sharkDir[num][d][j]
                nr = r + dx[nd]
                nc = c + dy[nd]
                if 0 <= nr < n and 0 <= nc < n:
                    if smell[nr][nc][0] == num:
                        arr[nr][nc] = num
                        arr[r][c] = 0
                        smell[r][c] = [num, k]
                        shark[num] = [num, nr, nc, nd, 1]
                        break

    cnt = 0
    for x in range(n):
        for y in range(n):
            if isinstance(smell[x][y], list):
                if smell[x][y][1] == 1:
                    smell[x][y] = 0
                else:
                    smell[x][y][1] -= 1
            if 0 < arr[x][y] <= m:
                cnt += 1

    if cnt == 1:
        break
if ans > 999:
    print(-1)
else:
    print(ans)


