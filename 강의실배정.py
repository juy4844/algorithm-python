import heapq

n = int(input())
arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))



arr.sort(key=lambda x : (x[0], x[1]))
heap = [arr[0][1]]

for i in range(1, n):
    if heap[0] <= arr[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, arr[i][1])

print(len(heap))