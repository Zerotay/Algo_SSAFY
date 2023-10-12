import sys

input = sys.stdin.readline

c, n = map(int, input().split())
lst = [[*map(int, input().split())] for _ in range(n)]
mst = 100001
dp = [[0] * mst for _ in range(n)]

ans = sys.maxsize

for i in range(mst):
    dp[0][i] = (i // lst[0][0]) * lst[0][1]
    if c <= dp[0][i]:
        ans = min(ans, i)

for i in range(1, n):
    cost = lst[i][0]
    customer = lst[i][1]
    for j in range(mst):
        if j - cost > -1:
            dp[i][j] = max(
                dp[i - 1][j], dp[i - 1][j - cost] + customer, dp[i][j - cost] + customer
            )
        else:
            dp[i][j] = dp[i - 1][j]

        if c <= dp[i][j]:
            ans = min(ans, j)
print(ans)
