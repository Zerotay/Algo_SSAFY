import collections

graph = collections.defaultdict(list)

def bfs(v):
    cnt=1
    visited = [0 for _ in range(n+1)]
    q = collections.deque([v])
    visited[v]=1
    while q:
        v = q.popleft()
        for p in graph[v]:
            if not visited[p]:
                q.append(p)
                visited[p]=1
                cnt +=1
    return cnt

n,m = map(int,input().split())

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

tmp=[]
cnt_max=-1
for i in range(1,n+1):
    count = bfs(i)
    if count>=cnt_max:
        cnt_max = count
        tmp.append((i, count))
tmp.sort()
for t in tmp:
    if t[1]==cnt_max:
        print(t[0], end=' ')
