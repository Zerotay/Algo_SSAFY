import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000)
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    com1, com2 = map(int, input().split())

    graph[com2].append(com1)

res = [0 for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

max_res = 0


def dfs(num, chk):

    visit[num] = chk
    cnt = 1
    for i in graph[num]:
        if visit[i] == chk:
            continue
        cnt += dfs(i, chk)

    return cnt


for i in range(1, N+1):

    res[i] = dfs(i, i)

    max_res = max(res[i], max_res)

for i in range(1, N+1):
    if res[i] == max_res:
        print(i, end=' ')
# 메모리 초과
