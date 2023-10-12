# 1941 소문난 칠공주 (G3)
# https://www.acmicpc.net/problem/1941
# 정답

import sys
input = sys.stdin.readline

map = [list(input().rstrip()) for _ in range(5)]

result = set()
answer = 0

def dfs(crew, y_cnt):
    global answer
    if tuple(sorted(crew)) in result:
        return

    result.add(tuple(sorted(crew)))
    
    if len(crew) == 7:
        answer += 1
        return

    for x, y in crew:
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + i, y + j

            if nx < 0 or nx > 4 or ny < 0 or ny > 4 or (nx, ny) in crew:
                continue
            
            if map[nx][ny] == 'S':
                dfs(crew | {(nx, ny)}, y_cnt)
                
            elif y_cnt < 3:
                dfs(crew | {(nx, ny)}, y_cnt+1)
                

for r in range(5):
    for c in range(5):
        if map[r][c] == 'S':
            dfs({(r, c)}, 0)

print(answer)