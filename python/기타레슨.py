n, m = map(int, input().split())

arr = list(map(int, input().split()))

left = max(arr)
right = 10 ** 9

while left < right:
    mid = (left + right) // 2

    cnt = 1
    temp = 0

    for i in range(n):
        if temp + arr[i] > mid:
            temp = arr[i]
            cnt += 1
        else:
            temp += arr[i]

    if cnt > m:
        left = mid + 1
    else:
        right = mid

print(right)
