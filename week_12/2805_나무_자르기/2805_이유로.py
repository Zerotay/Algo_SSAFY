# 2805 나무 자르기 (S2)
# https://www.acmicpc.net/problem/2805
# 정답

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = [*map(int, input().split())]
start, end = 1, sum(t)

while(start <= end):
  mid = (start + end) // 2
  count = 0

  for tree in t:
    if tree > mid:
      count += tree - mid
  
  if count >= m:
    start = mid + 1
  else:
    end = mid - 1