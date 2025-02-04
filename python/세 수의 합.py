n = int(input())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())

arr.sort()
s = set()
for i in arr:
    for j in arr:
        s.add(i+j)

for i in range(n-1, -1, -1):
    for j in range(i+1):
        if arr[i] - arr[j] in s:
            print(arr[i])
            exit()