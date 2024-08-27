t = int(input())

dp = [[0 for j in range(2)] for i in range(10001)]
dp[1][0] = 0
dp[1][1] = 0
dp[2][0] = 1
dp[2][1] = 0
dp[3][0] = 1
dp[3][1] = 1

for i in range(4, 10001):
    dp[i][0] = dp[i-2][0] + 1
    dp[i][1] = dp[i-3][0] + dp[i-3][1] + 1

for i in range(t):
    n = int(input())
    print(dp[n][1] + dp[n][0] + 1)

    