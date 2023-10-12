import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [list(input().rstrip()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
di = ((1,0),(-1,0),(0,1),(0,-1))
key = {chr(i+97):i for i in range(6)}
flag = 0

def reset(x,y):
    que = deque()
    que.append((x,y))
    while que:
        cx,cy = que.popleft()
        for i in range(4):
            nx,ny=cx+di[i][0],cy+di[i][1]
            if -1<nx<n and -1<ny<m and visited[nx][ny]:
                lst[nx][ny]='.'
                visited[nx][ny]=0
                que.append((nx,ny))

# print(lst)
for row in range(n):
    for col in range(m):
        if lst[row][col]=='0':
            que=deque()
            que.append((row,col))
            lst[row][col]='2'
            visited[row][col] = 1 # 0은 미방문의 뜻
            while que:
                # for i in lst:
                #     print(*i)
                # print()
                # for i in visited:
                #     print(*i)
                # print()
                cx,cy=que.popleft()
                for i in range(4):
                    nx,ny=cx+di[i][0],cy+di[i][1]
                    if -1<nx<n and -1<ny<m and lst[nx][ny]!='#' and not visited[nx][ny]:
                        tmp = visited[cx][cy]
                        if lst[nx][ny].islower():
                            if not (flag & 1 << key[lst[nx][ny]]):
                                flag |= 1 << key[lst[nx][ny]]
                                reset(nx,ny)
                                que.clear()
                                lst[nx][ny] = '2'
                                visited[nx][ny] = tmp + 1
                                que.append((nx,ny))
                                break
                            else:
                                lst[nx][ny] = '2'
                                visited[nx][ny] = tmp + 1
                                que.append((nx,ny))
                        elif lst[nx][ny].isupper():
                            if flag & 1 << key[lst[nx][ny].lower()]:
                                lst[nx][ny] = '2'
                                visited[nx][ny] = tmp + 1
                                que.append((nx,ny))
                        elif lst[nx][ny] == '.':
                            lst[nx][ny] = '2'
                            visited[nx][ny] = tmp + 1
                            que.append((nx,ny))
                        elif lst[nx][ny] == '1':
                            print(tmp)
                            exit()
else:
    print(-1)
