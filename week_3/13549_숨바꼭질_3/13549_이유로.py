# 13549 숨바꼭질 3 (G5)
# https://www.acmicpc.net/problem/13549
# 시간초과 -> 메모리초과

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([[5, 0]])

while(len(queue) > 0):
    current = queue.popleft()
    if (current[0] == k):
        print(current[1])
        break

    queue.append([current[0]*2, current[1]])
    queue.append([current[0]+1, current[1]+1])
    queue.append([current[0]-1, current[1]+1])
