import heapq
from collections import deque

n = int(input())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

arr.sort(key=lambda x: (-x[1], -x[0]))
arr = deque(arr)
hq = []

result = 0

for i in range(10000, 0, -1):
    while arr:
        p, d = arr[0]
        if d >= i:
            heapq.heappush(hq, -p)
            arr.popleft()
        else:
            break

    if hq:
        result += -heapq.heappop(hq)
    
print(result)

        


