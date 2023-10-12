# 1446 지름길 (S1)
# https://www.acmicpc.net/problem/1446
# 정답

import sys
import copy
from collections import deque

input = sys.stdin.readline

n, d = map(int, input().split())
roads = []
for _ in range(n):
  start, end, dist = map(int, input().split())
  roads.append([start, end, dist])

roads = sorted(roads, key=lambda x: -x[0])

def go(roads, current, dest, count):
  if len(roads) == 0:
    return count + (dest - current)

  curRoad = roads[-1]

  if (curRoad[0] < current or curRoad[1] > dest):
    return go(roads[:-1], current, dest, count)
  else:
    return min(go(roads[:-1], current, dest, count), go(roads[:-1], curRoad[1], dest, count + curRoad[2] + (curRoad[0]-current)))


print(go(roads, 0, d, 0))
