# 1194 달이 차오른다, 가자. (G1)
# https://www.acmicpc.net/problem/1194
# 

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

map = []
visited = [[False]*M for _ in range(N)]
start = [0, 0]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(N):
    line = input()
    if line.find("0") != -1:
        start[0] = i
        start[1] = line.find("0")
    map.append(line.split())

queue = deque([[*start, 0]])
keys = []
count = 0

while(len(queue) > 0):
    print(queue)
    cur = queue.popleft()
    if (map[cur[0]][cur[1]] == '1'):
        print(cur[2])
        exit(1)
    # map[cur[0]][cur[1]] = 'X'
    
    for d in direction:
        moved = [cur[0] + d[0], cur[1] + d[1]]
        if not (moved[0] >= 0 and moved[1] >= 0 and moved[0] < N and moved[1] < M):
            continue

        if (map[moved[0]][moved[1]] == '1'):
            visited[moved[0]][moved[1]] = True
            queue.append([*moved, cur[2]+1])
        elif (map[moved[0]][moved[1]] == '.' and visited[moved[0]][moved[1]] == False):
            visited[moved[0]][moved[1]] = True
            queue.append([*moved, cur[2]+1])
        elif (map[moved[0]][moved[1]] in ['a', 'b', 'c','d', 'e', 'f'] and visited[moved[0]][moved[1]] == False):
            queue.append([*moved, cur[2]+1])
            keys.append(map[moved[0]][moved[1]])
            visited = [[False]*M for _ in range(N)]
            visited[moved[0]][moved[1]] = True
            map[moved[0]][moved[1]] = '.'
        elif (map[moved[0]][moved[1]] in ['A', 'B', 'C','D', 'E', 'F'] and visited[moved[0]][moved[1]] == False):
            if map[moved[0]][moved[1]].lower() in keys:
                queue.append([*moved, cur[2]+1])
                visited[moved[0]][moved[1]] = True

print(-1)
