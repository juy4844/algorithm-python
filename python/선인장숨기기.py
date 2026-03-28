from collections import deque

# 50만?
# 일단 drops를 전부 다 찍어놔 시간 순서대로
# 그 다음 가로 세로로 돌면서 구역안에 들어올때의 최소값을 찍는다.
# 가로로 돌때 가로하나 열하나 고정 시키고 n만큼 도는데
#
# 마지막으로 전체를 돌면서 최대값을 찾으면 된다.

def solution(m, n, h, w, drops):
    answer = []

    lenD = len(drops)

    arr = [[lenD + 1 for j in range(n)] for i in range(m)]

    # 일단 drops를 전부 다 찍어놔 시간 순서대로
    for i in range(lenD):
        r = drops[i][0]
        c = drops[i][1]

        arr[r][c] = i

    t = [[0 for j in range(n-w+1)] for i in range(m)]

    for i in range(m):
        q = deque()
        for j in range(n):
            while q and arr[i][q[-1]] > arr[i][j]:
                q.pop()
            q.append(j)

            if q[0] <= j - w:
                q.popleft()

            if j >= w - 1:
                t[i][j - w + 1] = arr[i][q[0]]

    u = [[0 for j in range(n-w+1)] for i in range(m-h+1)]

    for i in range(n-w+1):
        q = deque()
        for j in range(m):
            while q and t[q[-1]][i] > t[j][i]:
                q.pop()
            q.append(j)

            if q[0] <= j - h:
                q.popleft()

            if j >= h - 1:
                u[j - h + 1][i] = t[q[0]][i]

    maxV = -1
    ai = -1
    aj = -1

    for i in range(m-h+1):
        for j in range(n-w+1):
            if u[i][j] > maxV:
                maxV = u[i][j]
                ai = i
                aj = j


    return [ai, aj]