# 1446 지름길 (S1)
# https://www.acmicpc.net/problem/1446
# 정답

import sys
from collections import defaultdict
import heapq as hq

input = sys.stdin.readline

n, d = map(int, input().split())
adjlst = defaultdict(list)
for _ in range(n):
    a, b, c = map(int, input().split())
    if a >= d:
        continue
    if b > d:
        continue
    adjlst[a].append((c, b))
for i in range(d):
    adjlst[i].append((1, i + 1))
vist = [sys.maxsize] * (d + 1)
vist[0] = 0
que = [(0, 0)]
while que:
    curdist, curnode = hq.heappop(que)
    if curdist > vist[curnode]:
        continue
    for nextdist, nextnode in adjlst[curnode]:
        dist = curdist + nextdist
        if dist < vist[nextnode]:
            vist[nextnode] = dist
            hq.heappush(que, (dist, nextnode))
print(vist[d])

# 지름길을 타면 무조건 이득을 보니 그리디하게?
# 특정 지름길을 안 타야 더 좋은 지름길을 탈 수 있는 경우도
# 다익스트라로 최단 경로 탐색하자
