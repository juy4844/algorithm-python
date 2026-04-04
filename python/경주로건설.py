import heapq


def solution(board):
    n = len(board)
    # dist[r][c][d]: (r, c) 칸에 d 방향으로 도착했을 때의 최소 비용
    # 0:위, 1:오른쪽, 2:아래, 3:왼쪽
    dist = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = []

    # 시작점 (0,0)에서 출발 처리
    # 처음에 오른쪽(1) 혹은 아래쪽(2)으로 바로 갈 수 있으므로 두 경우를 넣어줌
    # (비용, r, c, 방향)
    if board[0][1] == 0:
        heapq.heappush(q, (100, 0, 1, 1))
        dist[0][1][1] = 100
    if board[1][0] == 0:
        heapq.heappush(q, (100, 1, 0, 2))
        dist[1][0][2] = 100

    while q:
        cost, r, c, d = heapq.heappop(q)

        # 이미 기록된 최소 비용보다 크다면 스킵
        if dist[r][c][d] < cost:
            continue

        # 도착점에 도달했다면? (Dijkstra 특성상 처음 도착했을 때가 최솟값 중 하나)
        if r == n - 1 and c == n - 1:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 격자 범위 내이고 벽이 아닌 경우
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                # 같은 방향이면 100원, 다른 방향이면 600원(100+500)
                new_cost = cost + (100 if d == i else 600)

                # 기존에 기록된 해당 칸, 해당 방향의 비용보다 저렴할 때만 갱신
                if new_cost < dist[nr][nc][i]:
                    dist[nr][nc][i] = new_cost
                    heapq.heappush(q, (new_cost, nr, nc, i))

    # 도착점 (n-1, n-1)의 4개 방향 중 최솟값 반환
    return min(dist[n - 1][n - 1])