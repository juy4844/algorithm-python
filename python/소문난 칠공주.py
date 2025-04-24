from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

map_list = [input().strip() for _ in range(5)]
answer = 0

for num_list in combinations(range(25), 7) :
  visited = [[False]*5 for _ in range(5)]
  x, y = num_list[0] % 5, num_list[0] // 5
  visited[y][x] = True

  tot_cnt = 0
  s_cnt = 0
  q = deque([(x, y)])

  while q :
    x, y = q.popleft()
    tot_cnt += 1
    if map_list[y][x] == 'S' :
      s_cnt += 1
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < 5 and -1 < ay < 5 and (ax + ay * 5) in num_list and not visited[ay][ax]:
        visited[ay][ax] = True
        q.append((ax, ay))
  if tot_cnt == 7 and s_cnt > 3 :
    answer += 1

print(answer)