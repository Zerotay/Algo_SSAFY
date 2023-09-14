# 12442 약속장소 정하기 (Large) (G4)
# https://www.acmicpc.net/problem/12442
# 정답

import sys
from collections import defaultdict
import heapq as hq


def dijk(start):
    vist = [sys.maxsize] * (n + 1)
    vist[start] = 0
    que = [(0, start)]
    while que:
        curdist, curnode = hq.heappop(que)
        if curdist > vist[curnode]:
            continue
        for nextdist, nextnode in adjlst[curnode]:
            tmp = curdist + nextdist
            if tmp < vist[nextnode]:
                vist[nextnode] = tmp
                hq.heappush(que, (tmp, nextnode))
    return vist[1:]


input = sys.stdin.readline
for t in range(int(input())):
    n, p, m = map(int, input().split())
    friends = [[*map(int, input().split())] for _ in range(p)]
    adjlst = defaultdict(list)
    for _ in range(m):
        tmp = [*map(int, input().split())]
        dist = tmp[0]
        l = tmp[1]
        for i in range(2, l + 1):
            adjlst[tmp[i]].append((dist, tmp[i + 1]))
            adjlst[tmp[i + 1]].append((dist, tmp[i]))
    anslst = [0] * n
    for node, speed in friends:
        least = dijk(node)
        for i in range(n):
            anslst[i] = max(anslst[i], least[i] * speed)
    ans = min(anslst)
    print(f"Case #{t+1}: {ans if ans < 2147483648 else -1}")

# 최단경로 찾기 문제
# 저번 주 문제와 유사함

# 접근 1
# 도로가 어떻게 깔려있는지에 대한 정확하 정보가 주어지지 않기에
# 그리디한 접근 방식은 불가능
# 그럼 각 사람들이 각 노드에 가는 최단 경로를 구해보자
# 노드는 만 개애지만 사람이 100명 이하이므로 대충 시간 상 무리는 없을 듯
# 각 사람이 걸리는 이동 시간은 나중에 곱하는 것으로 한다.
# 성공
