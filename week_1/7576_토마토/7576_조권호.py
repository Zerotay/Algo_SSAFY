import collections

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def spread(tomatoes, q):
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx<0 or nx>=n)  or (ny<0 or ny>=m):
                continue
            if tomatoes[nx][ny] not in [1,-1]:
                if tomatoes[nx][ny]==0:
                    tomatoes[nx][ny] =tomatoes[x][y]+1
                    q.append((nx,ny))

q = collections.deque()
m,n = map(int,input().split())
tomatoes =[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if(tomatoes[i][j]==1):
            q.append((i,j))
spread(tomatoes, q)
cnt =0
for i in range(n):
    for j in range(m):
        if tomatoes[i][j]==0:
            print(-1)
            exit(0)
        cnt= max(tomatoes[i][j],cnt)
print(cnt-1)