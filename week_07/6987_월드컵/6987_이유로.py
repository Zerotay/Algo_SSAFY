# 6987 월드컵 (G4)
# https://www.acmicpc.net/problem/6987
# 실패

import sys
import copy
from collections import deque

input = sys.stdin.readline

arr = [[*map(int, input().split())] for _ in range(4)]
answer = []
print(arr)
for i in range(4):
  wlValid = True
  for j in range(6):
    if arr[i][3*j] + arr[i][3*j+1] + arr[i][3*j+2] != 5:
      wlValid = False
      break

  if wlValid is False:
    answer.append(0)
    continue

  count = 0
  for j in range(6):
    count += arr[i][3*j] - arr[i][3*j+2]

  if count != 0:
    answer.append(0)
    continue

  answer.append(1)


print(*answer)