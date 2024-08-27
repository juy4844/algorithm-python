n = int(input())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())

stack = [(arr[n-1], n-1)]
result = 0

for i in range(n-2, -1, -1):
    if not stack:
        result += (n-1 -i)
    elif arr[i] <= stack[-1][0]:
        result += (stack[-1][1] - i - 1)
        stack.append((arr[i], i))
    else:
        bo = True
        while arr[i] > stack[-1][0]:
            stack.pop()
            if not stack:
                result += (n-1 -i)
                bo = False
                break
        if bo:
            result += (stack[-1][1] - i - 1)
        stack.append((arr[i], i))
    print(result)

print(result)