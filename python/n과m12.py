n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answer = [0 for i in range(m)]

def dfs(index, start):
    if index == m:
        for i in range(m):
            print(answer[i], end=" ")
        print()
        return

    for i in range(start, n):
        if i != 0 and arr[i-1] == arr[i]:
            continue
        answer[index] = arr[i]
        dfs(index+1, i)


dfs(0,0)