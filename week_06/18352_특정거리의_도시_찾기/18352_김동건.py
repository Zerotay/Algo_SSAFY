# 18352 특정 거리의 도시 찾기 (S2)
# https://www.acmicpc.net/problem/18352
# 정답
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
adjlst = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    adjlst[a].append(b)
que = deque([(x, 0)])
vist = [0] * (n + 1)
vist[x] = -1
while que:
    cur, dist = que.popleft()
    if dist > k:
        break
    for nt in adjlst[cur]:
        if vist[nt]:
            continue
        vist[nt] = dist + 1
        que.append((nt, dist + 1))
ans = [i for i in range(n + 1) if vist[i] == k]
if ans:
    print(*ans, sep="\n")
else:
    print(-1)

# 간선이 없는 상태에서 최단 경로 구하기 문제
# 간선이 없다면 방문하는 순서만 따지면 되니 bfs를 사용한다
# 특정 거리를 넘기는 노드들은 더 이상 볼 필요가 없기 때문에 생략한다
# 단방향아라는 점에 유의한다
