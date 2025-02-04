from collections import deque

n = int(input())

arr = list(map(int, input().split()))

stack = []
ans = [0 for i in range(n)]

for i in range(n):
    if len(stack) == 0:
        stack.append((arr[i], i))
    else:
        while len(stack) != 0:
            if stack[len(stack)-1][0] < arr[i]:
                stack.pop()
            else:
                break
        if len(stack) == 0:
            stack.append((arr[i], i))
        else:
            ans[i] = stack[len(stack) - 1][1] + 1
            stack.append((arr[i], i))


for i in range(n):
    print(ans[i], end=" ")