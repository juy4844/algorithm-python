n = int(input())

arr = list(map(int, input().split()))

oper = list(map(int, input().split()))

maxnum = float("-inf")
minnum = float("inf")

def dfs(value, index):
    global maxnum
    global minnum

    if index == n:
        if maxnum < value:
            maxnum = value
        if minnum > value:
            minnum = value
        return

    for i in range(4):
        if oper[i] > 0:
            temp = 0
            if i == 0:
                temp = value + arr[index]
            elif i == 1:
                temp = value - arr[index]
            elif i == 2:
                temp = value * arr[index]
            else:
                if value >= 0:
                    temp = value // arr[index]
                else:
                    temp = ((value * -1) // arr[index]) * -1
            oper[i] -= 1
            dfs(temp, index+1)
            oper[i] += 1

dfs(arr[0], 1)
print(maxnum)
print(minnum)






