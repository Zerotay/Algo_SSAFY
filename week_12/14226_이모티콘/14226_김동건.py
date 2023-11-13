# 14226 이모티콘 (G4)
# https://www.acmicpc.net/problem/14226
# 정답

from collections import deque
n=int(input())
que = deque()
que.append((1, 0))
dp = dict()
dp[(1,0)]=0
while que:
    # print(que)
    val, clip = que.popleft()
    if val == n:
        print(dp[(val, clip)])
        exit()
    if (val, val) not in dp:
        dp[(val,val)] = dp[(val, clip)]+1
        que.append((val,val))
    if (val+clip, clip) not in dp:
        dp[(val+clip, clip)] = dp[(val, clip)]+1
        que.append((val+clip, clip))
    if (val-1, clip) not in dp:
        dp[(val-1, clip)] = dp[(val, clip)]+1
        que.append((val-1, clip))
    
# 접근 1
# 횟수를 늘려나가는 bfs로 가자
# 모든 행동을 다 해본다.
# 대신 val이 0 이하로 가거나, clip이 0일 때는 별도의 행동을 하지 말자
# -> 시간 초과
# 
# 접근 2
# 값을 저장하면서 나아가자
# 현재 값도 중요하지만, 그 동시에 현재 클립보드 상태도 중요하다
# 두 가지 값을 고유하게 해서 방문체크 하자
# ->성공    

