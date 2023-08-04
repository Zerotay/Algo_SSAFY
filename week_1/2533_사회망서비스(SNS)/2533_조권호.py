import collections

def bfs(v, cnt):
    q = collections.deque()
    q.append((v,cnt))
    visited =[0 for _ in range(n+1)]
    visited[1]=1
    while q:
        v, cnt = q.popleft()
        for i in graph[v]:
            if(not visited[i]):
                visited[i] = cnt
                print(i,"visit", visited[i])
                q.append((i, cnt+1))
    return visited

n = int(input())
graph=collections.defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = bfs(1, 1)

count=0
print(visit)
for vi in visit:
    if vi%2==1:
        count+=1
count -=1
print(count)
count = min(count, n-count)
print(count)