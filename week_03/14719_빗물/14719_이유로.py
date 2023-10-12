# 14719 빗물 (G5)
# https://www.acmicpc.net/problem/14719
# 정답

import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
world = [*map(int, input().split())]

count = 0

for i in range(h):
    for j in range(w):
        if world[j] == i and any(element > i for element in world[:j]) and any(element > i for element in world[j+1:]):
            world[j] += 1
            count += 1
    

print(count)