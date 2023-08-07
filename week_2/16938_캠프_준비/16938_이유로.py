# 16938 캠프 준비 (G5)
# https://www.acmicpc.net/problem/16938
# 성공

import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
problems = input().split()
isSelected = [False] * N
count = 0

def subset(cnt):
    global count
    if cnt == N:
        arr = []
        sum = 0
        for i in range(N):
            if (isSelected[i]):
                arr.append(int(problems[i]))
                sum += int(problems[i])
        if (sum >= L and sum <= R) and (max(arr) - min(arr) >= X) and len(arr) >= 2:
            count += 1
        return

    isSelected[cnt] = True
    subset(cnt+1)
    isSelected[cnt] = False
    subset(cnt+1)

subset(0)
print(count)
