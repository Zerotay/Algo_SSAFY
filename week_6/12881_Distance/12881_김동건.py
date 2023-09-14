# 12881 Distance (P5)
# https://www.acmicpc.net/problem/12881
# 정답

import sys
from collections import defaultdict
import heapq as hq

input = sys.stdin.readline
n, k, l = map(int, input().split())
people = [int(input()) for _ in range(n)]
adjlst = defaultdict(list)
for _ in range(l):
    b, c, d = map(int, input().split())
    adjlst[b].append((d, c))
    adjlst[c].append((d, b))

vist = [sys.maxsize] * (k + 1)
que = [(0, people[i]) for i in range(n)]
while que:
    curdist, curnode = hq.heappop(que)
    if vist[curnode] != sys.maxsize:
        print(int((vist[curnode] + (curdist - vist[curnode]) / 2) * 6))
        break
    vist[curnode] = curdist  # 큐에서 나온 시점에 업데이트를 한다. 그래야 해당 간선을 체크하고 있단 표시가 된다.
    for nextdist, nextnode in adjlst[curnode]:
        dist = nextdist + curdist
        if vist[nextnode] > dist:
            hq.heappush(que, (dist, nextnode))

# 접근 1
# 사람이 몇 명이건 간에 어떤 누구든 만나기만 하면 된다.
# 일단 빨리 만나게 해야 한다. 그렇다면 당연히 최단 경로를 찾아야한다
# 사람마다 최단 경로를 재자!
# 사람들이 노드에서 만나는 게 아니라 중간에서 만나는 것이 가능하다.
# 그래서 중요한 것은 어떤 사람이 갈 다음 노드에 다른 사람이 가 있었는 지를 판별하는 것이다.
# 임의의 지점 a,b가 있을 때, 각 지점에 도착한 사람들의 최단 경로 값과 a,bㅅ이의 거리를 이용하면
# 어느 중간 지점에서 만나게 되는지 알 수 있다.

# ex) a에 3의 경로로 도착한 사람, b에 7의 경로로 도착한 사람이 있다.
# a와 b 사이의 거리가 8이다.
# 이것이 최적의 경로임이 보장되는 상황에서, a에 도착한 사람이 b쪽으로 먼저 출발한다.
# b에 있는 도착한 사람이 a쪽으로 출발하기 전에 이미 a 사람은 7-3=4만큼 b로 이동해있을 것이다.
# 그러면 8-4=4 만큼의 거리를 양쪽의 사람이 마주보고 오는 상태가 된다.
# 그러면 4 / 2 = 2만큼의 거리를 걷는데 이동하는 시간을 구하고, a,b중 오래 걸린 쪽에서 도착한 시간을 더하면
# 언제 만나는지 알 수 있게 되는 것이다!

# 이 때 우리는 각각의 사람의 최단 경로가 궁금하기는 하지만, 일단 만나기만 하면 빠르게 종료를 시켜야하기에
# (누구에게 방문됐던)가장 빨리 방문되는 노드가 가장 궁금하다.
# 그렇기 때문에 일단 모든 사람들이 각자 최대한 가까운 노드로 이동하는 케이스를 찾는다
# 이를 위해 모든 사람들을 한 우선순위 큐에 넣어서 돌린다.
# 시작점이 많은 다익스트라인 꼴이다.
# 대신 각 사람이 어딜 방문했는지를 체크하면서 가자.

# -> 메모리 초과

# 접근 2
# 거리를 기준으로 어느 사람인지 안 따지고 한 우선순위큐에 넣어서 돌리는 건 좋다
# 각 사람을 구분해서 거리 체크를 할 필요가 있을까?
# 모든 사람 10만명에 대해 10만 개 노드를 체크하는 공간을 확보하면 당연히 메모리 초과가 난다
# 어차피 누군가가 만난다는 생각만 있으면 되니까, 거리를 기준으로 체크하되
# 그 거리는 각 위치에서 출발하여 이어지게 되는 간선의 길이를 기준으로 생각하면 될 것 같다.
# 그리고 누가 오게 될지는 몰라도 그냥 노드를 기준으로 어떤 사람이 최단 경로로 방문한 거리 기록만 남기면 되겠다
# 둘이 만나는지 체크를 하는 해당 '간선'을 탐색하는 지점. 즉 우선순위큐에서 나오게 되는 시점.
# 우선순위 큐에 넣는 시점은 노드를 탐색하는 시점이라고 할 수 있다.
# -> 사실 이 정도까지 고민하지 않았는데 갑자기 정답;;

# 결국 큐 자체는 간선을 기준으로 돌기 때문에 최악의 경우 최대 간선 개수인 10만번만큼 반복하게 될 것이다.
