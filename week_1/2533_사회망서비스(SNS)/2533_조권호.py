import collections, sys
sys.setrecursionlimit(10**6)

def dfs(v):
    for i in graph[v]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)
            check[v][0]+=check[i][1]
            check[v][1]+=min(check[i])
            

n = int(input())
graph=collections.defaultdict(list)
check =[[0,1] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1]=1
dfs(1)
print(min(check[1]))
