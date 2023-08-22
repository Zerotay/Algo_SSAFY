# 20058 마법사 상어와 파이어스톰 (G3)
# https://www.acmicpc.net/problem/20058
# 시간초과

import sys
from collections import deque
import copy
input = sys.stdin.readline

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
n, q = map(int, input().split(' '))
totalSize = pow(2, n)
a = [[*map(int, input().split(' '))] for _ in range(totalSize)]

def turn(startI, endI, startJ, endJ, original):
    global totalSize
    arr = [[*original[i][:]] for i in range(totalSize)]
    # arr = copy.deepcopy(original)
    newArr = []
    size = endI - startI
    for i in range(size):
        row = []
        for j in range(size):
            row.append(arr[endI - 1 - j][startJ + i])
        newArr.append(row)

    for i in range(size):
        for j in range(size):
            arr[i + startI][j + startJ] = newArr[i][j]
    
    return arr

def magic(arr):
    global direction
    global totalSize
    reduce = []
    for i in range(totalSize):
        for j in range(totalSize):
            count = 0
            for d in direction:
                newI = i + d[0]
                newJ = j + d[1]

                if not (0 <= newI < totalSize and 0 <= newJ < totalSize):
                    continue

                if arr[newI][newJ] > 0:
                    count += 1

            if (count < 3 and arr[i][j] > 0):
                reduce.append([i, j])

    for r in reduce:
        arr[r[0]][r[1]] -= 1
    return arr

for l in [*map(int, input().split(' '))]:
    i = 0
    j = 0
    size = pow(2, l)

    if l != 0:
        while(i < totalSize):
            while(j < totalSize):
                a = turn(i, i+size, j, j+size, a)
                j += size
            j = 0
            i += size
    a = magic(a)



visited = [[False] * totalSize for _ in range(totalSize)]
iceSum = 0
maxIceSize = 0
for i in range(totalSize):
    for j in range(totalSize):
        iceSum += a[i][j]
        if a[i][j] == 0 or visited[i][j] == True:
            visited[i][j] = True
            continue
    
        iceSize = 0
        queue = deque([[i, j]])
        visited[i][j] = True
        while(len(queue) > 0):
            cur = queue.popleft()
            iceSize += 1
            for d in direction:
                newI = cur[0] + d[0]
                newJ = cur[1] + d[1]
                if not (0 <= newI < totalSize and 0 <= newJ < totalSize):
                    continue
                if (not visited[newI][newJ]) and (a[newI][newJ] > 0):
                    queue.append([newI, newJ])
                    visited[newI][newJ] = True
        if iceSize > maxIceSize:
            maxIceSize = iceSize

print(iceSum)
print(maxIceSize)


