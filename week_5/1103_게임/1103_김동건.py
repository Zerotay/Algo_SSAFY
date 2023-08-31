import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]
ans =-1

def dfs(x,y,val):
    if visited[x][y] : return visited[x][y]
    # global ans
    # ans = maxa(ans,val)
    # v[x][y] = 1
    # print(x,y)
    if not adjlist[(x,y)]:
        visited[x][y]=1
        return 1
    tmp = 0
    for nx,ny in adjlist[(x,y)]:
        # if not visited[nx][ny]:
        if v[nx][ny]:
            print(-1)
            exit(0)
        v[nx][ny] = 1
        tmp = max(tmp, dfs(nx,ny,val+1))
        v[nx][ny] = 0
    visited[x][y] = tmp+1
    return visited[x][y]

adjlist = defaultdict(list)
dir = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    for j in range(m):
        if lst[i][j] == 'H': continue
        for k in range(4):
            tmp = int(lst[i][j])
            nx = i + dir[k][0] * tmp
            ny = j + dir[k][1] * tmp
            if -1<nx<n and -1<ny<m and lst[nx][ny] != 'H':
                adjlist[(i,j)].append((nx,ny))

visited = [[0] * m for _ in range(n)]
v = [[0] * m for _ in range(n)]
v[0][0] = 1
dfs(0,0,1)
print(visited[0][0])