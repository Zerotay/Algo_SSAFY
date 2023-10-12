# 1103 게임 (G2)
# https://www.acmicpc.net/problem/1103
# 시간초과

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[c for c in input().rstrip()] for _ in range(n)]
visited = [[False]* m for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

maxCount = 0

def go(i, j, count):
    global arr, visited, maxCount

    if not (0 <= i < n and 0 <= j < m) or arr[i][j] == 'H':
        maxCount = max(maxCount, count)
        return
    
    if visited[i][j]:
        print(-1)
        exit(0)

    visited[i][j] = True
    for d in direction:
        newI = i+(d[0] * int(arr[i][j]))
        newJ = j+(d[1] * int(arr[i][j]))
  
        go(newI, newJ, count+1)

    visited[i][j] = False

go(0, 0, 0)
    
print(maxCount)