def solution(sequence):
    answer = 0

    dp = [[0 for j in range(2)] for i in range(len(sequence))]

    dp[0][0] = sequence[0]
    dp[0][1] = sequence[0] * -1

    for i in range(1, len(sequence)):
        dp[i][0] = max(dp[i - 1][1] + sequence[i], sequence[i])
        dp[i][1] = max(dp[i - 1][0] - sequence[i], sequence[i] * -1)

    for i in range(len(sequence)):
        answer = max(dp[i][0], answer, dp[i][1])

    return answer