n = int(input())

arr = []
answer = []

for i in range(n):
    arr.append(list(input().split()))

arr.sort(key=lambda x : int(x[4]))

for i in range(n):
    if arr[i][1] == "jaehak" and arr[i][2] == "notyet" and (int(arr[i][3]) > 3 or int(arr[i][3]) == -1):
        if len(answer) < 10:
            answer.append(arr[i][0])

answer.sort()
print(len(answer))

for i in range(len(answer)):
    print(answer[i])

