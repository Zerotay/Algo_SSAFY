import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

dp = [[0,1] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    # 어디가 head인지 알 수 없다.

def dfs(i):
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1
            dfs(j)
            dp[i][0] += dp[j][1]
            dp[i][1] += min(dp[j])

visited[1] = 1
dfs(1)
print(min(dp[1]))