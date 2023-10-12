# 11559 Puyo Puyo (G4)
# https://www.acmicpc.net/problem/11559
# 정답

import sys
from collections import deque
input = sys.stdin.readline

map = [["x"] * 12 for _ in range(6)]
for i in range(12):
    line = input()
    map[0][11-i] = line[0]
    map[1][11-i] = line[1]
    map[2][11-i] = line[2]
    map[3][11-i] = line[3]
    map[4][11-i] = line[4]
    map[5][11-i] = line[5]

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def isValid(i, j):
    return i>=0 and j>=0 and i<6 and j<12

count = 0

while True:
    visited = [[False]*12 for _ in range(6)]
    
    delete = []
    for i in range(6):
        for j in range(12):
            if (map[i][j] != '.' and visited[i][j] == False):
                queue = deque([[i, j]])
                newDelete = [[i, j]]
                while len(queue) > 0:
                    c = queue.popleft()
                    if (c not in newDelete):
                        newDelete.append(c)
                    for d in direction:
                        newI = c[0] + d[0]
                        newJ = c[1] + d[1]
                        if isValid(newI, newJ) and map[newI][newJ] == map[i][j] and (visited[newI][newJ] == False):
                            visited[newI][newJ] = True
                            queue.append([newI, newJ])
                if len(newDelete) >= 4:
                    delete += newDelete
    
                    
    delete = sorted(delete, key=lambda x: (x[0], -x[1]))
    # print(delete)
    if (len(delete) == 0):
        break

    for d in delete:
        map[d[0]] = map[d[0]][:d[1]] + map[d[0]][d[1]+1:]
        map[d[0]].append('.')
    
    count += 1

print(count)

        
