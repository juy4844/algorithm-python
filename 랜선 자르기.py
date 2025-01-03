k, n = map(int, input().split())

arr = []

for i in range(k):
    arr.append(int(input()))

maxv = max(arr) + 1
minv = 1

while minv < maxv:
    mid = (maxv + minv) // 2
    cnt = 0

    for i in range(k):
        cnt += (arr[i] // mid)

    if cnt >= n:
        minv = mid + 1
    else:
        maxv = mid
    
print(maxv - 1)