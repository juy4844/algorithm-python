def solution(grid):
    R = len(grid)
    C = len(grid[0])

    # 방향: 0(위), 1(오른쪽), 2(아래), 3(왼쪽) - 시계 방향으로 설정
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 방문 여부를 체크할 3차원 배열 (행, 열, 방향)
    # R x C 격자에서 4개의 방향을 모두 False로 초기화
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]

    answer = []

    # 모든 칸(r, c)과 모든 방향(d)에 대해 탐색
    for r in range(R):
        for c in range(C):
            for d in range(4):
                # 이미 사이클에 포함되어 방문했던 경로라면 패스
                if not visited[r][c][d]:
                    cycle_length = 0
                    cr, cc, cd = r, c, d

                    # 방문했던 곳을 다시 만날 때까지(사이클이 완성될 때까지) 반복
                    while not visited[cr][cc][cd]:
                        # 현재 상태 방문 처리 및 사이클 길이 1 증가
                        visited[cr][cc][cd] = True
                        cycle_length += 1

                        # 1. 현재 칸의 문자에 따라 다음 이동 방향 결정
                        if grid[cr][cc] == 'L':
                            cd = (cd - 1) % 4  # 반시계 방향
                        elif grid[cr][cc] == 'R':
                            cd = (cd + 1) % 4  # 시계 방향

                        # (문자가 'S'인 경우는 방향 cd가 그대로 유지됨)

                        # 2. 다음 칸으로 이동 (격자를 벗어나면 반대쪽으로 넘어오도록 모듈러 연산)
                        cr = (cr + dr[cd]) % R
                        cc = (cc + dc[cd]) % C

                    # 하나의 온전한 사이클 탐색이 끝났으므로 정답 배열에 추가
                    answer.append(cycle_length)

    # 결과를 오름차순으로 정렬하여 반환
    answer.sort()
    return answer