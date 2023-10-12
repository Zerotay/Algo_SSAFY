# 1941 소문난 칠공주 (G3)
# https://www.acmicpc.net/problem/1941
# 정답

from collections import deque
lst=[list(input()) for _ in range(5)]
ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
v = [[0] * 5 for _ in range(5)]

def recur(start,ycnt, leng):
    if ycnt>3: return
    if leng==7:
        que = deque()
        for i in range(5):
            for j in range(5):
                if v[i][j]:
                    connected = 0
                    que.append((i,j))
                    re = []
                    v[i][j] = 0
                    while que:
                        x,y = que.popleft()
                        re.append((x,y))
                        connected+=1
                        for i in range(4):
                            nx,ny = x+dx[i],y+dy[i]
                            if -1<nx<5 and -1<ny<5 and v[nx][ny]:
                                v[nx][ny] = 0
                                que.append((nx,ny))
                    if connected==7:
                        global ans
                        ans+=1
                    for x,y in re:
                        v[x][y] = 1
                    return
        return
    for i in range(start, 25):
        x,y = divmod(i, 5)
        v[x][y] = 1
        recur(i+1,ycnt+1 if lst[x][y]=='Y' else ycnt, leng+1)
        v[x][y] = 0

recur(0,0,0)
print(ans)

# 생각보다 어려웠던 문제
# 단순 dfs로는 접근할 수 없다.
# 한 경로를 구하는 게 아니라 7원소의 조합을 구하는 것이기 때문
# 조합을 통해 원소를 선택한 후 그게 인접한지 확인한다
# 조합을 구하면서 Y개수 조건을 두고 가지치기한다.
# 최대 25C3이므로 2300정도의 가짓수가 나온다.