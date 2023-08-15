# 11559 Puyo Puyo (G4)
# https://www.acmicpc.net/problem/11559
# 정답

from collections import deque

lst = [list(input()) for _ in range(12)]
dx,dy=[1,-1,0,0],[0,0,1,-1]
ans = 0

def check(x,y,val):
    if val == '.': return 0
    if not visited[x][y]: return 0 # 이미 방문했던 곳이면 어차피 안 되니 무시
    cnt = 1
    que = deque()
    que.append((x,y))
    visited[x][y] = 0
    stack = []
    while que:
        x,y = que.popleft()
        stack.append((x,y))
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if -1<nx<12 and -1<ny<6 and visited[nx][ny] and lst[nx][ny]==val:
                que.append((nx,ny))
                visited[nx][ny] = 0
                cnt+=1
    if cnt > 3:
        while stack:
            x,y = stack.pop()
            lst[x][y] = '.'
        return 1
    return 0

flag = 1
while flag:
    flag = 0
    visited = [[1] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            flag |= check(i,j, lst[i][j]) # check가 한번이라도 1을 내뱉으면 flag는 무조건 1로 고정된다.
    if not flag: break
    ans += 1
    for i in range(6):
        fall = 1
        j = 11
        while fall and -1<j:
            fall = 0
            if lst[j][i] != '.':
                fall = 1
                j-=1
            else:
                k = j-1
                while -1<k and lst[k][i] == '.': k-=1
                if k>-1:
                    lst[k][i],lst[j][i] = lst[j][i],lst[k][i]
                    fall = 1
                    j-=1

print(ans)

# 구현이 빡센 그래프 탐색 문제
# 크게 두 가지 행동을 반복을 돌린다.

# 4개 이상 모인 블록을 부수는 행동, 폭발을 거친 후 지면에 붙도록 하는 행동.
# 부수는 행동의 경우 모든 지점을 탐색해야 하며 dfs,bfs 전부 사용가능하다.
# 요지는 방문체크를 잘 하는 것.
# 부수기 위해 드는 시간은 최악의 경우 모든 위치를 확인해야 하나 전부 터지지 않는 케이스.
# 6 * 12 * 4만큼의 반복을 하게 된다(이것조차 줄이기 위해 visited를 활용했다).

# 지면에 붙이는 행동은 각 열 별로 접근한다.
# 아래쪽의 빈 공간을 찾고, 그 빈 공간에 들어가야하는 블록을 찾는다.
# 최악을 고려해보자. 11개가 1칸씩 이동, 10개가 2칸씩 이동, 9개가 3칸씩 이동 ...
# 6개가 6칸씩 이동하는 36번이 각 열에서 일어날 수 있는 최대 반복인 듯.
# 6 * 6 * 6이 최대 반복횟수일 듯하다.