import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
arr = [sys.stdin.readline().rstrip().split() for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0': 
            count += 1
        
def isValid(i, j, N, M):
    return i >= 0 and j >= 0 and i < N and j < M

day = 0

while(count > 0):
    change = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                for d in direction:
                    newI = i+d[0]
                    newJ = j+d[1]
                    if isValid(newI, newJ, N, M) and arr[newI][newJ] == '0' and [newI, newJ] not in change:
                        change.append([newI, newJ])

    if len(change) == 0:
        break
    else:
        for c in change:
            arr[c[0]][c[1]] = '1'
            count -= 1
        day += 1

if count != 0:
    print(-1)
else:
    print(day)



