# 16987 계란으로 계란치기 (G5)
# https://www.acmicpc.net/problem/16987
# 시간초과

import sys
input = sys.stdin.readline

N = int(input())
eggs = []

for i in range(N):
    durability, weight = map(int, input().split())
    eggs.append([durability, weight])

def progress(arr, hit, n):
    if hit == n:
        return 0
    countArr = []
    for i in range(n):
        tempArr = [item[:] for item in arr]
        count = 0
        if (i != hit and tempArr[i][0] > 0 and tempArr[hit][0] > 0):
            tempArr[i][0] -= tempArr[hit][1]
            tempArr[hit][0] -= tempArr[i][1]
            if tempArr[i][0] < 0:
                count += 1
            if tempArr[hit][0] < 0:
                count += 1

        countArr.append(progress(tempArr, hit+1, n)+count)

    return max(countArr)

print(progress(eggs, 0, N))
        