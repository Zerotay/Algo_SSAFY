n = int(input())
dp = [[0] * 4 for _ in range(100)]
dp[0][0] = 1
dp[1][0] = 2
dp[1][1] = 1
dp[2][0] = 3
dp[2][1] = 2
dp[2][2] = 1

for i in range(3, 100):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][3]) + 1
    dp[i][1] = dp[i][0] - 1
    dp[i][2] = dp[i - 1][1]
    dp[i][3] = max()


for i in dp[:5]:
    print(i)
# def recur(k):
#     if dp[k]: return dp[k]
#     dp[k] = max(dp[k-1]+1, dp[k-2])
