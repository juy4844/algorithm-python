import heapq
import copy

inp = [0 for i in range(4)]
for i in range(4):
    inp[i] = list(map(int, input().split()))

arr = [[0 for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        arr[i][j] = [inp[i][j*2], inp[i][j*2+1] - 1]


answer = 0

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def move_fish(tmp):
    global dx
    global dy
    heap = []
    for i in range(4):
        for j in range(4):
            if tmp[i][j] != 0 and tmp[i][j] != 17:
                heap.append([tmp[i][j][0], tmp[i][j][1], i, j])
    heap.sort(reverse=True)

    while len(heap) >0:
        num, d, x, y = heap.pop()
        for i in range(8):
            if x+dx[(d+i)%8] < 0 or x+dx[(d+i)%8] >= 4 or y+dy[(d+i)%8] < 0 or y+dy[(d+i)%8] >= 4:
                continue
            if tmp[x+dx[(d+i)%8]][y+dy[(d+i)%8]] == 17:
                continue
            if tmp[x+dx[(d+i)%8]][y+dy[(d+i)%8]] == 0:
                tmp[x + dx[(d + i) % 8]][y + dy[(d + i) % 8]] = [tmp[x][y][0], (d + i) % 8]
                tmp[x][y] = 0
                break
            else:
                for h in range(len(heap)):
                    if heap[h][0] == tmp[x + dx[(d + i) % 8]][y + dy[(d + i) % 8]][0]:
                        heap[h][2] = x
                        heap[h][3] = y
                        break
                temp = [tmp[x][y][0], (d + i) % 8]
                tmp[x][y] = copy.deepcopy(tmp[x + dx[(d + i) % 8]][y + dy[(d + i) % 8]])
                tmp[x + dx[(d + i) % 8]][y + dy[(d + i) % 8]] = temp

                break



def dfs(x, y, d, sea, score):
    global dx
    global dy
    global answer

    # for i in range(4):
    #     print(sea[i])
    # print(score)
    # print()

    nx = x
    ny = y
    check = True
    while True:
        nx = nx + dx[d]
        ny = ny + dy[d]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if sea[nx][ny] != 0:
            check = False

            tmp = [i[:] for i in sea]

            tmp[x][y] = 0
            addScore = tmp[nx][ny][0]
            direction = tmp[nx][ny][1]
            tmp[nx][ny] = 17
            move_fish(tmp)
            dfs(nx, ny, direction, tmp, score + addScore)
    if check == True:
        # print("score : ")
        # print(score)
        if answer <= score:
            answer = score




tscore = arr[0][0][0]
direction = arr[0][0][1]
arr[0][0] = 17
move_fish(arr)
dfs(0,0,direction, arr, tscore)

print(answer)