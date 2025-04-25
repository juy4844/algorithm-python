import heapq


def solution(jobs):
    answer = 0

    jobs.sort()

    q = []
    work = [0, 0]

    i = 0

    while i < len(jobs):

        if len(q) == 0:
            work[0] = jobs[i][0]
            work[1] = jobs[i][0] + jobs[i][1]
            answer += (jobs[i][1] - jobs[i][0])
            print(answer)

        while i < len(jobs):
            if work[1] >= jobs[i][0]:
                heapq.heappush(q, (jobs[i][1], jobs[i][0], i))
                i = i + 1
            else:
                break

        x, y, z = heapq.heappop(q)
        if y > work[1]:
            work[0] = y
            work[1] = y + x
            answer += (y - x)
            print(answer)
        else:
            work[0] = work[1]
            work[1] = work[1] + x
            answer += (work[1] - y)
            print(answer)

    while q:

        x, y, z = heapq.heappop(q)

        if y > work[1]:
            work[0] = y
            work[1] = y + x
            answer += (y - x)
            print(answer)
        else:
            work[0] = work[1]
            work[1] = work[1] + x
            answer += (work[1] - y)
            print(answer)

    return answer // len(jobs)