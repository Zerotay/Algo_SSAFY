import math

n = int(input())
inlst = [*map(int, input().split())]

dp = [[0] * 20 for _ in range(n)]
dp[0][inlst[0]] += 1

for i in range(1, n - 1):
    print(inlst[i])
