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
    # print(anslst)
    print(f"Case #{t+1}: {ans if ans < 2147483648 else -1}")
    # print(adjlst)
