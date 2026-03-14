from collections import defaultdict


def move(prev, next):
    if next[0] > prev[0]:
        return [prev[0] + 1, prev[1]]
    elif next[0] < prev[0]:
        return [prev[0] - 1, prev[1]]
    else:
        if next[1] > prev[1]:
            return [prev[0], prev[1] + 1]
        elif next[1] < prev[1]:
            return [prev[0], prev[1] - 1]
        else:
            return next


def solution(points, routes):
    answer = 0

    x = len(routes)
    endCheckPoint = len(routes[0])

    rootMap = []
    rPoints = []
    for i, j in points:
        rPoints.append([i - 1, j - 1])

    for i in range(x):
        for j in range(endCheckPoint):
            routes[i][j] -= 1

    rootMap = []
    for i in range(x):
        rootMap.append(rPoints[routes[i][0]])

    check = [1 for i in range(x)]

    temp_init = defaultdict(int)
    for i in range(x):
        pos = (rootMap[i][0], rootMap[i][1])
        temp_init[pos] += 1
        if temp_init[pos] == 2:
            answer += 1

    flag = True

    while flag:
        # 4. 2차원 배열 대신 Dictionary 사용 (시간 초과 방지)
        temp = defaultdict(int)
        flag = False  # 루프 시작 시 False로 두고, 움직인 로봇이 있으면 True로 변경

        for i in range(x):
            if check[i] < endCheckPoint:
                target_point = rPoints[routes[i][check[i]]]

                # 로봇 이동
                rootMap[i] = move(rootMap[i], target_point)

                # 현재 좌표 충돌 체크
                pos = (rootMap[i][0], rootMap[i][1])
                temp[pos] += 1
                if temp[pos] == 2:
                    answer += 1

                # 목적지에 도착했다면 다음 목적지를 바라보도록 업데이트
                if rootMap[i] == target_point:
                    check[i] += 1

        # 하나라도 아직 운송 중인 로봇이 있는지 확인
        for i in range(x):
            if check[i] < endCheckPoint:
                flag = True
                break

    return answer