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
    map.append(line)

queue = deque([start])
keys = []
count = 0

while(len(queue) > 0):
    print(queue)
    cur = queue.popleft()
    # map[cur[0]][cur[1]] = 'X'
    count += 1

    for d in direction:
        moved = [cur[0] + d[0], cur[1] + d[1]]
        if not (moved[0] >= 0 and moved[1] >= 0 and moved[0] < N and moved[1] < M):
            continue

        if (map[moved[0]][moved[1]] == '1'):
            print(count)
            exit(1)
        elif (map[moved[0]][moved[1]] == '.' and visited[moved[0]][moved[1]] == False):
            visited[moved[0]][moved[1]] = True
            queue.append(moved)
        elif (map[moved[0]][moved[1]] in ['a', 'b', 'c','d', 'e', 'f'] and visited[moved[0]][moved[1]] == False):
            queue.append(moved)
            keys.append(map[moved[0]][moved[1]])
            visited = [[False]*M for _ in range(N)]
        elif (map[moved[0]][moved[1]] in ['A', 'B', 'C','D', 'E', 'F'] and visited[moved[0]][moved[1]] == False):
            if map[moved[0]][moved[1]].lower() in keys:
                queue.append(moved)
                visited[moved[0]][moved[1]] = True

print(count+1)

# 빈 칸: 언제나 이동할 수 있다. ('.')
# 벽: 절대 이동할 수 없다. ('#')
# 열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
# 문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
# 민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
# 출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')