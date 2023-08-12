# 0-1 BFS

import collections

n,k = map(int,input().split())
visit = [0 for _ in range(100001)]

def bfs(x):
    global visit
    q = collections.deque()
    cnt=0
    visit[x]=1;
    q.append((x,cnt))
    while q:
        x,cnt = q.popleft()
        if x==k:
            return cnt
        for i in [x-1, x+1, 2*x]:
            if not visit[i]:
                if i==2*x:
                    q.append((i,cnt))
                    visit[i]=1
                else:
                    q.append((i,cnt+1))
                    visit[i]=1;
print(bfs(n))