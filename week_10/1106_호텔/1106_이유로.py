# 1106 호텔 (G5)
# https://www.acmicpc.net/problem/1106
# 정답

import sys
input = sys.stdin.readline

c, n = map(int, input().split())



arr = []
for i in range(n):
  cost, customer = map(int, input().split())
  arr.append([cost, customer])

np = [100000] * 1101
np[0] = 0



for i in range(1101):
  for a in arr:
    if i-a[1] >= 0:
      np[i] = min(np[i], np[i-a[1]] + a[0])

m = np[c]
for i in range(c, 1101):
  m = min(m, np[i])
print(m)
