import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
stack = deque()

ans = [0 for i in range(n)]

for i in range(n):
    while stack:
        if stack[len(stack)-1][1] >= data[i]:
            ans[i] = stack[len(stack)-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, data[i]])

print(*ans)
