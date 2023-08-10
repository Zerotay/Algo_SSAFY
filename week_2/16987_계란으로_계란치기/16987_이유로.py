# 16987 계란으로 계란치기 (G5)
# https://www.acmicpc.net/problem/16987
# 진행중 (예제 5, 7 실패)

import sys
input = sys.stdin.readline

N = int(input())
eggs = []

for i in range(N):
    durability, weight = map(int, input().split())
    eggs.append([durability, weight])

def progress(arr, hit):
    if hit == N:
        return 0
    countArr = [0]
    for i in range(N):
        if (i == hit):
            continue
        tempArr = [item[:] for item in arr]
        count = 0
        if (tempArr[i][0] < 0 or tempArr[hit][0] < 0):
            continue
        else:
            tempArr[i][0] -= tempArr[hit][1]
            tempArr[hit][0] -= tempArr[i][1]
            if tempArr[i][0] < 0:
                count += 1
            if tempArr[hit][0] < 0:
                count += 1
        countArr.append(progress(tempArr, hit+1)+count)

    return max(countArr)

print(progress(eggs, 0))
        