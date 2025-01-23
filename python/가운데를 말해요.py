import heapq

n = int(input())

leftHeap = []
rightHeap = []

answer = []

for i in range(n):
    num = int(input())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, num * -1)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and leftHeap[0] * -1 > rightHeap[0]:
        left = heapq.heappop(leftHeap) * -1
        right = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, right * -1)
        heapq.heappush(rightHeap, left)

    answer.append(leftHeap[0] * -1)

for i in answer:
    print(i)