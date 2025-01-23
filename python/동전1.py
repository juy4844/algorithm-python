n, k = map(int, input().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = int(input())

arr.sort()

dp = [0 for i in range(k+1)]

for i in range(n):
    if arr[i] > k:
        continue
    dp[arr[i]] += 1
    for j in range(1, k+1):
        if j - arr[i] >= 1:
            dp[j] = dp[j] + dp[j - arr[i]]


print(dp[k])
