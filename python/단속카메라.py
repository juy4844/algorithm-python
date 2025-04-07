def solution(routes):
    answer = 0

    routes.sort()

    left = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] <= left:
            left = min(left, routes[i][1])
        else:
            left = routes[i][1]
            answer += 1

    answer += 1
    return answer