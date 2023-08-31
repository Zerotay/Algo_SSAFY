# 1451 직사각형으로 나누기 (G4)
# https://www.acmicpc.net/problem/1451
#

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[*map(int, [c for c in input().rstrip()])] for _ in range(n)]
s = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + arr[i-1][j-1]


def getSum(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]


result = 0

# |||
for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = getSum(1, 1, n, i)
        r2 = getSum(1, i+1, n, j)
        r3 = getSum(1, j+1, n, m)
        if result < r1 * r2 * r3:
            result = r1 * r2 * r3


# =
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = getSum(1, 1, i, m)
        r2 = getSum(i+1, 1, j, m)
        r3 = getSum(j+1, 1, n, m)
        if result < r1 * r2 * r3:
            result = r1 * r2 * r3

# |=
for i in range(1, m):
    for j in range(1, n):
        r1 = getSum(1, 1, n, i)
        r2 = getSum(1, i+1, j, m)
        r3 = getSum(j+1, i+1, n, m)
        if result < r1 * r2 * r3:
            result = r1 * r2 * r3

# =|
for i in range(1, n):
    for j in range(1, m):
        r1 = getSum(1, 1, i, j)
        r2 = getSum(i+1, 1, n, j)
        r3 = getSum(1, j+1, n, m)
        if result < r1 * r2 * r3:
            result = r1 * r2 * r3

# ㅠ
for i in range(1, n):
    for j in range(1, m):
        r1 = getSum(1, 1, i, m)
        r2 = getSum(i+1, 1, n, j)
        r3 = getSum(i+1, j+1, n, m)
        if result < r1 * r2 * r3:
            result = r1 * r2 * r3

# ㅛ
for i in range(1, n):
    for j in range(1, m):
        r1 = getSum(1, 1, i, j)
        r2 = getSum(1, j+1, i, m)
        r3 = getSum(i+1, 1, n, m)
        if result < r1 * r2 * r3:
            result = r1 * r2 * r3

print(result)
