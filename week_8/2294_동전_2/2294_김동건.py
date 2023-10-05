# 2294 동전 2(G5)
# https://www.acmicpc.net/problem/2294
# 정답

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
dp = [10001] * 100001
dp[0] = 0
for i in lst:
    for j in range(i, 10001):
        dp[j] = min(dp[j], dp[j - i] + 1)
print(dp[k] if dp[k] != 10001 else -1)

# dp 문제
# 상태공간은 해당 값을 만드는데 들어가는 횟수로 정의한다.
# 냅색과 유사하게, 각 값을 순회를 돌면서 그 값이 있었을 때와 없었을 때의 최소값을 취한다.
