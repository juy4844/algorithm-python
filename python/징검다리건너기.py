def solution(stones, k):
    answer = 0

    ans = max(stones[0:k])
    temp = ans

    for i in range(0, len(stones) - k):
        if temp > stones[i] and temp >= stones[i + k]:
            continue
        elif temp >= stones[i] and temp <= stones[i + k]:
            temp = stones[i + k]
        elif temp == stones[i] and temp > stones[i + k]:
            temp = max(stones[i + 1:i + k + 1])
            ans = min(ans, temp)

    return ans