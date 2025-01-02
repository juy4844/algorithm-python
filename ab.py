from collections import deque

n, k = map(int, input().split())

a, b = 0, 0

bo = True

if n % 2 == 0:
    a = n//2
    b = n//2
    if k > n//2 * n//2:
        bo = False
        print(-1)
else:
    a = n//2
    b = n//2 + 1
    if k > n//2 * (n//2+1):
        bo = False
        print(-1)
        
line = b
answer = deque()

if bo == True:

    if k > line:
        answer.append("A")
        for i in range(line):
            answer.append("B")
        a -= 1
        k -= line
    else:
        answer.append("A")
        b -= k
        a -= 1
        for i in range(k):
            answer.append("B")
        for i in range(b):
            answer.appendleft("B")
        for i in range(a):
            answer.append("A")
        k = 0
        a = 0

    while k != 0 or a != 0:
        if k > line:
            answer.appendleft("A")
            k -= line
            a -= 1
        elif k < line and k > 0:
            answer.insert(len(answer)-k, "A")
            a -=1
            k = 0
        else:
            for i in range(a):
                answer.append("A")
            a = 0
        
    print("".join(answer))