n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees) + 1

while start < end:  
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += (tree-mid)
    
    if cnt >= m:
        start = mid + 1
    else:
        end = mid

print(end-1)