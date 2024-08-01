n = int(input())
arr = [[0 for j in range(3)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

dp = [[0 for j in range(3)] for i in range(n)]

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3] + arr[i][j], dp[i-1][(j+2)%3] + arr[i][j])


print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
