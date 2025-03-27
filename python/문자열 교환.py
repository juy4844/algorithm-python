arr = list(input())

aNum = 0

for n in arr:
    if n == 'a':
        aNum += 1

temp = 0

for i in range(aNum):
    if arr[i] == 'a':
        temp += 1

ans = aNum - temp

for i in range(aNum, len(arr) + aNum):
    if arr[i % len(arr)] == 'a':
        temp += 1
    if arr[i-aNum] == 'a':
        temp -= 1

    ans = min(ans, aNum - temp)

print(ans)