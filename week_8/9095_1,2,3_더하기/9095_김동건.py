# 9095 1, 2, 3 더하기(S3)
# https://www.acmicpc.net/problem/9095
# 정답

import sys

input = sys.stdin.readline

dp = [0] * 11
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(*(dp[int(input()) - 1] for _ in range(int(input()))), sep="\n")

# 말할 것 없는 문제. 그냥 dp로 풀 수 있다는 것만 파악하면 끝.
# 3^11도 크지는 않아서 그렇게 풀이해도 상관은 없을 듯
