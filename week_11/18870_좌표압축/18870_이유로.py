# 18870 좌표 압축 (S2)
# https://www.acmicpc.net/problem/18870
# 정답

import sys

input = sys.stdin.readline
 
n = int(input())
arr = [*map(int, input().split())]
 
sortedArr = sorted(list(set(arr)))
dic = {sortedArr[i] : i for i in range(len(sortedArr))}

for num in arr:
    print(dic[num], end = ' ')