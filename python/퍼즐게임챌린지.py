def solution(diffs, times, limit):
    answer = 0

    left = 1
    right = 100001

    mid = (left + right) / 2

    while left < right:

        temp = 0
        time_prev = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                temp += times[i]
                time_prev = times[i]
            else:
                temp += ((diffs[i] - mid) * (time_prev + times[i]) + times[i])
                time_prev = ((diffs[i] - mid) * (time_prev + times[i]) + times[i])

        if temp > limit:
            left = mid + 1
        else:
            right = mid

    return right