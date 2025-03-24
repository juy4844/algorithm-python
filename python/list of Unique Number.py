from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))

dic = defaultdict(int)

left = 0
answer = 1
dic[arr[0]] = 1

for i in range(1, n):
    if dic[arr[i]] == 0:
        dic[arr[i]] = 1
        answer += (i-left+1)
    else:
        for j in range(left, i):
            if arr[j] == arr[i]:
                left = j+1
                break
            else:
                dic[arr[j]] = 0
        answer += (i-left+1)

print(answer)