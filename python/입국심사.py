def solution(n, times):
    answer = 0

    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2

        temp = 0

        for t in times:
            temp += (mid // t)

        if temp < n:
            left = mid + 1
        else:
            right = mid

    answer = right

    return answer