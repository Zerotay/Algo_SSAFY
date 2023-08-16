# 14411 합집합 (G4)
# https://www.acmicpc.net/problem/14411
# 시간 초과 / 메모리 초과

import sys
input = sys.stdin.readline

n = int(input())
arr = []

max = 0
for i in range(n):
    x, y = map(int, input().split())
    x2 = int(x/2)
    y2 = int(y/2)
    if (x2 > max):
        max = x2
    if (y2 > max):
        max = y2
    arr.append([int(x/2), int(y/2)])

positions = [[False]*max for i in range(max)]

for square in arr:
    for i in range(square[0]):
        for j in range(square[1]):
            positions[i][j] = True

quarter = 0
for square in positions:
    for pos in square:
        if pos:
            quarter += 1


# sortedArr = sorted(arr, key=lambda i: (i[0]))
# sum = []
# for i in range(n):
#     if i == 0:
#         sum

# quarter = 0
# for i in range(n):
#     max = sortedArr[i][1]
#     for j in range(n):
#         if sortedArr[i][0] <= sortedArr[j][0] and sortedArr[j][1] > max:
#             max = sortedArr[j][1] 
#     if i == 0:
#         quarter += sortedArr[i][0] * max
#     else:
#         quarter += (sortedArr[i][0] - sortedArr[i-1][0]) * max

print(quarter * 4)