from collections import deque
from collections import defaultdict

t = int(input())

for i in range(t):
    w = input()
    k = int(input())
    numMax = -1
    numMin = 10001
    di = defaultdict(deque)
    for j in range(len(w)):
        if len(di[w[j]]) < k-1:
            di[w[j]].append(j)
        elif len(di[w[j]]) == k-1:
            di[w[j]].append(j)
            numMax = max(numMax, j - di[w[j]][0] + 1)
            numMin = min(numMin, j - di[w[j]][0] + 1)
        else:
            di[w[j]].popleft()
            di[w[j]].append(j)
            numMax = max(numMax, j - di[w[j]][0] + 1)
            numMin = min(numMin, j - di[w[j]][0] + 1)

    if numMax == -1:
        print(-1)
    else:
        print(numMin, end=" ")
        print(numMax)

