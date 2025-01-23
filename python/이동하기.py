n,m = map(int, input().split())

arr = [0 for i in range(n)]
d = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

d[0][0] = arr[0][0]


for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            d[i][j] = max(d[i][j-1], d[i-1][j], d[i-1][j-1]) + arr[i][j]
        elif i > 0:
            d[i][j] = d[i - 1][j] + arr[i][j]
        elif j > 0:
            d[i][j] = d[i][j - 1] + arr[i][j]
        else:
            d[i][j] = arr[i][j]

print(d[n-1][m-1])
