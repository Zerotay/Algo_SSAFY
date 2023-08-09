# 16987 계란으로 계란치기 (G5)
# https://www.acmicpc.net/problem/16987
# 진행중

import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    durability, weight = map(int, input().split())
    arr.append([durability, weight])

hit = [0] * N
max = 0

for i in range(N):
    arr = progress(arr, i)
    count = []

def progress(arr, hit):
    countArr = []
    for i in range(N):
        tempArr = arr[:]
        count = 0
        if (i == hit or tempArr[i][0] < 0 or tempArr[hit][0] < 0):
            continue
        else:
            tempArr[i][0]  = tempArr[i][0] - tempArr[hit][1]
            tempArr[hit][0]  = tempArr[hit][0] - tempArr[i][1]
            if tempArr[i][0] < 0:
                count += 1
            if tempArr[hit][0] < 0:
                count += 1
        countArr.append(count)

    countArr.index(max(countArr))

print(max)
        