# 18352 특정 거리의 도시 찾기 (S2)
# https://www.acmicpc.net/problem/18352
# 정답

import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)

def dijkstra(arr, start):
  distances = [float('inf')] * len(arr)
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    current_distance, current_destination = heapq.heappop(queue)

    if distances[current_destination] < current_distance: 
      continue
    
    for new_destination in arr[current_destination]:
      distance = current_distance + 1
      if distance < distances[new_destination]:
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])
    
  return distances

count = 0
result = dijkstra(arr, x)
for i in range(len(result)):
  if result[i] == k:
    print(i)
    count += 1

if count == 0:
  print(-1)