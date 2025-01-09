n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
answer = [0 for i in range(n)]

check = [False for i in range(n)]

def dfs(n, m, index):
    if index == m:
        for i in range(m):
            print(answer[i], end=" ")
        print()
        return

    xx = -1

    for i in range(n):
        if check[i] == False and xx != arr[i]:
            check[i] = True
            xx = arr[i]
            answer[index] = arr[i]
            dfs(n, m, index+1)
            check[i] = False

dfs(n,m,0)