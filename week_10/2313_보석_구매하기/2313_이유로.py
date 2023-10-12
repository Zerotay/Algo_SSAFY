# 2313 보석 구매하기 (S1)
# https://www.acmicpc.net/problem/2313
# 시간초과

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

answer = 0
answers = []

for i in range(n):
  l = int(input())
  nums = [*map(int, input().split())]
  sum = 0
  sums = [0]
  idx = []
  for c in range(len(nums)):
    sum += nums[c]
    sums.append(sum)
    idx.append(c)

  result = [-1, -1, -10000]
  combi = list(combinations(idx, 2))
  for a, b in combi:
    if result[2] < sums[b] - sums[a] or (result[2] == sums[b] - sums[a] and  b-a < result[1]-result[0]):
      result[0] = a + 1
      result[1] = b
      result[2] = sums[b] - sums[a]
  
  answer += result[2]
  answers.append(str(result[0]) + " " + str(result[1]))

print(answer)
for ans in answers:
  print(ans)
  
  