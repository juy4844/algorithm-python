n = int(input())

arr = list(map(int, input().split()))

dp = [float("inf") for i in range(n)]
dp [0] = 0

for i in range(n):
    for j in range(1, arr[i] + 1):
        if i + j < n:
            dp[j + i] = min(dp[j+i], dp[i] + 1)

if dp[n-1] != float("inf"):
    print(dp[n-1])
else:
    print(-1)

