# 2294 동전 2 (G5)
# https://www.acmicpc.net/problem/2294
# 정답

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [0] * n
dp = [-1] * (k+1)
dp[0] = 0
for i in range(n):
  coins[i] = int(input())

for i in range(k+1):
  c = []
  for j in range(n):
    if i >= coins[j] and dp[i - coins[j]] != -1:
      c.append(dp[i - coins[j]] + 1)
  if len(c) > 0:
    dp[i] = min(c)

print(dp[k])