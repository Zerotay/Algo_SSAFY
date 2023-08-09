import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
stack = deque()
line = deque()
check = deque()
temp = []
for _ in range(n):
    temp.append(list(map(str, input().split())))
for i in range(n):
    for s in temp[i]:
        alpha = ord(s[0]) - ord('A')
        num = int(s[2:])
        line.append(alpha*1000 + num)

check.append(sorted(line))

while line:
    tmp = line.popleft()
    if tmp == check[0]:
        check.popleft()
        continue
    while stack and stack[0] == check[0]:
        stack.popleft()
        check.popleft()
    stack.append(tmp)
    
if stack and stack[0] < tmp:
    print("BAD")
else:
    print("GOOD")
