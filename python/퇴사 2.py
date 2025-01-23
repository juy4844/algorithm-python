n = int(input())

arr = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    arr[i] = list(map(int, input().split()))

dp = [0 for i in range(n + 1)]

for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[i])
    if arr[i][0] + i -1 <= n:
        dp[arr[i][0] + i - 1] = max(dp[arr[i][0] + i -1], dp[i-1] + arr[i][1])

print(max(dp))
