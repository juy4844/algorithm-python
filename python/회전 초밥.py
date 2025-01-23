
n, d, k, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

ans = 0

for i in range(n):
    s = set()
    for j in range(i, i+k):
        s.add(arr[j%n])
    s.add(c)

    temp = len(s)
    if ans < temp:
        ans = temp
    
print(ans)