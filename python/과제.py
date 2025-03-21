import heapq

n = int(input())

arr = [[] for i in range(n)]
visited = [False] * 1001

for i in range(n):
    arr[i] = list(map(int, input().split()))

arr.sort(key= lambda x : (-x[1], x[0]))

answer = 0
for day, worth in arr:
    i = day
    while i > 0 and visited[i]:
        i -= 1
    if i == 0:
        continue
    else:
        visited[i] = True
        answer += worth

print(answer)