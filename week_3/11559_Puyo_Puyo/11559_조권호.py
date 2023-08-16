import sys
import collections
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

puyo = []
for _ in range(12):
    puyo.append(list(input()))

def bfs(x,y):
    q = collections.deque()
    q.append((x,y))
    tmp.append((x,y))
    while q:
        n,m = q.popleft()
        for i in range(4):
            nx = n+dx[i]
            ny = m+dy[i]
            if nx<0 or ny<0 or nx>=12 or ny>=6:
                continue
            # print(nx, ny)
            if puyo[nx][ny] ==puyo[x][y] and not visited[nx][ny]:
                q.append((nx,ny))
                tmp.append((nx,ny))
                visited[nx][ny] = True;

def remove_puyo(tmp):
    for t in tmp:
        puyo[t[0]][t[1]] = '.'

def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if puyo[j][i]!='.' and puyo[k][i]=='.':
                    puyo[k][i]=puyo[j][i]
                    puyo[j][i]='.'
                    # print(puyo)
                    break

ans =0
while True:
    flag = True
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if puyo[i][j] !='.' and visited[i][j] == False:
                visited[i][j] = True
                tmp = []
                bfs(i,j)
                if(len(tmp)>=4):
                    flag = False
                    remove_puyo(tmp)
    if flag:
       break
    ans +=1                                 
    down()

print(ans)