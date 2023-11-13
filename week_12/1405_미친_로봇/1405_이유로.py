# 1405 미친 로봇 (G4)
# https://www.acmicpc.net/problem/1405
# 정답

import sys

input = sys.stdin.readline

N, e, w, s, n = map(int,input().split())
result = 0
directionPercent = [e/100, w/100, s/100, n/100]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

visited = [[False] * (2*(N+1)) for _ in range(2*(N+1))]

def dfs(count, i, j, percent):
  global result
  if (count == N):
    result += percent
    return

  for d in range(len(direction)):
    if directionPercent[d] > 0:
      newI = i + direction[d][0]
      newJ = j + direction[d][1]
      
      if not visited[newI][newJ]:
        visited[newI][newJ] = True
        dfs(count+1, newI, newJ, percent * directionPercent[d])
        visited[newI][newJ] = False

visited[N][N] = True  
dfs(0, N, N, 1)


print(result)
  
  
  
