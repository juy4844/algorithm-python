# 우선 석유를 bfs로 찾아놔 번호메겨서
# 그리고 각 번호마다 크기가 몇인지 매핑해둬
# 그리고 m만큼 돌려서 몇번이 있는지 확인해

from collections import deque
from collections import defaultdict


def solution(land):
    answer = 0

    n = len(land)
    m = len(land[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    landMap = [[0 for j in range(m)] for i in range(n)]
    size = defaultdict(int)

    idx = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and landMap[i][j] == 0:
                q = deque()
                q.append((i, j))
                landMap[i][j] = idx
                cnt += 1

                while q:
                    r, c = q.popleft()

                    for d in range(4):
                        nr = r + dx[d]
                        nc = c + dy[d]

                        if nr >= 0 and nr < n and nc >= 0 and nc < m:
                            if land[nr][nc] == 1 and landMap[nr][nc] == 0:
                                q.append((nr, nc))
                                landMap[nr][nc] = idx
                                cnt += 1
                size[idx] = cnt
                idx += 1
                cnt = 0

    size[0] = 0
    for i in range(m):
        a = set()
        for j in range(n):
            a.add(landMap[j][i])
        temp = 0
        for j in a:
            temp += size[j]
        if answer < temp:
            answer = temp

    return answer




