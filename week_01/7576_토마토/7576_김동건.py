import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(m)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

que = deque([(i,j) for i in range(m) for j in filter(lambda x: inlst[i][x]==1,range(n))])

while que:
    x,y= que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<m and -1<ny<n and not inlst[nx][ny]:
            inlst[nx][ny] = inlst[x][y]+1
            que.append((nx,ny))

print(max(max(i) for i in inlst)-1 if all(all(i) for i in inlst) else -1)
