n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def dfs(x, y, d1, d2):
    check = [0] * 5
    tmp = [[0 for j in range(n)] for i in range(n)]
    for i in range(0, d1+1):
        tmp[x+i][y-i] = 5
        tmp[x + d2 + i][y + d2 - i] =5
    for i in range(0, d2+1):
        tmp[x+i][y+i] = 5
        tmp[x + d1 + i][y - d1 + i] =5
    for i in range(x+1, x+d1+d2):
        flag = False
        for j in range(n):
            if tmp[i][j] == 5:
                flag = not flag
            if flag:
                tmp[i][j] = 5

    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 5:
                check[4] += arr[i][j]
            elif 0 <= i and i < x + d1 and 0 <= j and j <= y:
                check[0] += arr[i][j]
            elif 0 <= i and i <= x + d2 and y < j and j < n:
                check[1] += arr[i][j]
            elif x + d1 <= i and i < n and 0 <= j and j < y - d1 + d2:
                check[2] += arr[i][j]
            elif x + d2 < i and i < n and y-d1+d2 <= j and j < n:
                check[3] += arr[i][j]


    return max(check) - min(check)

ans = float("inf")

for d1 in range(n):
    for d2 in range(1, n):
        for x in range(n-d1-d2):
            for y in range(d1, n-d2):
                temp = dfs(x, y, d1, d2)
                if ans > temp:
                    ans = temp


print(ans)

