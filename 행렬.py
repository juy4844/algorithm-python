n,m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(input()))

for i in range(n):
    b.append(list(input()))

cnt = 0

b = True

if n < 3 or m < 3:
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                b = False
                break
    if b == False:
        print(-1)
    else:
        print(0)
    exit()

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:

            cnt += 1
            for k in range(3):
                for l in range(3):
                    if a[i+k][j+l] == '0':
                        a[i+k][j+l] = '1'
                    else:
                        a[i+k][j+l] = '0'

bo = True

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            bo = False
            break

if bo == False:
    print(-1)
else:
    print(cnt)