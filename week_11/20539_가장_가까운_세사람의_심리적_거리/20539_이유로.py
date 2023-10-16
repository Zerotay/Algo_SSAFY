# 20539 가장 가까운 세 사람의 심리적 거리 (S1)
# https://www.acmicpc.net/problem/20539
# 시간초과

import sys
from itertools import combinations
input = sys.stdin.readline


t = int(input())
for _ in range(t):
  n = int(input())
  arr = []
  
  arr = [*input().split()]
  answer = 100000
  
  for a, b, c in combinations(arr, 3):
    distance = 0
    for i in range(4):
      if (a[i] != b[i]):
        distance += 1
      if (b[i] != c[i]):
        distance += 1
      if (c[i] != a[i]):
        distance += 1
    answer = min(answer, distance)
    
  
  print(answer)