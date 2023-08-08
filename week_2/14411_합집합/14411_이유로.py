# 14411 합집합 (G4)
# https://www.acmicpc.net/problem/14411
# 시간 초과

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([int(x/2), int(y/2)])

sortedArr = sorted(arr, key=lambda i: (i[0]))

sum = 0
for i in range(n):
    max = sortedArr[i][1]
    for j in range(n):
        if sortedArr[i][0] <= sortedArr[j][0] and sortedArr[j][1] > max:
            max = sortedArr[j][1] 
    if i == 0:
        sum += sortedArr[i][0] * max
    else:

        sum += (sortedArr[i][0] - sortedArr[i-1][0]) * max

print(sum * 4)