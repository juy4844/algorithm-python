n, k = map(int, input().split())

arr = [0 for i in range(n)]
dp = [100000 for i in range(k+1)]
dp[0] = 0

for i in range(n):
    arr[i] = int(input())

for i in range(1, k+1):
    for j in range(n):
        if i - arr[j] >= 0:
            dp[i] = min(dp[i], dp[i-arr[j]] + 1)


if dp[k] == 100000:
    print(-1)
else:
    print(dp[k])