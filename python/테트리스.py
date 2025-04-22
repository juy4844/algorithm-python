
tetrist = [[[0,0], [0,1], [0,2], [0,3]],
           [[0,0], [1,0], [2,0], [3,0]],
           [[0,0],[0,1],[1,1],[1,2]],
           [[0,1],[1,0],[1,1],[2,0]],
        [[0,0],[0,1],[0,2],[1,2]],
        [[0,0],[0,1],[1,0],[2,0]],
        [[0,0],[1,0],[1,1],[1,2]],
        [[0,1],[1,1],[2,1],[2,0]],
        [[0,0],[0,1],[1,0],[1,1]],
        [[0,0],[1,0],[1,1],[2,0]],
        [[0,1],[1,0],[1,1],[2,1]],
        [[0,1],[1,0],[1,1],[1,2]],
        [[0,0],[0,1],[0,2],[1,1]]]

test = 1

while True:
    n = int(input())
    if n == 0:
        break

    ans = float("-inf")

    arr = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        arr[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            for t in tetrist:
                sum = 0
                flag = True
                for dx, dy in t:
                    nx = i + dx
                    ny = j + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        sum += arr[nx][ny]
                    else:
                        flag = False

                if flag:
                    if ans < sum:
                        ans = sum

    print("%d. %d" % (test, ans))
    test += 1