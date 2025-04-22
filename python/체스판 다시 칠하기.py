n, m = map(int, input().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = list(input())

ans = float("inf")

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for a in range(8):
            for b in range(8):
                x = i+a
                y = j+b
                if (a + b) % 2 == 0 and arr[x][y] == "W":
                    black += 1
                elif (a + b) % 2 == 1 and arr[x][y] == "W":
                    white += 1
                elif (a + b) % 2 == 0 and arr[x][y] == "B":
                    white += 1
                elif (a + b) % 2 == 1 and arr[x][y] == "B":
                    black += 1

        ans = min(ans, white, black)

print(ans)