# 20058 마법사 상어와 파이어스톰 (G3)
# https://www.acmicpc.net/problem/20058
# 정답

import sys
from collections import deque
input = sys.stdin.readline
n,q = map(int, input().split())
total = 1<<n
lst = [[*map(int, input().split())] for _ in range(total)]

command = [*map(int, input().split())]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

# def turn(x,y,val,dst):
#     if val == dst:
#         size = 1<<val
#         tmp = [[0] * size for _ in range(size)]
#         for i in range(size):
#             for j in range(size):
#                 tmp[i][j] = lst[x+size-j-1][y+i]
#         for i in range(size):
#             for j in range(size):
#                 lst[x+i][y+j] = tmp[i][j]
#         return
#     val-=1
#     size = 1<<val
#     turn(x,y,val,dst)
#     turn(x+size,y,val,dst)
#     turn(x,y+size,val,dst)
#     turn(x+size,y+size,val,dst)

def turn(size):
    size = 1 << size
    tmp = [i[:] for i in lst]
    for i in range(0,total,size):
        for j in range(0,total,size):
            for r in range(size):
                for c in range(size):
                    lst[i+r][j+c] = tmp[i+size-1-c][j+r]

def melt():
    meltlst = deque()
    for i in range(total):
        for j in range(total):
            if lst[i][j]:
                side = 0
                for k in range(4):
                    nx,ny=i+dx[k],j+dy[k]
                    if -1<nx<total and -1<ny<total and lst[nx][ny]:
                        side +=1
                if side<3: meltlst.append((i,j))
    for x,y in meltlst: lst[x][y] -= 1

for i in command:
    # turn(0,0,n,i)
    turn(i)
    melt()

anssum=0
anssize=0
que = deque()
for i in range(total):
    for j in range(total):
        if lst[i][j]:
            currsize=0
            que.append((i,j))
            anssum+=lst[i][j]
            lst[i][j] = 0
            while que:
                x,y=que.popleft()
                currsize+=1
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if -1<nx<total and -1<ny<total and lst[nx][ny]:
                        anssum += lst[nx][ny]
                        lst[nx][ny] = 0
                        que.append((nx,ny))
            anssize = max(anssize, currsize)

print(anssum)
print(anssize)

# 까다로운 구현 유형의 총체
# 분할 정복으로 들어가 배열 돌리기를 진행하고
# 이후 그래프 탐색으로 큰 사이즈의 그래프를 구해야 함.
# 순서대로만 하면 별 거 아니지만, 문제 예시가 사람을 조금 헷갈리게 함..
# 개인적으로는 구현 문제에서 시간 복잡도 고민하는 건 사치가 아닌가..

# 배열 돌리는 원리만 이해하면 분할정복을 쓰지 않고도 바로 값을 수정하는 것도 가능