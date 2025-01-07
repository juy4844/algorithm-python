n, k = map(int, input().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

dp = [[0 for j in range(n)] for i in range(k + 1)]

for i in range(1, k+1):
    for j in range(n):
        if j == 0:
            if i >= arr[j][0]:
                dp[i][j] = arr[j][1]
        else:
            if i >= arr[j][0]:
                dp[i][j] = max(dp[i][j-1], dp[i-arr[j][0]][j-1] + arr[j][1])
            else:
                dp[i][j] = dp[i][j-1]

print(dp[k][n-1])
