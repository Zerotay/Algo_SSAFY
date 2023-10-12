# 13549 숨바꼭질 3 (G5)
# https://www.acmicpc.net/problem/13549
# 정답

import heapq as hq
n,k = map(int,input().split())
que = [(0,n)]
visited = [1 for i in range(100001)]
while que:
    time, pos = hq.heappop(que)
    visited[pos] = 0
    if pos == k: break
    tmp = pos*2
    if tmp < 100001 and visited[tmp]: hq.heappush(que,(time,tmp))
    tmp = pos-1
    if tmp > -1 and visited[tmp]: hq.heappush(que,(time+1,tmp))
    tmp = pos+1
    if tmp < 100001 and visited[tmp]: hq.heappush(que,(time+1,tmp))
print(time)

# 대충 풀면 시간초과나는 그래프 문제
# 힙소트를 통해 가장 빠른 값을 먼저 빼서 갱신시키듯 풀 수 있음
# 가장 빠른 경로를 찾는 것이라 bfs를 사용함
# 같은 경로 재방문을 막기 위해 방문 배열 사용
# 최악의 경우 배열의 모든 값을 한번씩 방문하므로 1000000까지 반복할 수 있음