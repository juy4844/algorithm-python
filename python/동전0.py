n, k = map(int, input().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = int(input())

remain = k
cnt = 0

while True:
    if remain == 0:
        break
    
    bo = False
    for i in range(n):
        if remain < arr[i]:
            tcnt = remain // arr[i-1]
            remain -= arr[i-1] * tcnt
            cnt += tcnt
            bo = True
            break
    
    if bo == False:
        tcnt = remain // arr[n-1]
        remain -= arr[n-1] * tcnt
        cnt += tcnt

print(cnt)