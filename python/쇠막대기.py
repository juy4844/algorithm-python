arr = list(input())

stack = []
ans = 0

flag = False

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
        flag = True
    else:
        if flag:
            stack.pop()
            ans += len(stack)
            flag = False
        else:
            stack.pop()
            ans += 1

print(ans)