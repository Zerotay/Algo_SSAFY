# 2170 선 긋기 (G5)
# https://www.acmicpc.net/problem/2170
# 정답

import sys
input = sys.stdin.readline

n = int(input())
lines = {}
for _ in range(n):
  x, y = map(int, input().split())
  if x not in lines:
    lines[x] = 0
  if y not in lines:
    lines[y] = 0
  lines[x] += 1
  lines[y] -= 1
  
lines = sorted(lines.items())
INF = -1_000_000_001

cur = INF
pen = 0
result = 0
for i in range(len(lines)):
  pen += lines[i][1]
  if cur != INF:
    result += lines[i][0] - cur

  if pen > 0:
    cur = lines[i][0]
  else:
    cur = INF

print(result)