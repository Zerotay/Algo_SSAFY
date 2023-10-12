# 1325 효율적인 해킹 [실버 1]
# https://www.acmicpc.net/problem/1325
# 시간 초과

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
arr = [[] for i in range(N+1)]


for i in range(M):
    a, b = map(int, stdin.readline().split())
    arr[b].append(a)


def hacking(index, count, visit):
    next = []
    for i in arr[index]:
        if visit[i] == False:
            visit[i] = True
            next.append(hacking(i, count+1, visit))
    if len(next) == 0:
        return count
    else:
        return max(next)

hackingCount = [0]
for i in range(1, N+1):
    hackingCount.append(hacking(i, 1, [False]*(N+1)))

for i in range(1, N+1):
    if hackingCount[i] == max(hackingCount):
        print(i, end=" ")
print()