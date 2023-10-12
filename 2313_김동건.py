# 실패

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    l = int(input())
    length = l
    lst = [*map(int, input().split())]
    dp = [[0, 0, 0] for _ in range(l)]
    dp[0] = [lst[0], 0, 0]
    maxval = 0
    left = right = 0
    start = end = 0
    sumlst = [0] * l
    sumlst[0] = lst[0]
    for i in range(1, l):
        # if lst[i] > 0:
        #     tmp = dp[i - 1] + lst[i]
        #     end = i
        # else:
        #     tmp = dp[i - 1]
        # dp[i] = tmp

        sumlst[i] = sumlst[i - 1] + lst[i]
        if sumlst[i] > 0:
            end = i
            if sumlst[i] > maxval:
                maxval = sumlst[i]
                left = start
                right = end
        elif sumlst[i] == 0:

        if sumlst[i] < 0:
            start = -1
            end = i



print(sumlst)

# dp를 쓰자
# 각 위치를 끝점으로 하는 가장 큰 값 찾기
