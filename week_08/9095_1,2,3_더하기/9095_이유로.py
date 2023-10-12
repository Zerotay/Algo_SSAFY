# 9095 1, 2, 3 더하기 (S3)
# https://www.acmicpc.net/problem/9095
# 정답

import sys
input = sys.stdin.readline

t = int(input())
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 11):
    arr[i] += arr[i-3]
    arr[i] += arr[i-2]
    arr[i] += arr[i-1]

for _ in range(t):
    print(arr[int(input())])