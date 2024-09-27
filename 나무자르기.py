n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)

# start가 end보다 커져야만 종료

while start <= end:  
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += (tree-mid)
    
    if cnt <= m:
        end = mid -1
    else:
        start = mid + 1

print(start)