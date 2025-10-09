# p[I][j] = p[I-1][j] + p[i][j-1]

def solution(m, n, puddles):
    answer = 0

    dp = [[0 for j in range(m)] for i in range(n)]
    dp[0][0] = 1

    puddles = [[q-1, p-1] for [p, q] in puddles]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007
    return dp[n-1][m-1]