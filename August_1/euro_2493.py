# 2493 탑 [골드 5]
# https://www.acmicpc.net/problem/2493
# 시간초과

from sys import stdin

N = int(stdin.readline())
towers = []

for tower in map(int, stdin.readline().split()):
    towers.append(tower)

receives = []
for i in range(N):
    receive = -1
    for j in range(i):
        if towers[i-j-1] > towers[i]:
            receive = i-j-1
            break
    receives.append(receive + 1)

print(" ".join(map(str, receives)))


