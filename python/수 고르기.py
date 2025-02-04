n, m = map(int, input().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = int(input())

arr.sort()

left = 0
right = 0
ans = float("inf")

while right < n:
    temp = arr[right] - arr[left]
    if ans > temp and m <= temp:
        ans = temp
    if temp == m:
        break
    if temp < m:
        right += 1
    else:
        left += 1

print(ans)