# 1941 소문난 칠공주 (G3)
# https://www.acmicpc.net/problem/1941
# 실패

import sys
from collections import deque

input = sys.stdin.readline

direction = [[1, 0], [0, 1]]

result = 0
arr = []
for _ in range(5):
    line = input()
    temp = []
    for i in range(5):
        temp.append(line[i])
    arr.append(temp)

for _ in range(5):
    print(arr[_])

def isValid(i, j):
    return i>=0 and j>=0 and i<5 and j<5

# for i in range(5):
#     for j in range(5):
#         q = deque([[i, j]])
#         count = 0
#         yCount = 0
#         while(len(q) > 0):
#             cur = q.popleft()
            
#             if arr[cur[0]][cur[1]] == 'Y':
#                 yCount += 1
#             if yCount > 3:
#                 break

#             count += 1
#             if count == 7:
#                 result += 1
#             for d in direction:
#                 newI = cur[0] + d[0]
#                 newJ = cur[1] + d[1]
#                 if not isValid(newI, newJ):
#                     continue
#                 q.append([newI, newJ])
        


def dfs(i, j, count, visited, sCount):
    global result

    if (count - sCount > 3):
        return [count, visited, sCount]
    elif (count == 7):
        print(i, j)
        result += 1
        return
    for d in direction:
        newI = i+d[0]
        newJ = j+d[1]
        if (isValid(newI, newJ) and not visited[newI][newJ]):
            visited[newI][newJ] = True
            dfs(newI, newJ, count+1, visited, sCount+1 if arr[newI][newJ] == 'S' else sCount)
            visited[newI][newJ] = False

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, [[False] * 5 for _ in range(5)], 1 if arr[i][j] == 'S' else 0)

print(result)