n, s = map(int, input().split())
arr = list(map(int, input().split()))
sumArr = [0 for i in range(n)]
sumArr[0] = arr[0]

for i in range(1, n):
    sumArr[i] = sumArr[i-1] + arr[i]

left = -1
right = 0
ans = float("inf")

while right < n:
    if left == -1:
        temp = sumArr[right]
        if temp >= s and ans > right+1:
            ans = right + 1
    else:
        temp = sumArr[right] - sumArr[left]
        if temp >= s and ans > right - left:
            ans = right - left
    if temp <= s:
        right += 1
    else:
        left += 1

if ans == float("inf"):
    print(0)
else:
    print(ans)