import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    l = int(input())
    length = l
    maxLst = []
    lst = [*map(int, input().split())]
    dp = [[0,0,0] for _ in range(l)]
    dp[0] = [lst[0],0,0]
    maxval = 0
    for i in range(1, l):

        if lst[i] > 0:
            tmp = dp[i-1]+lst[i]
            end = i
        else:
            tmp = dp[i-1]
        dp[i] = tmp


        dp[i] = dp[i-1]+lst[i]
        if dp[i] > maxval:
            maxval = dp[i]






    maxval = max(sumlst)
    for i in range(l):
        if sumlst[i] == maxval:
            maxLst.append(i)
    for i in reversed(maxLst):


    print(sumlst)

# dp를 쓰자
# 각 위치를 끝점으로 하는 가장 큰 값 찾기