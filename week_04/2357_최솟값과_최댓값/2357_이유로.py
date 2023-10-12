# 2357 최솟값과 최댓값 (G1)
# https://www.acmicpc.net/problem/2357
# 시간초과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

for _ in range(m):
    a, b = map(int, input().split())
    print(min(arr[a-1:b]), max(arr[a-1:b]))
