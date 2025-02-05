def dfs(x, y):
    global r
    global c
    if y == c-1:
        return True

    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if arr[nx][ny] == '.' and check[nx][ny] == False:
                check[nx][ny] = True
                if dfs(nx, ny):
                    return True

    return False

r, c = map(int, input().split())

arr = [[] for i in range(r)]

for i in range(r):
    arr[i] = list(input())

check = [[False for j in range(c)] for i in range(r)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

ans = 0

for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)








