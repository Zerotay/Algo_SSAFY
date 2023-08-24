import collections
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def rotate(x,y, size):
    global board
    tmp = [[-1]*(1<<n) for _ in range(1<<n)]
    for xx in range(size):
        for yy in range(size):
            tmp[x+yy][y+size-xx-1] = board[x+xx][y+yy]
    for i in range(size):
        for j in range(size):
            board[x+i][y+j] = tmp[x+i][y+j]


def reduce():
    global board
    tmp=[]
    for i in range(1<<n):
        for j in range(1<<n):
            cnt =0
            if(board[i][j]==0):
                continue
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if(nx<0 or ny<0 or nx>=(1<<n) or ny >=(1<<n)):
                    continue
                if(board[nx][ny]>0):
                    cnt+=1
            # print(cnt)
            if(cnt<3):
                tmp.append((i,j))
                # print(i, j)
    for t in tmp:
        board[t[0]][t[1]]-=1


def bfs(x,y):
    global visited, big
    q = collections.deque()
    visited[x][y] = True
    q.append((x,y))
    tmp = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx<0 or ny<0 or nx>=(1<<n) or ny >=(1<<n) or visited[nx][ny] or board[nx][ny]==0):
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
            tmp+=1
    big = max(big, tmp)


n ,q = map(int,input().split())
board=[]
for _ in range(1<<n):
    board.append(list(map(int,input().split())))
l = list(map(int,input().split()))

for le in l:
    width = 1<<le
    i=0
    j=0
    while i< (1<<n):
        while j< (1<<n):
            rotate(i,j,width)
            j+=width
        i+=width
        j=0
    reduce()
# print(board)

ice =0
big=0
visited = [[False]*(1<<n) for _ in range(1<<n)]

for i in range(1<<n):
    for j in range(1<<n):
        ice+=board[i][j]
        if(not visited[i][j] and board[i][j]!=0):
            bfs(i,j)
print(ice)
print(big)
