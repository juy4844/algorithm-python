n = int(input())

arr = list(map(int, input().split()))

m = int(input())

qt = []
for i in range(m):
    qt.append(list(map(int, input().split())))

dp = [[-1 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if j + i < n:
            if i == 0:
                dp[j][j+i] = 1
            elif i == 1:
                if arr[j] == arr[j+i]:
                    dp[j][j+i] = 1
                else:
                    dp[j][j+i] = 0
            else:
                if arr[j] == arr[j + i] and dp[j+1][j+i-1] == 1:
                    dp[j][j + i] = 1
                else:
                    dp[j][j + i] = 0

for i in range(m):
    print(dp[qt[i][0]-1][qt[i][1]-1])