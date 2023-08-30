# 1092 배 (G5)
# https://www.acmicpc.net/problem/1092
# 성공

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
crane = sorted([*map(int, input().split())], reverse=True)
m = int(input())
box = deque(sorted([*map(int, input().split())]))
boxes = [deque([]) for _ in range(n+1)]
boxes[0] = box

result = 0
for i in range(n):
    if (len(boxes[i]) == 0):
        continue
    while(len(boxes[i]) > 0 and boxes[i][0] <= crane[i]):
        cur = boxes[i].popleft()
        boxes[i+1].append(cur)


if len(boxes[0]) > 0:
    print(-1)
    exit(0)

counts = [*map(len, boxes)][1:]

result = 0
while(max(counts) > 0):
    for i in range(n):
        if counts[i] > 0:
            counts[i] -= 1
        else:
            j = i
            while(j < n-1):
                j += 1
                if (counts[j] > 0):
                    counts[j] -= 1
                    break
        
    result += 1

print(result)