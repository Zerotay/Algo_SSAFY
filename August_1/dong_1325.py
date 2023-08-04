import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    e,s = map(int,input().split())
    lst[s].append(e)

ans = []

maxcnt = 0
for i in range(1,n+1):
    visited=[0 for _ in range(n+1)]
    que = deque()
    que.append(i)
    visited[i] = 1
    tmp = 0
    while que:
        node = que.popleft()
        for j in lst[node]:
            if not visited[j]:
                que.append(j)
                visited[j] = 1
                tmp += 1
    if maxcnt < tmp:
        maxcnt = tmp
        ans = [i]
    elif maxcnt == tmp:
        ans.append(i)

# 사이클이 있으면 위상정렬은 불가능하다. 다른 방법은 없을까
print(*ans)
