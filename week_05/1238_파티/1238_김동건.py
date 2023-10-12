import sys
from collections import defaultdict
import heapq as hq
input = sys.stdin.readline
n,m,x = map(int, input().split())
lst = defaultdict(list)
for _ in range(m):
    start, end, dist = map(int, input().split())
    lst[start-1].append((end-1, dist))

def dkstr(start, end):
    visited = [sys.maxsize] * n
    visited[start] = 0
    que = [(0,start)]
    while que:
        curdist, curnode = hq.heappop(que)
        if visited[curnode] < curdist: continue
        for nextnode, nextdist in lst[curnode]:
            tmpdist = visited[curnode] + nextdist
            if visited[nextnode] > tmpdist:
                visited[nextnode] = tmpdist
                hq.heappush(que,(tmpdist, nextnode))
    return visited[end]

ans = 0
for i in range(n):
    if i==x: continue
    ans = max(ans, dkstr(i,x-1)+dkstr(x-1,i))
print(ans)